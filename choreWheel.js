function ChoreWheel(){
  this.chores = ['Dishes', 'Garbage', 'Recycling', 'Stuff'];
  this.people = ['Mike', 'Will', 'Tanzi', 'Sarah', 'Nick',
                 'Steev', 'Chase Original', 'Nu-Chase', 'Todd'];
  this.pairs = [];
  this.begin = new Date(2014,2,25,13,15,00);
  this.setPairs();
  this.setup();
};

ChoreWheel.prototype.setPairs = function(){
  this.pairs = [];
  for(var i = 0;i < this.people.length;i++){
    if(i >= this.chores.length){
     this.pairs.push(['Free', this.people[i]]);
    }
    else{
      this.pairs.push([this.chores[i], this.people[i]]);
    }
  }
};

ChoreWheel.prototype.getPairs = function(){
  return this.pairs;
};

ChoreWheel.prototype.addPerson = function(name){
  this.people.push(name);
};

ChoreWheel.prototype.addChore = function(name){
  this.chores.push(name);
};

ChoreWheel.prototype.rotateWheel = function(){
  this.people.push(this.people.shift());
  this.setPairs();
  console.log(this.begin);
};

ChoreWheel.prototype.setup = function(){
  var today = new Date();
  var spins = new Date(today-this.begin);
  spins = spins%(this.people.length);

  for(var i = 0;i < spins;i++){
    this.rotateWheel();
  }
};


var wheel = new ChoreWheel();


var choreWheelApp = angular.module('choreWheelApp', []);

choreWheelApp.controller('choreWheelCtrl', function($scope)
                                           {$scope.wheel = wheel});

