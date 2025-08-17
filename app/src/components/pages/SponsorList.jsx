// src/components/pages/SponsorList.jsx
import React, { useEffect, useState } from 'react';

const SponsorList = () => {
  const [sponsors, setSponsors] = useState([]);

  useEffect(() => {
    fetch("https://mwaami-project.onrender.com/api/api/sponsors/")
      .then((res) => res.json())
      .then((data) => setSponsors(data))
      .catch((err) => console.error('Error fetching sponsors:', err));
  }, []);

  return (
    <div className="sponsor-list">
      <h2>Our Sponsors</h2>
      <div className="sponsor-grid">
        {sponsors.map((sponsor) => (
          <div key={sponsor.id} className="sponsor-card">
            <img src={sponsor.logo} alt={sponsor.name} />
            <h3>{sponsor.name}</h3>
            <p>{sponsor.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default SponsorList;
