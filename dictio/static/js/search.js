$(function() {
  $("#search-input").autocomplete({
    source: "/autocomplete/",
    minLength: 1,
    autoFocus: true,
    delay: 500,
    search: function() {
      // disable caching of AJAX responses
      $.ajaxSettings.cache = false;
    },
    open: function() {
      $(this).removeClass("ui-corner-all").addClass("ui-corner-top");
      $(".ui-autocomplete").addClass("rounded");
    },
    close: function() {
      $(this).removeClass("ui-corner-top").addClass("ui-corner-all");
    }
  }).autocomplete("instance")._renderItem = function(ul, item) {
    return $("<li>")
      .append("<div>" + item.label + "</div>")
      .appendTo(ul);
  };
});
