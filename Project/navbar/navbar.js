document.querySelector("#navbar").innerHTML = `
<div class="navbarHead">

<div class="logo">
<img class="imp" src="" alt="Your photo">
    <div class="logo-name">
        Portfolio
    </div>
</div>
<div class="social">
    <a href="" style="text-decoration: none"> <div>
    <i class="fa fa-instagram" aria-hidden="true"></i>
    </div> </a>
   <a href="" style="text-decoration: none"> <div>
   <i class="fa fa-facebook-square" aria-hidden="true"></i>
   </div> </a>
   <a href="" style="text-decoration: none"> <div>
   <i class="fa fa-twitter" aria-hidden="true"></i>
   </div> </a>
</div>
</div>
`;

const button = document.getElementById("myButton");
myButton.addEventListener("click", () => {
  document.body.classList.toggle("dark-Mode");
});
