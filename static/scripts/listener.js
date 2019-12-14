var pieces = []
var empty_spaces = []
for(var i = 0; i < 25; i++) {
	elem = document.getElementById(i)
	if(elem.className.includes("square")) {
	   pieces.push(elem);
	} else {
		empty_spaces.push(elem)
	}
}
var selected = null

pieces.forEach(function(elem) {
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

        var og = window.location.href
        window.location.href += "get_valid_moves/" + id
        selected = id
    });
});

empty_spaces.forEach(function(elem) {
	elem.addEventListener("click", function() {
		var id = elem.id
		window.location.href += "move_selected_to/" + id
	});
});