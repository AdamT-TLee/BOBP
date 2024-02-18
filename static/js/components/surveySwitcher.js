const surveySwitcher = () => {
    const form1 = document.querySelector("#form1");
    const sec1 = document.querySelector(".sec1");
    const sec2 = document.querySelector(".sec2");
  
    form1.addEventListener("submit", () => {
      event.preventDefault();
      sec1.remove();
      sec2.style.display = "inline";
      sec2.style.opacity = 1;
    });
  };
  
  export default surveySwitcher;