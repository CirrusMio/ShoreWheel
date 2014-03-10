function ChoreWheel(){
  this.chores = [];
  this.people = [];
  this.pairs = [];
};

ChoreWheel.prototype.setPairs = function(){
  this.pairs = [];
  for(var i = 0;i < people.length;i++){
    this.pairs.push([chores[i],people[i]]);
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
};
