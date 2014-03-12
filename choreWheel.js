function ChoreWheel(){
  this.chores = ['Dishes','Garbage','Recycling','Stuff'];
  this.people = ['Mike','Will','Tanzi','Sarah'];
  this.pairs = [];
  // This variable remembers the children that need to be removed
  this.children = [];
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
  var str = '';
  for(var i = 0;i < this.children.length;i++){
    document.getElementById("WHEEL").removeChild(this.children[i]);
  }
  for(var i = 0;i < this.pairs.length;i++){
    str = this.pairs[i][0] + " " + this.pairs[i][1];
    var pair = document.createTextNode(str);
    var para = document.createElement("p");
    para.appendChild(pair);
    this.children.push(para);
    document.getElementById("WHEEL").appendChild(para);
  }
};

var wheel =new ChoreWheel();
wheel.setPairs();
