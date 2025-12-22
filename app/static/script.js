console.log("conectado");

const addTaskBtn = document.getElementById("add-task-btn");
const logoutBtn = document.getElementById("logout-btn");

const modal = document.getElementById("task-modal");
const modalTitle = document.getElementById("modal-title");
const taskForm = document.getElementById("task-form");
const taskInput = document.getElementById("task-input");
const cancelBtn = document.getElementById("cancel-btn");

const taskList = document.getElementById("task-list");
const defaultLi = document.getElementById("default-li");

let editTask = null;

/** modal */

function openModal(title = "Nova Tarefa", value = "") {
  if (!modal || !modalTitle || !taskInput) return;

  modalTitle.textContent = title;
  taskInput.value = value;
  modal.classList.add("open");
  taskInput.focus();
}

function closeModal() {
  if (!modal || !taskInput) return;

  modal.classList.remove("open");
  taskInput.value = "";
  editTask = null;
}

/** listener */

function taskListener() {
  if (addTaskBtn) {
    addTaskBtn.addEventListener("click", () => openModal());
  }

  if (cancelBtn) {
    cancelBtn.addEventListener("click", closeModal);
  }
}

function taskCreator() {
  if (!taskForm || !taskInput) return;

  taskForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const title = taskInput.value.trim();
    if (!title) return;

    try {
      if (editTask) {
        await updateTask(title);
      } else {
        await createTask(title);
      }
      closeModal();
    } catch (err) {
      console.error("Erro ao salvar tarefa:", err);
    }
  });
}

/** API */

async function createTask(title) {
  const response = await fetch("/api/tasks", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title })
  });

  if (!response.ok) throw new Error("Erro ao criar tarefa");

  const task = await response.json();
  addTaskToDOM(task);
}

async function updateTask(title) {
  if (!editTask) return;

  const response = await fetch(`/api/tasks/${editTask.id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title })
  });

  if (!response.ok) throw new Error("Erro ao editar tarefa");

  editTask.textEl.textContent = title;
}

if (taskList) {
  taskList.addEventListener("click", async (e) => {
    const li = e.target.closest("li");
    if (!li) return;

    // EDITAR
    if (e.target.classList.contains("edit")) {
      const textEl = li.querySelector(".task-text");
      const checkbox = li.querySelector("input[type='checkbox']");
      if (!textEl || !checkbox) return;

      editTask = {
        id: checkbox.dataset.id,
        textEl
      };

      openModal("Editar Tarefa", textEl.textContent);
    }

    // REMOVER
    if (e.target.classList.contains("delete")) {
      const checkbox = li.querySelector("input[type='checkbox']");
      if (!checkbox) return;

      const taskId = checkbox.dataset.id;
      if (!confirm("Tem certeza que deseja remover esta tarefa?")) return;

      try {
        const response = await fetch(`/api/tasks/${taskId}`, {
          method: "DELETE"
        });

        const data = await response.json();

        if (data.success) {
          li.remove();
          checkEmptyList();
        }
      } catch (err) {
        console.error("Erro ao remover tarefa:", err);
      }
    }
  });

  // CHECKBOX
  taskList.addEventListener("change", async (e) => {
    if (e.target.type !== "checkbox") return;

    const checkbox = e.target;
    const li = checkbox.closest("li");
    const textEl = li?.querySelector(".task-text");
    if (!textEl) return;

    const taskId = checkbox.dataset.id;
    textEl.classList.toggle("completed", checkbox.checked);

    try {
      await fetch(`/tasks/${taskId}/toggle`, {
        method: "POST",
      });
    } catch (err) {
      console.error("Erro ao atualizar status da tarefa:", err);
    }
  });
}

/** dom updates */
function addTaskToDOM(task) {
  if (!taskList || !defaultLi) return;

  const li = document.createElement("li");

  const left = document.createElement("div");
  left.className = "task-left";

  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";
  checkbox.dataset.id = task.id;
  checkbox.checked = task.done;

  const span = document.createElement("span");
  span.className = `task-text ${task.done ? "completed" : ""}`;
  span.textContent = task.title;

  left.appendChild(checkbox);
  left.appendChild(span);

  const actions = document.createElement("div");
  actions.className = "task-actions";

  const editBtn = document.createElement("button");
  editBtn.className = "edit";
  editBtn.textContent = "Editar";

  const deleteBtn = document.createElement("button");
  deleteBtn.className = "delete";
  deleteBtn.textContent = "Remover";

  actions.appendChild(editBtn);
  actions.appendChild(deleteBtn);

  li.appendChild(left);
  li.appendChild(actions);

  taskList.appendChild(li);
  defaultLi.style.display = "none";
}

function checkEmptyList() {
  if (!taskList || !defaultLi) return;

  if (taskList.querySelectorAll("li").length === 1) {
    defaultLi.style.display = "block";
  }
}

if (logoutBtn) {
  logoutBtn.addEventListener("click", () => {
    window.location.href = "/logout";
  });
}

/** check if dom elements needed exist */
document.addEventListener("DOMContentLoaded", () => {
  taskListener();
  taskCreator();
});
