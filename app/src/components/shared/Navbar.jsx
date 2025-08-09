import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import "./Navbar.css";

const Navbar = () => {
  const [isMobileMenuOpen, setMobileMenuOpen] = useState(false);

  const toggleMenu = () => setMobileMenuOpen(!isMobileMenuOpen);

  // 🛠️ Close menu when window is resized to large screens
  useEffect(() => {
    const handleResize = () => {
      if (window.innerWidth > 768) {
        setMobileMenuOpen(false);
      }
    };

    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  return (
    <header className="navbar">
      <div className="navbar__container">
        <div className="navbar__logo">
          <Link to="/">
            <img
              src="/logo.png"
              alt="Mwaami foundation Logo"
              className="navbar__logo-img"
            />
            <span>Mwaami Foundation</span>
          </Link>
        </div>

        <nav className={`navbar__menu ${isMobileMenuOpen ? "active" : ""}`}>
          <Link to="/">Home</Link>
          <Link to="/about">About</Link>
          <Link to="/programs">Programs</Link>
          <Link to="/children">Children</Link>
          <Link to="/sponsors">Sponsors</Link>
          <Link to="/media">Media</Link>
          <Link to="/contact">Contact</Link>
        </nav>

        <button className="navbar__toggle" onClick={toggleMenu}>
          ☰
        </button>
      </div>
    </header>
  );
};

export default Navbar;
