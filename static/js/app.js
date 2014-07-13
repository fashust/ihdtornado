/*
* application
* */

var error_messages = {
    'username:createUser': "Обязательное поле",
    'email:createUser': "Обязательное поле",
    'password:createUser': "Обязательное поле",
    'password_confirm:createUser': "Обязательное поле"
};

var serialize = function(obj, prefix) {
  var str = [];
  for(var p in obj) {
    var k = prefix ? prefix + "[" + p + "]" : p, v = obj[p];
    str.push(typeof v == "object" ?
      serialize(v, k) :
      encodeURIComponent(k) + "=" + encodeURIComponent(v));
  }
  return str.join("&");
};

function validate_form(form_name, form_fields, fields_valid) {
    /*
    * validate forms
    * */

    _.each(
        _.zip(form_fields, fields_valid),
        function(item) {
            var error_holder = $('form[name=' + form_name + '] input[name=' + item[0] + ']').next('.errorMsg');

            if (!item[1]) {
                error_holder.show();
                error_holder.text(error_messages[[item[0], form_name].join(':')]);
            } else {
                error_holder.hide();
            }
        }
    );
}


var ihd = angular.module('ihd', ['ngCookies']);

ihd.controller('noauth', ['$scope', '$http', '$cookies', function($scope, $http, $cookies) {
    $scope.auth_popup = false;
    $scope.registration_popup = false;

    $scope.show_auth = function() {
        if (!$scope.auth_popup) {
            $scope.auth_popup = true;
            $('#popupAuth').addClass('show');
        }
    };

    $scope.show_registration = function() {
        if (!$scope.registration_popup) {
            $scope.registration_popup = true;
            $('#popupRegister').addClass('show');
        }
    };

    $scope.close = function(popup) {
        switch (popup) {
            case 'popupAuth':
                $scope.auth_popup = false;
                break;
            case 'popupRegister':
                $scope.registration_popup = false;
                break;
        }
        $('#'+popup).removeClass('show');
    };

    $scope.create_user = function(user_data) {
        var form_fields = _.filter(
            _.keys($scope.createUser),
            function(item) {
                return item.indexOf('$') == -1
            }
        ),
            fields_valid = _.map(
                form_fields,
                function(item) {
                    return $scope.createUser[item].$valid
                }
            ),
            form_name = $scope.createUser.$name;

        validate_form(form_name, form_fields, fields_valid);
        if ($scope.createUser.$valid) {
            console.log(user_data);
            user_data._xsrf = $cookies._xsrf;
            $http({
                method: 'POST',
                url: '/users/create/',
                data: $.param(user_data),
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    '_xsrf': $cookies._xsrf,
                    'X-Requested-With': 'XMLHttpRequest'
                }
            }).success(function(response) {
                console.log(response)
            }).error(function(data, status, xhr) {
                console.log(data, status, xhr);
            });
        }
    };
}]);

ihd.controller('user', function($scope) {
    console.log('userctrl');
});