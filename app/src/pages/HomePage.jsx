import React from "react";
import Hero from "../components/home/Hero";
import SlideShow from "../components/home/SlideShow";
import AboutSection from "../components/home/AboutSection";
import ProgramSection from "../components/home/ProgramSection";
import Stats from "../components/home/Stats";
import TestimonialSection from "../components/home/TestimonialSection";
import SponsorsSection from "../components/home/SponsorsSection";
import StaffSection from "../components/home/StaffSection"; // NEW IMPORT

const HomePage = () => (
  <>
    <Hero />
    <SlideShow />
    <AboutSection />
    <ProgramSection />
    <Stats />
    <TestimonialSection />
    <SponsorsSection />
    <StaffSection /> 
  </>
);

export default HomePage;
