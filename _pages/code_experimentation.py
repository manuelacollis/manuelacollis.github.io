< body >
< button
onclick = "window.location.href='https://www.socialscienceregistry.org/trials/11438';" >
AEA
RCT
Registry
< / button >
< / body >





< !DOCTYPE
html >
< html >
< head >
< meta
name = "viewport"
content = "width=device-width, initial-scale=1" >
< style >
.tooltip
{
    position: relative;
display: inline - block;
}

.tooltip.tooltiptext
{
    visibility: hidden;
width: 140
px;
background - color:  # 555;
color:  # fff;
text - align: center;
border - radius: 6
px;
padding: 5
px;
position: absolute;
z - index: 1;
bottom: 150 %;
left: 50 %;
margin - left: -75
px;
opacity: 0;
transition: opacity
0.3
s;
}

.tooltip.tooltiptext::after
{
    content: "";
position: absolute;
top: 100 %;
left: 50 %;
margin - left: -5
px;
border - width: 5
px;
border - style: solid;
border - color:  # 555 transparent transparent transparent;
}

.tooltip: hover.tooltiptext
{
    visibility: visible;
opacity: 1;
}
< / style >
< / head >
< body >

< div


class ="tooltip" >

< button
onclick = "myFunction()"
onmouseout = "outFunc()" >
< span


class ="tooltiptext" id="myTooltip" > Copy to clipboard < /span >


BibTeX
< / button >
< / div >

< script >
function
myFunction()
{
    value1 = "@article{coffman2023apply, title={Whether to Apply}, author={Coffman, Katherine B. and Collis, Manuela R. and Kulkarni, Leena}, journal=Management Science}, year={Forthcoming} }"
citation = "Coffman, Collis, and Kulkarni 2023"

navigator.clipboard.writeText(value1);
var
tooltip = document.getElementById("myTooltip");
tooltip.innerHTML = "Copied: BibTeX data for" + citation;
}

function
outFunc()
{
    var
tooltip = document.getElementById("myTooltip");
tooltip.innerHTML = "Copy to clipboard";
}
< / script >
< / body >
< / html >
