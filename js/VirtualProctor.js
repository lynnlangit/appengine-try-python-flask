angular.module('VirtualProctor',[]);
angular.module('VirtualProctor').controller('Screenshots',function($scope,$http,$interval){

    $scope.className = "All Classes";
    $scope.selectClass = function(classname){
        $scope.className = classname;
    }
    function loadData(){
        $http.get('/screenshots').success(function(data){
         $scope.screenshots = data;
     });
    }
    loadData();
    $interval(loadData,10000);
});


//filter from https://github.com/angular-ui/angular-ui-OLDREPO/blob/master/modules/filters/unique/unique.js
angular.module('VirtualProctor').filter('unique',function(){
    return function (items, filterOn) {

    if (filterOn === false) {
      return items;
    }

    if ((filterOn || angular.isUndefined(filterOn)) && angular.isArray(items)) {
      var hashCheck = {}, newItems = [];

      var extractValueToCompare = function (item) {
        if (angular.isObject(item) && angular.isString(filterOn)) {
          return item[filterOn];
        } else {
          return item;
        }
      };

      angular.forEach(items, function (item) {
        var valueToCheck, isDuplicate = false;

        for (var i = 0; i < newItems.length; i++) {
          if (angular.equals(extractValueToCompare(newItems[i]), extractValueToCompare(item))) {
            isDuplicate = true;
            break;
          }
        }
        if (!isDuplicate) {
          newItems.push(item);
        }

      });
      items = newItems;
    }
    return items;
  };
});
angular.module('VirtualProctor').filter('byClass',function(){
    return function(items, className){
        if (className === "All Classes"){
            return items;
        }
        return items.filter(function(value){
            return value.classroom === className;
        })
    }
});
angular.module('VirtualProctor').filter('escape', function() {
  return window.encodeURIComponent;
});