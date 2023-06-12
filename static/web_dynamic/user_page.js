$(document).ready(function() {
    // Array to store team members
    var teamMembers = [];

    $(".add-btn").click(function() {
        $("form").toggle();
    });

    $("form").submit(function(event) {
        event.preventDefault(); // Prevent form submission

        // Get input values from the form
        var taskName = $("#task-name").val();
        var taskDescription = $("#task-description").val();
        var teamName = $("#member-name").val();

        // Create a new task element
        var taskElement = $("<div></div>").addClass("task");
        var checkbox = $("<input type='checkbox'>").addClass("task-checkbox");
        var taskTitle = $("<h3></h3>").text(taskName);
        var taskDesc = $("<p></p>").text(taskDescription);
        var deleteBtn = $("<button></button>").text("Delete").addClass("delete-btn");
        var editBtn = $("<button></button>").text("Edit").addClass("edit-btn");
        var teamMember = $("<p></p>").text(teamName).addClass("member");

        // Append checkbox, task title, description, delete button, Team members and edit button to the task element
        taskElement.append(checkbox);
        taskElement.append(taskTitle);
        taskElement.append(taskDesc);
        taskElement.append(deleteBtn);
        taskElement.append(editBtn);
        taskElement.append(teamMember);

        // Append the task element to the task container
        $("#task-container").append(taskElement);


        // Clear the form input fields
        $("#task-name").val("");
        $("#task-description").val("");
        $("member-name").val("");

        // Hide the form
        $("form").hide();
        
        // Store the task data in the database
        storeTaskData(taskName, taskDescription, teamName);

        // Add team member to the session
        var memberName = $("#member-name").val();
        teamMembers.push(memberName);

        // Clear the member input field
        $("#member-name").val("");
    });

    $(document).on("click", ".delete-btn", function() {
        $(this).closest(".task").remove();
        
        // Delete the task from the database
        var taskId = $(this).closest(".task").data("task-id");
        deleteTaskData(taskId);
    });

    $(document).on("click", ".edit-btn", function() {
        var taskElement = $(this).closest(".task");
        var taskTitle = taskElement.find("h3").text();
        var taskDesc = taskElement.find("p").text();

        // Fill the form fields with the task details
        $("#task-name").val(taskTitle);
        $("#task-description").val(taskDesc);

        // Remove the task element from the DOM
        taskElement.remove();

        // Show the form
        $("form").show();
    });
    
    $(document).on("click", ".task-checkbox", function() {
        var taskElement = $(this).closest(".task");
        taskElement.toggleClass("completed");
        
        // Update the task status in the database
        var taskId = taskElement.data("task-id");
        var isCompleted = taskElement.hasClass("completed");
        updateTaskStatus(taskId, isCompleted);
    });

    $("#search-member").on("input", function() {
        var searchQuery = $(this).val();
        var matchingMembers = searchMembers(searchQuery);

        // Display the matching members in the UI
        displayMatchingMembers(matchingMembers);
    });

    // Function to store the task data in the database using AJAX
    function storeTaskData(taskName, taskDescription) {
        $.ajax({
            url: "/store-task",
            method: "POST",
            data: {
                name: taskName,
                description: taskDescription
            },
            success: function(response) {
                console.log("Task data stored successfully!");
                // Assign a unique ID to the task element and store it as a data attribute
                var taskId = response.taskId;
                var taskElement = $("#task-container").find(".task").last();
                taskElement.data("task-id", taskId);
            },
            error: function(xhr, status, error) {
                console.error("Error storing task data:", error);
            }
        });
    }
    
    // Function to delete the task data from the database using AJAX
    function deleteTaskData(taskId) {
        $.ajax({
            url: "/delete-task",
            method: "POST",
            data: {
                id: taskId
            },
            success: function(response) {
                console.log("Task data deleted successfully!");
            },
            error: function(xhr, status, error) {
                console.error("Error deleting task data:", error);
            }
        });
    }
    
    // Function to update the task status in the database using AJAX
    function updateTaskStatus(taskId, isCompleted) {
        $.ajax({
            url: "/edit-task",
            method: "POST",
            data: {
                id: taskId,
                completed: isCompleted
            },
            success: function(response) {
                console.log("Task status updated successfully!");
            },
            error: function(xhr, status, error) {
                console.error("Error updating task status:", error);
            }
        });
    }
    
    
});
