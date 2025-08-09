import React from "react";
import { Link } from "react-router-dom";

const NotFoundPage = () => (
  <main style={{ textAlign: "center", padding: "5rem" }}>
    <h1>404 - Page Not Found</h1>
    <p>Sorry, the page you requested does not exist.</p>
    <Link to="/">Go back Home</Link>
  </main>
);

export default NotFoundPage;
