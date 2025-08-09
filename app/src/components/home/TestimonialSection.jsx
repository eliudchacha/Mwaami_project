import React, { useEffect, useState } from "react";
import axios from "axios";
import "./TestimonialSection.css";

const TestimonialSection = () => {
  const [testimonials, setTestimonials] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/testimonials/")
      .then(res => setTestimonials(res.data))
      .catch(err => console.error("Error loading testimonials:", err));
  }, []);

  if (testimonials.length === 0) return null;

  return (
    <section className="testimonials">
      <div className="testimonials__container">
        <h2>What People Say</h2>
        <div className="testimonials__grid">
          {testimonials.map((item) => (
            <div className="testimonial__card" key={item.id}>
              <p className="testimonial__quote">"{item.message}"</p>
              <h4 className="testimonial__author">— {item.author}</h4>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default TestimonialSection;
