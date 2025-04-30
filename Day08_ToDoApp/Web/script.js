function addTask() {
  const input = document.getElementById("taskInput");
  const taskText = input.value.trim();
  if (taskText === "") return;

  const li = document.createElement("li");
  li.textContent = taskText;

  li.addEventListener("click", function () {
    this.classList.toggle("completed");
  });

  li.addEventListener("dblclick", function () {
    this.remove();
  });

  document.getElementById("taskList").appendChild(li);
  input.value = "";
}
