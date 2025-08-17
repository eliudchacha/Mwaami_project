import React, { useEffect, useState } from "react";
import "./SlideShow.css";
import axios from "axios";

const SlideShow = () => {
  const [slides, setSlides] = useState([]);
  const [current, setCurrent] = useState(0);

  useEffect(() => {
    axios.get( "https://mwaami-project.onrender.com/api/api/slides")
      .then(res => setSlides(res.data))
      .catch(err => console.error("Error loading slides:", err));
  }, []);

  useEffect(() => {
    const timer = setInterval(() => {
      setCurrent((prev) => (prev + 1) % slides.length);
    }, 5000);
    return () => clearInterval(timer);
  }, [slides]);

  if (slides.length === 0) return null;

  return (
    <div className="slideshow">
      <img src={slides[current].image} alt={slides[current].title} />
      <div className="slideshow__caption">
        <h3>{slides[current].title}</h3>
        <p>{slides[current].description}</p>
      </div>
    </div>
  );
};

export default SlideShow;
