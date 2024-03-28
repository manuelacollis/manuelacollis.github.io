---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
redirect_from:
  - /research
---
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
#more {display: none;}
</style>
</head>
<body>

# Publications

### [Whether to Apply](http://manuelacollis.github.io/files/2023_02_Whether_to_Apply.pdf) <i> Management Science, 2023 </i> <br>
with [Katherine Baldiga Coffman](https://sites.google.com/site/kbaldigacoffman/) and Leena Kulkarni <br>
<p><b><i>Abstract:</i></b> Labor market outcomes depend, in part, upon an individual’s willingness to put herself forward for different opportunities. We use a series of experiments to explore gender differences in willingness to apply for higher return, more challenging work. We find that,<span id="dots">...</span><span id="more">in male-typed domains, qualified women are significantly less likely to apply than similarly well-qualified men. We provide evidence both in a controlled setting and in the field that reducing ambiguity surrounding required qualifications increases the rate at which qualified women apply. The effects are more mixed for men. Our results suggest a path for increasing the pool of qualified women applicants.</span></p>
<button onclick="myFunction()" id="myBtn">Read more</button>

### [Stereotypes and Belief Updating](http://manuelacollis.github.io/files/2021_01_Stereotypes_and_Belief_Updating.pdf) <i> accepted at Journal of European Economic Association, 2023 </i> <br>
with [Katherine Baldiga Coffman](https://sites.google.com/site/kbaldigacoffman/) and Leena Kulkarni <br>
<b><i>Abstract:</i></b> We explore how feedback shapes, and perpetuates, gender gaps in self-assessments. Participants 
in our experiments take tests of their ability across different domains. Absent feedback, beliefs of own 
ability are strongly influenced by gender stereotypes: holding own ability fixed, individuals are more 
confident in more gender congruent domains (i.e. more male-typed for men, more female-typed for 
women). After feedback, stereotypes continue to shape posterior beliefs, even beyond what a Bayesian 
model would predict. This is primarily because both men and women update their beliefs more positively 
in response to good news when it arrives in a more gender congruent domain

<h2>Read More Read Less Button</h2>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus imperdiet, nulla et dictum interdum, nisi lorem egestas vitae scel<span id="dots_2">...</span><span id="more_2">erisque enim ligula venenatis dolor. Maecenas nisl est, ultrices nec congue eget, auctor vitae massa. Fusce luctus vestibulum augue ut aliquet. Nunc sagittis dictum nisi, sed ullamcorper ipsum dignissim ac. In at libero sed nunc venenatis imperdiet sed ornare turpis. Donec vitae dui eget tellus gravida venenatis. Integer fringilla congue eros non fermentum. Sed dapibus pulvinar nibh tempor porta.</span></p>
<button onclick="myFunction_2()" id="myBtn_2">Read more</button>

<script>
function myFunction() {
  var dots = document.getElementById("dots");
  var moreText = document.getElementById("more");
  var btnText = document.getElementById("myBtn");

  if (dots.style.display === "none") {
    dots.style.display = "inline";
    btnText.innerHTML = "Read more"; 
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    btnText.innerHTML = "Read less"; 
    moreText.style.display = "inline";
  }
}
</script>

<script>
function myFunction_2() {
  var dots = document.getElementById("dots_2");
  var moreText = document.getElementById("more_2");
  var btnText = document.getElementById("myBtn_2");

  if (dots.style.display === "none") {
    dots.style.display = "inline";
    btnText.innerHTML = "Read more"; 
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    btnText.innerHTML = "Read less"; 
    moreText.style.display = "inline";
  }
}
</script>

</body>
</html>
