import React, { useEffect, useState } from "react";
import "./Hero.css";
import axios from "axios";

const Hero = () => {
  const [heroData, setHeroData] = useState(null);

  useEffect(() => {
    axios.get("https://eliudwaryoba.me/api/api/heropages/")
      .then(response => {
        setHeroData(response.data[0]); // assuming only 1 hero object
      })
      .catch(error => {
        console.error("Failed to fetch hero data:", error);
      });
  }, []);

  if (!heroData) return null;

  return (
    <section
      className="hero"
      style={{ backgroundImage: `url(${heroData.image})` }}
    >
      <div className="hero__overlay">
        <div className="hero__content">
          <h1>{heroData.title}</h1>
          <p>{heroData.subtitle}</p>
          <a href="/about" className="hero__btn">Learn More</a>
        </div>
      </div>
    </section>
  );
};

export default Hero;
