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

  document.getElementById("myrating").textContent="My rating ("+i+"/5)"

  while(i>0)
  {
    document.getElementById("star"+i).className="fa fa-star checked";
    i--
  }
}
        
