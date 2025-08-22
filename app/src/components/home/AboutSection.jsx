import React, { useEffect, useState } from "react";
import axios from "axios";
import "./AboutSection.css";

const AboutSection = () => {
  const [about, setAbout] = useState(null);

  useEffect(() => {
    axios.get("https://eliudwaryoba.me/api/api/about/")
      .then(res => setAbout(res.data[0]))  // assuming one about record
      .catch(err => console.error("Failed to load about data:", err));
  }, []);

  if (!about) return null;

  return (
    <section className="about">
      <div className="about__container">
        <h2>About Us</h2>
        <p className="about__mission">{about.mission}</p>
        <p className="about__vision">{about.vision}</p>
      </div>
    </section>
  );
};

export default AboutSection;
