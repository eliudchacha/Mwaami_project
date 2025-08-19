import React, { useEffect, useState } from "react";
import "./SlideShow.css";
import axios from "axios";

const SlideShow = () => {
  const [slides, setSlides] = useState([]);
  const [current, setCurrent] = useState(0);

  useEffect(() => {
    axios
      .get("https://mwaami-project.onrender.com/api/api/slides")
      .then((res) => setSlides(res.data))
      .catch((err) => console.error("Error loading slides:", err));
  }, []);

  useEffect(() => {
    if (slides.length > 0) {
      const timer = setInterval(() => {
        setCurrent((prev) => (prev + 1) % slides.length);
      }, 3000); // 3 seconds per slide
      return () => clearInterval(timer);
    }
  }, [slides]);

  if (slides.length === 0) return null;

  const prevSlide = () => setCurrent((prev) => (prev - 1 + slides.length) % slides.length);
  const nextSlide = () => setCurrent((prev) => (prev + 1) % slides.length);

  return (
    <div
      className="slideshow"
      style={{ backgroundImage: `url(${slides[current].image})` }}
    >
      <div className="slideshow__overlay">
        <div className="slideshow__content">
          <h1>{slides[current].title}</h1>
          <p>{slides[current].description}</p>
          <button>Learn More</button>
        </div>
        <div className="slideshow__nav">
          <span className="prev" onClick={prevSlide}>&#10094;</span>
          <span className="next" onClick={nextSlide}>&#10095;</span>
        </div>
      </div>
    </div>
  );
};

export default SlideShow;
