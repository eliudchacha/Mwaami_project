import React, { useEffect, useState } from 'react';

const SponsorsSection = () => {
  const [sponsors, setSponsors] = useState([]);

  useEffect(() => {
    fetch('https://209.38.93.164/api/api/sponsors/')
      .then((res) => res.json())
      .then((data) => setSponsors(data))
      .catch((error) => console.error('Error fetching sponsors:', error));
  }, []);

  return (
    <section className="sponsors-section">
      <h2>Our Sponsors</h2>
      <div className="sponsors-grid">
        {sponsors.map((sponsor) => (
          <div className="sponsor-card" key={sponsor.id}>
            <img src={sponsor.logo} alt={sponsor.name} />
            <h4>{sponsor.name}</h4>
          </div>
        ))}
      </div>
    </section>
  );
};

export default SponsorsSection;
