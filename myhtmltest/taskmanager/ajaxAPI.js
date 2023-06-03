$(document).ready(function() {
    const taskInputEl = $("#todo-inputs");
    const taskOutputEl = $("#tasks");
    const filters = $(".edit-options p");
    const clearEl = $("#btn-clear");
    const apiUrl = "https://api.example.com/tasks"; // Replace with your API URL
  
    let todos = [];
  
    // Fetch tasks from the API
    function fetchTasks() {
      $.ajax({
        url: apiUrl,
        method: "GET",
        success: function(response) {
          todos = response.data;
          showTodoList("all");
        },
        error: function() {
          showError("Failed to fetch tasks from the API.");
        }
      });
    }
  
    // Save tasks to the API
    function saveTasks() {
      $.ajax({
        url: apiUrl,
        method: "POST",
        data: {
          tasks: todos
        },
        success: function() {
          showSuccess("Tasks saved successfully.");
        },
        error: function() {
          showError("Failed to save tasks to the API.");
        }
      });
    }
  
    // Delete task from the API
    function deleteTaskFromAPI(taskId) {
      $.ajax({
        url: apiUrl + "/" + taskId,
        method: "DELETE",
        success: function() {
          showSuccess("Task deleted successfully.");
        },
        error: function() {
          showError("Failed to delete task from the API.");
        }
      });
    }
  
    filters.on("click", function() {
      const filter = $(".options.active");
      filter.removeClass("active");
      $(this).addClass("active");
      showTodoList($(this).attr("id"));
    });
  
    function showTodoList(filter) {
      let li = "";
      if (todos) {
        todos.forEach(function(todo, id) {
          let isCompleted = todo.status === "completed" ? "checked" : "";
          if (filter === todo.status || filter === "all") {
            li += `<li class="task-items">
              <div class="input-task">
                   <label class="container">
                     <input onclick="updateStatus(this)" type="checkbox" id="${id}" ${isCompleted} />
                     <div class="checkmark"></div>
                   </label>
                   <label for="${id}" class="todo ${isCompleted}">${todo.name}</label>
              </div>
              <div class="setting">
                <i onclick="showMenu(this)" class="fa-solid fa-ellipsis-vertical del-icon"></i>
                <ul class="task-menu">
                  <li id="task-del" onclick="editTask(${id},'${todo.name}')"><i class="fa-solid fa-pen"></i>Edit</li>
                  <li id="task-edit" onclick="deleteTask(${id})"><i class="fa-solid fa-trash"></i>Delete</li>
                </ul>
              </div>
              </li>`;
          }
        });
      }
      taskOutputEl.html(li || `<span>You don't have any task here...</span>`);
    }
  
    function updateStatus(selectedTask) {
      let taskName = $(selectedTask).parent().parent().find(".todo");
      if (selectedTask.checked) {
        taskName.addClass("checked");
        todos[selectedTask.id].status = "completed";
      } else {
        taskName.removeClass("checked");
        todos[selectedTask.id].status = "pending";
      }
      saveTasks();
    }
  
    function showMenu(selectedMenu) {
      let taskMenu = $(selectedMenu).parent().find(".task-menu");
      taskMenu.addClass("show");
      $(document).on("click", function(e) {
        if ($(e.target).prop("tagName") !== "I" || $(e.target)[0] !== selectedMenu) {
          taskMenu.removeClass("show");
        }
      });
    }
  
    function deleteTask(taskId) {
      todos.splice(taskId, 1);
      saveTasks();
      showTodoList("all");
    }
  
    function editTask(taskId, taskName) {
      taskInputEl.val(taskName);
      taskInputEl.focus();
      taskInputEl.data("taskId", taskId);
    }
  
    taskInputEl.on("keyup", function(e) {
      let userTaskInput = taskInputEl.val().trim();
      if (e.key === "Enter" && userTaskInput) {
        if (taskInputEl.data("taskId") === undefined) {
          let taskInfo = {
            name: userTaskInput,
            status: "pending",
          };
          todos.push(taskInfo);
        } else {
          let taskId = taskInputEl.data("taskId");
          todos[taskId].name = userTaskInput;
          taskInputEl.removeData("taskId");
        }
        saveTasks();
        taskInputEl.val("");
        showTodoList("all");
      }
    });
  
    clearEl.on("click", function() {
      todos = [];
      saveTasks();
      showTodoList("all");
    });
  
    fetchTasks();
  });
  