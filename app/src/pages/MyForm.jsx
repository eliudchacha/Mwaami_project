import axios from "axios";
import { getCSRFToken } from "../utils/csrf"; // adjust path if needed

axios.defaults.withCredentials = true;

const csrftoken = getCSRFToken();

axios.post("https://209.38.93.164/api/endpoint/", data, {
  headers: { "X-CSRFToken": csrftoken }
})
.then(res => console.log(res.data))
.catch(err => console.error(err));
