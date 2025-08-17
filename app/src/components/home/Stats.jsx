import React, { useEffect, useState } from "react";
import axios from "axios";
import "./Stats.css";

const Stats = () => {
  const [stats, setStats] = useState([]);

  useEffect(() => {
    axios.get("https://mwaami-project.onrender.com/api/api/impactstats/")
      .then(res => setStats(res.data))
      .catch(err => console.error("Failed to load impact stats:", err));
  }, []);

  if (stats.length === 0) return null;

  return (
    <section className="stats">
      <div className="stats__container">
        <h2>Our Impact</h2>
        <div className="stats__grid">
          {stats.map((item) => (
            <div className="stat__card" key={item.id}>
              <h3>{item.number}</h3>
              <p>{item.title}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Stats;
