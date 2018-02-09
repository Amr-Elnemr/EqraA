var selectResType = document.getElementById('select-res-type')
// var booksResDiv = document.getElementById('books-res-div')
// var authorsResDiv = document.getElementById('authors-res-div')

var hideDiv =  function (e){
	for (var i = 0; i < selectResType.children.length; i++) {
		resDiv = selectResType.children[i].children[0]
		if(resDiv.checked){
			document.getElementById(resDiv.id+"-div").style.display = "block"
		}
		else {
			document.getElementById(resDiv.id+"-div").style.display = "none"
			
		}
	}
	// tagetDiv = document.getElementById(e.target.id)
	// document.getElementById(e.target.id).style.display = 'none'
}

selectResType.addEventListener('click', hideDiv)