import React, { useEffect, useState } from "react";
import "./SlideShow.css";
import axios from "axios";

const SlideShow = () => {
  const [slides, setSlides] = useState([]);
  const [current, setCurrent] = useState(0);

  // Fetch slides from API
  useEffect(() => {
    axios
      .get("https://eliudwaryoba.me/api/api/slides")
      .then((res) => {
        const slidesWithAbsoluteUrls = res.data.map((slide) => ({
          ...slide,
          image: slide.image.startsWith("http")
            ? slide.image
            : `https://eliudwaryoba.me${slide.image}`,
        }));
        setSlides(slidesWithAbsoluteUrls);
      })
      .catch((err) => console.error("Error loading slides:", err));
  }, []);

  // Auto change slide every 3s
  useEffect(() => {
    if (slides.length > 0) {
      const timer = setInterval(() => {
        setCurrent((prev) => (prev + 1) % slides.length);
      }, 3000);
      return () => clearInterval(timer);
    }
  }, [slides]);

  if (slides.length === 0) return null;

  return (
    <div
      className="slideshow"
      style={{
        backgroundImage: `url(${slides[current]?.image})`,
        backgroundSize: "cover",
        backgroundPosition: "center",
      }}
    >
      <div className="slideshow__overlay">
        <div className="slideshow__content">
          <h1>{slides[current]?.title}</h1>
          <p>{slides[current]?.description}</p>
          <button>Learn More</button>
        </div>
      </div>
    </div>
  );
};

export default SlideShow;
