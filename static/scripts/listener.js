var squares = document.getElementsByClassName("square")
var elems = []

for(var i = 0; i < squares.length; i++) {
   elems.push((squares.item(i)));
}

var selected = null
elems.forEach(function(elem) {
    elem.addEventListener("click", function() {
        //this function does stuff
        console.log("elem: " + elem)
        console.log("id: " + elem.id)
        console.log("inner html: " + elem.innerHTML.trim())
        console.log("selected: " + selected)
        var id = elem.id

        console.log("id: " + id)
        var num_row = parseInt(id / 5)
        var num_col = id % 5

        console.log("row: " + num_row)
        console.log("col: " + num_col)
    });
});