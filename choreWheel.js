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
  var str = '';
  var start = document.getElementById("WHEEL");
  while(start.firstChild){
    start.removeChild(start.firstChild);
  }
  for(var i = 0;i < this.pairs.length;i++){
    str = this.pairs[i][0] + " " + this.pairs[i][1];
    var pair = document.createTextNode(str);
    var para = document.createElement("p");
    para.appendChild(pair);
    start.appendChild(para);
  }
};

var wheel =new ChoreWheel();
wheel.setPairs();
