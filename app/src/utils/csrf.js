// src/utils/csrf.js

/**
 * Utility for safely handling CSRF tokens with Django backend
 * ------------------------------------------------------------
 * - Looks for csrftoken in cookies (default Django name).
 * - Provides helper to attach token to fetch/axios calls.
 * - Ensures frontend stays secure against CSRF attacks.
 */

/**
 * Extracts CSRF token from cookies
 * @returns {string|null} token or null if not found
 */
export function getCsrfToken() {
    const name = "csrftoken=";
    const decodedCookie = decodeURIComponent(document.cookie);
    const cookies = decodedCookie.split(";");
    for (let cookie of cookies) {
      cookie = cookie.trim();
      if (cookie.startsWith(name)) {
        return cookie.substring(name.length);
      }
    }
    return null;
  }
  
  /**
   * Wrapper for fetch that automatically includes CSRF token
   * @param {string} url - API endpoint
   * @param {object} options - fetch options (method, headers, body…)
   * @returns {Promise<Response>}
   */
  export async function csrfFetch(url, options = {}) {
    const token = getCsrfToken();
  
    // Default headers
    const headers = {
      "Content-Type": "application/json",
      ...(options.headers || {}),
    };
  
    // Only attach CSRF for unsafe methods
    if (token && ["POST", "PUT", "PATCH", "DELETE"].includes((options.method || "GET").toUpperCase())) {
      headers["X-CSRFToken"] = token;
    }
  
    return fetch(url, {
      ...options,
      headers,
      credentials: "include", // important for sending cookies with requests
    });
  }
  