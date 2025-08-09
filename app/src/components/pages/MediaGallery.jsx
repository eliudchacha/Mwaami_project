// src/components/pages/MediaGallery.jsx
import React, { useEffect, useState } from 'react';

const MediaGallery = () => {
  const [media, setMedia] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/media/')
      .then((res) => res.json())
      .then((data) => setMedia(data))
      .catch((err) => console.error('Error fetching media:', err));
  }, []);

  return (
    <div className="media-gallery">
      <h2>Media Gallery</h2>
      <div className="media-grid">
        {media.map((item) => (
          <div key={item.id} className="media-item">
            {item.type === 'image' ? (
              <img src={item.file} alt={item.caption} />
            ) : (
              <video controls>
                <source src={item.file} type="video/mp4" />
              </video>
            )}
            <p>{item.caption}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default MediaGallery;
