/**
 * Created by fashust on 19.07.14.
 */

var createUserCtrl = function($scope, $http, $cookies) {
    $scope.create_user = function(user_data) {
        /*
        * crete new user
        * */

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
                if (response.status) {
                    console.log('redirect user to main page');
                    $scope.user_data = {};
                    build_page(response.data);
                } else {
                    validate_form(form_name, form_fields, fields_valid, response.errors);
                }
            }).error(function(data, status, xhr) {
                console.log(data, status, xhr);
            });
        }
    };
};