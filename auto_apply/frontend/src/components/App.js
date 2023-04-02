import React, { Component } from "react";
import { render } from "react-dom";

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div className="home-page">
        <h1 className="home-page-title">Auto Apply for your jobs </h1>
        <p className="home-page-text">This is a sample home page for my app.</p>
        <p className="home-page-text">
          You can customize this page to fit your needs.
        </p>
      </div>
    );
  }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);
