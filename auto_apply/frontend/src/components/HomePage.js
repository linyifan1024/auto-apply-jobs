import React, { Component } from "react";
import Nav from "react-bootstrap/Nav";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";
import Form from "react-bootstrap/Form";
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import NavBar from "./NavBar";
export default class HomePage extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <NavBar />
        <div className="home-page">
          <h1 className="home-page-title">Hello, this is our homepage </h1>
          <p className="home-page-text">
            This is a sample home page for my app.
          </p>
          <p className="home-page-text">
            You can customize this page to fit your needs.
          </p>
        </div>
      </div>
    );
  }
}
