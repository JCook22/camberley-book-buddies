// All JS code is taken from Materialze CSS.
// wait for DOM content to be loaded
document.addEventListener('DOMContentLoaded', function() {
  // initalize side navigation on small devices
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);
  });
  // initliaze select element in review form
  let selects = document.querySelectorAll('select');
  M.FormSelect.init(selects);
  // initialize collapsibles used in reviews page
  let collapsibles = document.querySelectorAll('.collapsible');
  M.Collapsible.init(collapsibles);