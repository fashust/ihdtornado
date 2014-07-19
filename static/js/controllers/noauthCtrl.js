/**
 * Created by fashust on 18.07.14.
 * not authenticated user controller
 */

var noauthCtrl = function($scope, $http, $cookies) {
    $scope.auth_popup = false;
    $scope.registration_popup = false;

    $scope.show_auth = function() {
        /*
        * show authentication popup
        * */
        if (!$scope.auth_popup) {
            $scope.auth_popup = true;
            $('#popupAuth').addClass('show');
        }
    };

    $scope.show_registration = function() {
        /*
        * show registration popup
        * */
        if (!$scope.registration_popup) {
            $scope.registration_popup = true;
            $('#popupRegister').addClass('show');
        }
    };

    $scope.close = function(popup) {
        /*
        * close popups
        * */
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
};