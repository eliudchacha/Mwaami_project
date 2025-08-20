// src/components/shared/Footer.jsx
import React, { useState } from "react";
import "./Footer.css";
import { csrfFetch } from "./utils/csrf";

const Footer = () => {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    subject: "",
    message: "",
  });
  const [status, setStatus] = useState(null);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await csrfFetch("/api/message/", {
        method: "POST",
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        setStatus("Message sent successfully!");
        setFormData({ name: "", email: "", subject: "", message: "" });
      } else {
        const data = await response.json();
        setStatus(`Error: ${JSON.stringify(data)}`);
      }
    } catch (err) {
      setStatus("Network error: unable to send message");
      console.error(err);
    }
  };

  return (
    <footer className="footer">
      <div className="footer__container">
        {/* Existing copyright & links */}
        <p>&copy; {new Date().getFullYear()} Mwaami Foundation. All rights reserved.</p>
        <div className="footer__links">
          <a href="#">Privacy Policy</a>
          <a href="#">Terms</a>
        </div>

        {/* New Contact Form */}
        <div className="footer__contact">
          <h3>Contact Us</h3>
          <form onSubmit={handleSubmit} className="footer__form">
            <input
              type="text"
              name="name"
              placeholder="Your Name"
              value={formData.name}
              onChange={handleChange}
              required
            />
            <input
              type="email"
              name="email"
              placeholder="Your Email"
              value={formData.email}
              onChange={handleChange}
              required
            />
            <input
              type="text"
              name="subject"
              placeholder="Subject"
              value={formData.subject}
              onChange={handleChange}
              required
            />
            <textarea
              name="message"
              placeholder="Message"
              value={formData.message}
              onChange={handleChange}
              required
            />
            <button type="submit">Send Message</button>
          </form>
          {status && <p className="footer__status">{status}</p>}
        </div>
      </div>
    </footer>
  );
};

export default Footer;
