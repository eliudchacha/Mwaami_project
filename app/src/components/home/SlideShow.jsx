import React, { useEffect, useState } from "react";
import "./SlideShow.css";
import axios from "axios";

const SlideShow = () => {
  const [slides, setSlides] = useState([]);
  const [current, setCurrent] = useState(0);

  // Fetch slides from backend
  useEffect(() => {
    axios
      .get("https://mwaami-project.onrender.com/api/api/slides")
      .then((res) => setSlides(res.data))
      .catch((err) => console.error("Error loading slides:", err));
  }, []);

  // Auto-slide every 5 seconds
  useEffect(() => {
    if (slides.length === 0) return;

    const timer = setInterval(() => {
      setCurrent((prev) => (prev + 1) % slides.length);
    }, 3000);

    return () => clearInterval(timer);
  }, [slides]);

  if (slides.length === 0) return null;

  return (
    <div className="slideshow">
      {slides.map((slide, index) => (
        <div
          key={index}
          className={`slide ${index === current ? "active" : ""}`}
          style={{ backgroundImage: `url(${slide.image})` }}
        >
          <div className="slide-caption">
            <h3>{slide.title}</h3>
            <p>{slide.description}</p>
          </div>
        </div>
      ))}
    </div>
  );
};

export default SlideShow;
