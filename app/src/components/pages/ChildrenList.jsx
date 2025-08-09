// src/components/pages/ChildrenList.jsx
import React, { useEffect, useState } from 'react';

const ChildrenList = () => {
  const [children, setChildren] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/child/')
      .then((res) => res.json())
      .then((data) => setChildren(data))
      .catch((err) => console.error('Error fetching children:', err));
  }, []);

  return (
    <div className="children-list">
      <h2>Our Children</h2>
      <div className="children-grid">
        {children.map((child) => (
          <div key={child.id} className="child-card">
            <img src={child.photo} alt={child.name} />
            <h3>{child.name}</h3>
            <p>{child.age} years old</p>
            <p>{child.story}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ChildrenList;
