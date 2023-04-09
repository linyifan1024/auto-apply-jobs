import React, { Component } from "react";
import { render } from "react-dom";
import NavBar from "./NavBar";
import HomePage from "./HomePage";
import { BrowserRouter, Router, Switch, Route, Link } from "react-router-dom";
export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return <HomePage />;
  }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);
