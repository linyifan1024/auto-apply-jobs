import React, { Component } from "react";
import Nav from "react-bootstrap/Nav";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";
import Form from "react-bootstrap/Form";
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
export default class NavBar extends Component {
  constructor(props) {
    super(props);
    this.state = {
      showLoginModal: false,
    };

    this.handleShowLogin = this.handleShowLogin.bind(this);
    this.handleCloseLogin = this.handleCloseLogin.bind(this);
  }
  handleShowLogin() {
    this.setState({ showLoginModal: true });
  }

  handleCloseLogin() {
    this.setState({ showLoginModal: false });
  }
  render() {
    return (
      <div>
        <Nav defaultActiveKey="/home" as="ul">
          <Nav.Item as="li">
            <Nav.Link href="/">Home</Nav.Link>
          </Nav.Item>
          <Nav.Item as="li">
            <Nav.Link href="/linkedin">Linkedin</Nav.Link>
          </Nav.Item>
          <Nav.Item as="li">
            <Nav.Link href="/glassdoor">Glassdoor</Nav.Link>
          </Nav.Item>
          <Nav.Item as="li">
            <Nav.Link href="/indeed">Indeed</Nav.Link>
          </Nav.Item>
          <Nav.Item as="li">
            <Link to="/register" className="nav-link">
              Register
            </Link>
          </Nav.Item>
          <Nav.Item as="li">
            <Button variant="light" onClick={this.handleShowLogin}>
              Login
            </Button>{" "}
          </Nav.Item>
        </Nav>

        <Modal show={this.state.showLoginModal} onHide={this.handleCloseLogin}>
          <Modal.Header closeButton>
            <Modal.Title>Login</Modal.Title>
          </Modal.Header>
          <Modal.Body>
            <Form>
              <Form.Group controlId="formBasicEmail">
                <Form.Label>Email address</Form.Label>
                <Form.Control type="email" placeholder="Enter email" />
              </Form.Group>

              <Form.Group controlId="formBasicPassword">
                <Form.Label>Password</Form.Label>
                <Form.Control type="password" placeholder="Password" />
              </Form.Group>
            </Form>
          </Modal.Body>
          <Modal.Footer>
            <Button variant="secondary" onClick={this.handleCloseLogin}>
              Close
            </Button>
            <Button variant="primary" onClick={this.handleCloseLogin}>
              Login
            </Button>
          </Modal.Footer>
        </Modal>
      </div>
    );
  }
}
