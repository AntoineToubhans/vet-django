var menu_state = false;
var toggle_menu = function() {};

jQuery(document).ready(function($){
  toggle_menu = function() {
    menu_state = !menu_state;
  
    if (menu_state) {
      $('.menu-button svg').replaceWith('<i class="fas fa-angle-right"></i>');
      $('.home-left-menu.menu')
      .removeClass('menu-opened')
      .addClass('menu-closed');
    } else {
      $('.menu-button svg').replaceWith('<i class="fas fa-angle-left"></i>');
      $('.home-left-menu.menu')
        .removeClass('menu-closed')
        .addClass('menu-opened');
    }
  }
});

