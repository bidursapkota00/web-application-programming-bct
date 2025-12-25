// Create SingleItem Element
function createSingleItem(item) {
  var $div = $('<div class="single-item"></div>');

  $div.html(`
    <input type="checkbox" ${item.completed ? "checked" : ""} />
    <p style="text-decoration: ${item.completed ? "line-through" : "none"}">
      ${item.name}
    </p>
    <button class="btn icon-btn edit-btn" type="button">
      <i class="fa-regular fa-pen-to-square"></i>
    </button>
    <button class="btn icon-btn remove-btn" type="button">
      <i class="fa-regular fa-trash-can"></i>
    </button>
  `);

  $div.find('input[type="checkbox"]').on("change", function () {
    editCompleted(item.id);
  });

  $div.find(".remove-btn").on("click", function () {
    removeItem(item.id);
  });

  $div.find(".edit-btn").on("click", function () {
    setEditId(item.id);
  });

  return $div;
}
