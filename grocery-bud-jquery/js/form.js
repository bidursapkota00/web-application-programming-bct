function createForm(editId, itemToEdit) {
  var $form = $("<form></form>");

  // added value and dynamic button name
  $form.html(`
    <h2>grocery bud</h2>
    <div class="form-control">
      <input
        type="text"
        class="form-input"
        placeholder="e.g. eggs"
        value="${itemToEdit ? itemToEdit.name : ""}"
      />
      <button type="submit" class="btn">
        ${editId ? "edit item" : "add item"}
      </button>
    </div>
  `);

  $form.on("submit", function (e) {
    e.preventDefault();
    var $input = $form.find(".form-input");
    var value = $.trim($input.val());

    if (!value) {
      alert("Please provide value");
      return;
    }

    // added conditions
    if (editId) {
      updateItemName(value);
    } else {
      addItem(value);
    }

    $input.val("");
  });

  return $form;
}
