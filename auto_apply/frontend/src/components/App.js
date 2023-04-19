import React from "react";
import ReactDOM from "react-dom";
import NavBar from "./NavBar";
import HomePage from "./HomePage";
import RegisterPage from "./RegisterPage";
import Glassdoor from "./Glassdoor";
import Indeed from "./Indeed";
import Linkedin from "./Linkedin";
import {
  BrowserRouter,
  Router,
  Routes,
  Switch,
  Route,
  Link,
} from "react-router-dom";
export default class App extends Component {
  constructor(props) {
    super(props);
  }

ReactDOM.createRoot(document.getElementById("app")).render(
  <React.StrictMode>
    <Router>
      <NavBar />
      <Routes>
        <Route exact path="/" element={<HomePage />} />
        <Route path="/linkedin" element={<Linkedin />} />
        <Route path="/glassdoor" element={<Glassdoor />} />
        <Route path="/indeed" element={<Indeed />} />
        <Route path="/register" element={<RegisterPage />} />
      </Routes>
    </Router>
  </React.StrictMode>
);
