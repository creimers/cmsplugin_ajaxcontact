$(document).ready(function(){
  $('.form-group').removeClass('has-feedback');
  $('.form-group').removeClass('has-error');

  var handleResponse = function(data){

    // success
    if (data.object) {
      $('.contacts-plugin').hide(); 
      $('#success').show();
    }
    // error handling
    else {
      Recaptcha.reload();
      $('.form-group').addClass('has-feedback');
      $.each(data, function(key, value){
        if (key=== 'captcha') {
          console.log('wrong captcha'); 
        }
        else{
         $('#id_' + key).parent().addClass('has-error');
        }
      });
    }
  };

  var submitContact = function(form){
    $.ajax({
      type: 'POST',
      url: form.attr('action'),
      data: form.serialize()
    }).always(handleResponse);
  };
  
  $('.contacts-plugin input[type=submit]').on('click', function(evt){
    console.log('click');
    evt.preventDefault();
    var $form = $(this).parents('form').eq(0);
    submitContact($form);
  });

});
