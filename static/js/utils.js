/**
 * Created by fashust on 19.07.14.
 */

var error_messages = {
    'username:createUser': "Обязательное поле",
    'email:createUser': "Обязательное поле",
    'password:createUser': "Обязательное поле",
    'password_confirm:createUser': "Обязательное поле",
    'password:authUser': "Обязательное поле",
    'email:authUser': "Обязательное поле"
},
    side_selector = '#side',
    content_selector = '#content';

function validate_form(form_name, form_fields, fields_valid, messages) {
    /*
     * validate forms
     * */

    if (messages == undefined) {
        _.each(
            _.zip(form_fields, fields_valid),
            function(item) {
                var error_holder = $('form[name=' + form_name + '] input[name=' + item[0] + ']').next('.errorMsg');

                if (!item[1]) {
                    error_holder.show();
                    error_holder.text(
                        error_messages[[item[0], form_name].join(':')]
                    );
                } else {
                    error_holder.hide();
                }
            }
        );
    } else {
        _.each(_.zip(_.values(messages), _.keys(messages)), function(item) {
            var message = item[0][0],
                field = item[1],
                error_holder = $('form[name=' + form_name + '] input[name=' + field + ']').next('.errorMsg');

            error_holder.show();
            error_holder.text(message);
        });
    }
}

function build_page(user_data) {
    /*
     * build page after user singin(up)
     * */

    $('body').removeClass('main');
    $('body').removeAttr('ng-controller');
    $(side_selector).remove();
    $(content_selector).before(user_data.menu);
    $(content_selector).remove();
    $(side_selector).after(user_data.data);
//    create_initial_address();
}