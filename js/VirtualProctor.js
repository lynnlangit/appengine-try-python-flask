/**
 * Created by lynnlangit on 5/18/15.
 */
angular.module('VirtualProctor',[]);
angular.module('VirtualProctor').controller('Screenshots',function($scope,$http){
     $http.get('/screenshots').success(function(data){
         $scope.screenshots = data;
         console.log(JSON.stringify($scope.screenshots));
     })
});
