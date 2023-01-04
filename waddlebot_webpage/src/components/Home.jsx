import React from "react";
import { Container, Col, Row } from "react-bootstrap";

function Home() {
  return (
    <div className="hero bg-dark">
      <Row>
        <Col>
          <h1 className="hdg"> Make your Discord server "smarter" </h1>
        </Col>
        <Col>
          <h6 className="hdg">some cartoon penguin or some shit</h6>
        </Col>
      </Row>
    </div>
  );
}

export default Home;
