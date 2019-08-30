const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function() {
  $('.alert-message').fadeOut('slow');
}, 2000);
