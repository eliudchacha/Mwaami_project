import React, { useEffect, useState } from "react";
import "./SlideShow.css";
import axios from "axios";

const SlideShow = () => {
  const [slides, setSlides] = useState([]);
  const [current, setCurrent] = useState(0);

  useEffect(() => {
    axios
      .get("https://mwaami-project.onrender.com/api/api/slides")
      .then((res) => {
        // Ensure image URLs are absolute
        const slidesWithAbsoluteUrls = res.data.map(slide => ({
          ...slide,
          image: slide.image.startsWith('http') 
            ? slide.image 
            : `https://mwaami-project.onrender.com${slide.image}`
        }));
        setSlides(slidesWithAbsoluteUrls);
      })
      .catch((err) => console.error("Error loading slides:", err));
  }, []);

  useEffect(() => {
    if (slides.length > 0) {
      const timer = setInterval(() => {
        setCurrent((prev) => (prev + 1) % slides.length);
      }, 3000);
      return () => clearInterval(timer);
    }
  }, [slides]); // Keep slides as dependency

  if (slides.length === 0) return null;

  const prevSlide = () => setCurrent((prev) => (prev - 1 + slides.length) % slides.length);
  const nextSlide = () => setCurrent((prev) => (prev + 1) % slides.length);

  return (
    <div
      className="slideshow"
      style={{ 
        backgroundImage: `url(${slides[current]?.image})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center'
      }}
    >
      <div className="slideshow__overlay">
        <div className="slideshow__content">
          <h1>{slides[current]?.title}</h1>
          <p>{slides[current]?.description}</p>
          <button>Learn More</button>
        </div>
        {/* Hidden navigation that still works */}
        <div className="slideshow__nav" style={{ opacity: 0 }}>
          <span className="prev" onClick={prevSlide}>&#10094;</span>
          <span className="next" onClick={nextSlide}>&#10095;</span>
        </div>
      </div>
    </div>
  );
};

export default SlideShow;