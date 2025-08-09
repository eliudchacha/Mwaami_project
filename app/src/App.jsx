import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Navbar from "./components/shared/Navbar";
import Footer from "./components/shared/Footer";

import HomePage from "./pages/HomePage";
import AboutPage from "./pages/AboutPage";
import ProgramPage from "./pages/ProgramPage";
import ChildrenPage from "./pages/ChildrenPage";
import DonationPage from "./pages/DonationPage";
import SponsorsPage from "./pages/SponsorsPage";
import MediaPage from "./pages/MediaPage";
import ContactPage from "./pages/ContactPage";
import NotFoundPage from "./pages/NotFoundPage";

function App() {
  return (
    <Router>
      <div className="app-container">
        <Navbar />
        <main className="main-content">
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/about" element={<AboutPage />} />
            <Route path="/programs" element={<ProgramPage />} />
            <Route path="/children" element={<ChildrenPage />} />
            <Route path="/donate" element={<DonationPage />} />
            <Route path="/sponsors" element={<SponsorsPage />} />
            <Route path="/media" element={<MediaPage />} />
            <Route path="/contact" element={<ContactPage />} />
            <Route path="*" element={<NotFoundPage />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
