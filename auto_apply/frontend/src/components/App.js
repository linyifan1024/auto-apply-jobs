import React, { Component } from "react";
import { render } from "react-dom";
import NavBar from "./NavBar";
import HomePage from "./HomePage";
import RegisterPage from "./RegisterPage";
import Glassdoor from "./Glassdoor";
import Indeed from "./Indeed";
import Linkedin from "./Linkedin";
import { BrowserRouter, Routes, Route } from "react-router-dom";

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <BrowserRouter>
          <NavBar />
          <Routes>
            <Route exact path="/" element={<HomePage />} />
            <Route path="/linkedin" element={<Linkedin />} />
            <Route path="/glassdoor" element={<Glassdoor />} />
            <Route path="/indeed" element={<Indeed />} />
            <Route path="/register" element={<RegisterPage />} />
          </Routes>
        </BrowserRouter>
      </div>
    );
  }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);
