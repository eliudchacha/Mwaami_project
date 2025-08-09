import React, { useEffect, useState } from "react";

const AboutPage = () => {
  const [about, setAbout] = React.useState(null);

  React.useEffect(() => {
    fetch("http://127.0.0.1:8000/api/about/")
      .then((res) => res.json())
      .then((data) => setAbout(data[0]))
      .catch((err) => console.error("Error fetching about:", err));
  }, []);

  if (!about) return <p>Loading...</p>;

  return (
    <main className="about-page">
      <h1>About Us</h1>
      <p>{about.mission}</p>
      <p>{about.vision}</p>
      {/* Add more details if available */}
    </main>
  );
};

export default AboutPage;
