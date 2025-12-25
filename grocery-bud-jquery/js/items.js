// Create Items Container
function createItems(itemsArray) {
  var $container = $('<div class="items"></div>');

  $.each(itemsArray, function (index, item) {
    var $itemElement = createSingleItem(item);
    $container.append($itemElement);
  });

  return $container;
}
