/**
 * Created by fashust on 19.07.14.
 */

var authUserCtrl = function($scope, $http, $cookies) {

    $scope.auth_user = function(user_data) {
        /*
        * authenticate user
        * */

        var form_fields = _.filter(
                _.keys($scope.authUser),
                function(item) {
                    return item.indexOf('$') == -1
                }
            ),
            fields_valid = _.map(
                form_fields,
                function(item) {
                    return $scope.authUser[item].$valid
                }
            ),
            form_name = $scope.authUser.$name;

        validate_form(form_name, form_fields, fields_valid);
        if ($scope.authUser.$valid) {
            user_data._xsrf = $cookies._xsrf;
            $http({
                method: 'POST',
                url: '/users/auth/',
                data: $.param(user_data),
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    '_xsrf': $cookies._xsrf,
                    'X-Requested-With': 'XMLHttpRequest'
                }
            }).success(function(response) {
                if (response.status) {
                    console.log('redirect user to main page');
                    build_page(response.data);
                } else {
                    validate_form(form_name, form_fields, fields_valid, response.errors);
                }
            }).error(function(data, status, xhr) {
                console.log('error', data, status, xhr);
            });
        }
    }
};