import React, { useEffect, useState } from "react";

const ProgramPage = () => {
  const [programs, setPrograms] = useState([]);

  useEffect(() => {
    fetch("https://209.38.93.164/api/api/programs/")
      .then((res) => res.json())
      .then((data) => setPrograms(data))
      .catch((err) => console.error("Error fetching programs:", err));
  }, []);

  return (
    <main className="program-page">
      <h1>Our Programs</h1>
      <div className="program-list">
        {programs.map((program) => (
          <div key={program.id} className="program-card">
            {program.image && <img src={program.image} alt={program.title} />}
            <h2>{program.title}</h2>
            <p>{program.description}</p>
          </div>
        ))}
      </div>
    </main>
  );
};

export default ProgramPage;
