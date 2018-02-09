
document.getElementById("star1").addEventListener("click", function(){rate(1)})
document.getElementById("star2").addEventListener("click", function(){rate(2)})
document.getElementById("star3").addEventListener("click", function(){rate(3)})
document.getElementById("star4").addEventListener("click", function(){rate(4)})
document.getElementById("star5").addEventListener("click", function(){rate(5)})

function rate(i)
{
  for(j=1; j<=5; j++)
  {
    document.getElementById("star"+j).className="fa fa-star";
  }


  while(i>0)
  {
    document.getElementById("star"+i).className="fa fa-star checked";
    i--
  }
}
var myRatingDiv = document.getElementById('myrating-div')
var statusDiv = document.getElementById('status')

function ajaxSuccess () {
  var response = JSON.parse(this.responseText)
  console.log(response)
}

var ajaxReruest = function (rate, status) {
  var oReq = new XMLHttpRequest()
  var currentURL = window.location.href
  oReq.onload = ajaxSuccess
  oReq.open("get", currentURL+`edit?rate=${rate}&status=${status}`)
  oReq.send();
}

myRatingDiv.addEventListener("click", function (e) {
  console.log('aaaaa')
    starNum = e.target.id.substring(4)
    if(e.target.id.substring(0, 4)=='star'){
      ajaxReruest(starNum, 0)
    }

})

statusDiv.addEventListener('change', function (e) {
  ajaxReruest(0, this.value)
})
   