import React, { useEffect, useState } from "react";
import "./StaffSection.css";

const StaffSection = () => {
  const [staff, setStaff] = useState([]);

  useEffect(() => {
    fetch("http://eliudwaryoba.me/api/api/staff/") // API endpoint from Django
      .then((res) => res.json())
      .then((data) => setStaff(data))
      .catch((err) => console.error("Error fetching staff:", err));
  }, []);

  return (
    <section className="staff-section">
      <h2>Meet Our Staff</h2>
      <div className="staff-grid">
        {staff.map((member) => (
          <div key={member.id} className="staff-card">
            <img src={member.photo} alt={member.name} />
            <h3>{member.name}</h3>
            <p>{member.position}</p>
          </div>
        ))}
      </div>
    </section>
  );
};

export default StaffSection;
