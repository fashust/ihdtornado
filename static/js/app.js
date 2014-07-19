/*
 * application
 * */

var ihd = angular.module('ihd', ['ngCookies']);

ihd.controller('noauth', ['$scope', '$http', '$cookies', noauthCtrl]);
ihd.controller('createUserCtrl', ['$scope', '$http', '$cookies', createUserCtrl]);
ihd.controller('authUserCtrl', ['$scope', '$http', '$cookies', authUserCtrl]);

ihd.controller('user', function($scope) {
    console.log('userctrl');
});