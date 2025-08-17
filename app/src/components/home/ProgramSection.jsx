import React, { useEffect, useState } from "react";
import axios from "axios";
import "./ProgramSection.css";

const ProgramSection = () => {
  const [programs, setPrograms] = useState([]);

  useEffect(() => {
    axios.get("https://mwaami-project.onrender.com/api/api/programs/")
      .then(res => setPrograms(res.data))
      .catch(err => console.error("Failed to load programs:", err));
  }, []);

  if (programs.length === 0) return null;

  return (
    <section className="programs">
      <div className="programs__container">
        <h2>Our Programs</h2>
        <div className="programs__grid">
          {programs.map((program) => (
            <div className="program__card" key={program.id}>
              {program.image && (
                <img src={program.image} alt={program.title} />
              )}
              <h3>{program.title}</h3>
              <p>{program.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default ProgramSection;
