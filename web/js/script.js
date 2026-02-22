// Простая реализация появления элементов при скролле (без библиотек)
document.addEventListener("DOMContentLoaded", () => {
  const elements = document.querySelectorAll("[data-aos]");

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("aos-animate");
      }
    });
  }, { threshold: 0.1 });

  elements.forEach(el => {
    observer.observe(el);
  });
});
