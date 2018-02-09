var searchInput = document.getElementById('searchInput')
var searchResDiv = document.getElementById('searchResDiv')
var currentURL = window.location.href
var advancedSearch = document.getElementById('advancedSearch')


var exist = function (parent, id) {
	for (var i in parent.children) {
		if (parent.children.hasOwnProperty(i)) {
			if(parent.children[i].id==id){
				return parent.children[i]
			}
		}
	}
	return 0
}

var delOthers = function (parent, idArr) {
	for (var i=0; i < parent.children.length; i++) {
		if(idArr.indexOf(parent.children[i].id)<0 && parent.children[i].id && parent.children[i].id!='advancedSearch') {
			parent.children[i].remove()
			i = i-1
		}
	}
}

var populateSearchRes = function (resType, dataArr, allIds){
	for (var i = 0; i < dataArr.length; i++) {
		delOthers(searchResDiv, allIds)
		var resItem = document.getElementsByClassName("dropdown-item")[0].cloneNode(true)
		resItem.id= resType+dataArr[i]['id']
		if (!exist(searchResDiv, resItem.id)){
			resItem.style.display = 'block'
			resItem.href = location.origin+"/library/"+resType+"/"+dataArr[i]['id']+"/"
			resItem.children[0].innerHTML = resType
			if (resType=='book') {
				resItem.children[1].innerHTML = " "+dataArr[i]['title']
			}
			else {
				resItem.children[1].innerHTML = " "+dataArr[i]['full_name']
			}
			searchResDiv.insertBefore(resItem, searchResDiv.firstChild);
		}
	}
}


function ajaxSuccess () {
	var response = JSON.parse(this.responseText)
	console.log(response)
		if (response['req_status']=="ok") {
			searchResDiv.style.display = 'block'
			var books = response['data']['books']
			var authors = response['data']['authors']
			var allIds = response['data']['all_ids']

			if (books.length) {
				populateSearchRes('book', books, allIds)
			}
			if (authors.length) {
				populateSearchRes('author', authors, allIds)
			}
		}
		else {
			delOthers(searchResDiv, [1])
			searchResDiv.style.display = 'none'
			
		}
}

var ajaxReruest = function (input) {
	var oReq = new XMLHttpRequest();
	advancedSearch.href = currentURL + `advanced_search?k=${input}`
	oReq.onload = ajaxSuccess;
	oReq.open("get", currentURL+`search?k=${input}`);
	oReq.send();
}


searchFun = function (e) {
	if(e.target.value){
		ajaxReruest(e.target.value)
	}
	else {
		delOthers(searchResDiv, [1])
		searchResDiv.style.display = 'none'
	}
}

searchInput.addEventListener('input', searchFun)