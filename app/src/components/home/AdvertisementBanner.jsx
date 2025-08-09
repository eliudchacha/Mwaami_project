import React, { useEffect, useState } from 'react';

const AdvertisementBanner = () => {
  const [ads, setAds] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/ads/')
      .then((res) => res.json())
      .then((data) => setAds(data))
      .catch((error) => console.error('Error fetching ads:', error));
  }, []);

  return (
    <section className="ad-banner">
      {ads.map((ad) => (
        <div className="ad-item" key={ad.id}>
          <img src={ad.image} alt={ad.title} />
          <div className="ad-text">
            <h3>{ad.title}</h3>
            <p>{ad.description}</p>
          </div>
        </div>
      ))}
    </section>
  );
};

export default AdvertisementBanner;
