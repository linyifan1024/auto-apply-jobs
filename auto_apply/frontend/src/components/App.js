import React, { Component } from "react";
import { render } from "react-dom";
import NavBar from "./NavBar";
import HomePage from "./HomePage";
import RegisterPage from "./RegisterPage";
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

  render() {
    return (
      <div>
        <BrowserRouter>
          <NavBar />
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/register" element={<RegisterPage />} />
          </Routes>
        </BrowserRouter>
      </div>
    );
  }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);
