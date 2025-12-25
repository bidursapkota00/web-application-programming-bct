// Local Storage Functions
function getLocalStorage() {
  var list = localStorage.getItem("grocery-list");
  if (list) {
    return JSON.parse(list);
  }
  return [];
}

function setLocalStorage(itemsArray) {
  localStorage.setItem("grocery-list", JSON.stringify(itemsArray));
}

// Initialize items from local storage
var items = getLocalStorage();
var editId = null;

// Render App
function render() {
  var $app = $("#app");
  $app.empty();

  var itemToEdit = editId
    ? $.grep(items, function (item) {
        return item.id === editId;
      })[0]
    : null;
  var $formElement = createForm(editId, itemToEdit); // edited line
  var $itemsElement = createItems(items);

  $app.append($formElement);
  $app.append($itemsElement);
}

// Initialize App
$(document).ready(function () {
  render();
});

// Update Item Name Function
function updateItemName(newName) {
  items = $.map(items, function (item) {
    if (item.id === editId) {
      return $.extend({}, item, { name: newName });
    }
    return item;
  });
  editId = null;
  setLocalStorage(items);
  render();
  setTimeout(function () {
    alert("Item Updated Successfully!");
  }, 0);
}

// Set Edit ID Function
function setEditId(itemId) {
  editId = itemId;
  render();

  // Focus input after render
  setTimeout(function () {
    $(".form-input").focus();
  }, 0);
}

function editCompleted(itemId) {
  items = $.map(items, function (item) {
    if (item.id === itemId) {
      return $.extend({}, item, { completed: !item.completed });
    }
    return item;
  });
  setLocalStorage(items);
  render();
}

function removeItem(itemId) {
  items = $.grep(items, function (item) {
    return item.id !== itemId;
  });
  setLocalStorage(items);
  render();
  setTimeout(function () {
    alert("Item Deleted Successfully!");
  }, 0);
}

// Generate unique ID
function generateId() {
  return Date.now().toString(36) + Math.random().toString(36).substr(2);
}

// Add Item Function
function addItem(itemName) {
  var newItem = {
    name: itemName,
    completed: false,
    id: generateId(),
  };
  items.push(newItem);
  setLocalStorage(items);
  render();
  setTimeout(function () {
    alert("Item Added Successfully!");
  }, 0);
}
