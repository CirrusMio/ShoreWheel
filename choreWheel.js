function ChoreWheel(){
  this.chores = ['Dishes','Garbage','Recycling','Stuff'];
  this.people = ['Mike', 'Will', 'Tanzi', 'Sarah', 'Nick', 
                 'Steev', 'Chase Original', 'Nu-Chase', 'Todd'];
  this.pairs = [];
};

ChoreWheel.prototype.setPairs = function(){
  this.pairs = [];
  for(var i = 0;i < this.people.length;i++){
    this.pairs.push([this.chores[i],this.people[i]]);
  }
};

ChoreWheel.prototype.getPairs = function(){
  return this.pairs;
}

ChoreWheel.prototype.addPerson = function(name){
  this.people.push(name);
};

ChoreWheel.prototype.addChore = function(name){
  this.chores.push(name);
};

ChoreWheel.prototype.rotateWheel = function(){
  this.people.push(this.people.shift());
  this.setPairs();
};

var wheel =new ChoreWheel();
wheel.setPairs();

var choreWheelApp = angular.module('choreWheelApp',[]);

choreWheelApp.controller('choreWheelCtrl',function($scope){$scope.wheel = wheel});

