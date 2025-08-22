import React, { useState } from "react";

const ContactPage = () => {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    message: "",
  });
  const [submitted, setSubmitted] = useState(false);

  const handleChange = (e) =>
    setFormData({ ...formData, [e.target.name]: e.target.value });

  const handleSubmit = (e) => {
    e.preventDefault();

    fetch("http://209.38.93.164/api/contactmessages/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formData),
    })
      .then((res) => {
        if (res.ok) {
          setSubmitted(true);
          setFormData({ name: "", email: "", message: "" });
        } else {
          alert("Failed to send message.");
        }
      })
      .catch(() => alert("Failed to connect to server."));
  };

  if (submitted)
    return (
      <main className="contact-page">
        <h1>Contact Us</h1>
        <p>Thank you for reaching out! We will get back to you soon.</p>
      </main>
    );

  return (
    <main className="contact-page">
      <h1>Contact Us</h1>
      <form onSubmit={handleSubmit}>
        <input
          name="name"
          placeholder="Your Name"
          value={formData.name}
          onChange={handleChange}
          required
        />
        <input
          name="email"
          type="email"
          placeholder="Your Email"
          value={formData.email}
          onChange={handleChange}
          required
        />
        <textarea
          name="message"
          placeholder="Your Message"
          value={formData.message}
          onChange={handleChange}
          required
        />
        <button type="submit">Send Message</button>
      </form>
    </main>
  );
};

export default ContactPage;
