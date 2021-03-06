var pieces = []
var empty_spaces = []
for(var i = 0; i < 25; i++) {
	elem = document.getElementById(i)
	if(elem.className.includes("can_move_to")) {
	   empty_spaces.push(elem)
	} else if (elem.className.includes("square")) {
		pieces.push(elem)
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

var placeable = []
var all_dead = document.getElementsByClassName("square dead")
console.log(all_dead)
for (let elem of all_dead) {
	console.log(elem)
	elem.addEventListener("click", function() {
		var change = "place_piece/" + elem.id
		window.location.href += change
	});
}

var play_again = document.getElementById("play_again")
if (play_again != null) {
	play_again.addEventListener("click", function() {
		window.location.href += "reset"
	});
}

var promotion_options_holder = document.getElementById("promotion-options")
if (promotion_options_holder != null) {
	var promotion_options = promotion_options_holder.getElementsByTagName("div")
	for (let elem of promotion_options) {
		elem.addEventListener("click", function() {
			window.location.href += "promote_to/" + elem.id
		});
	}
}