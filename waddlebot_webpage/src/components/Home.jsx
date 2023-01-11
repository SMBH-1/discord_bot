import React from "react";
import { Container, Col, Row } from "react-bootstrap";

function Home() {
  return (
    <div id={'home'} className="hero icon text-dark">
      <Row>
        <Col style={{paddingRight: '200px'}}>
          <h1 className="hdg"> WaddleBot </h1>
          <h5 className="hdg"> making your server as smart as... a penguin? </h5>
        </Col>
        <Col>
          
        </Col>
      </Row>
    </div>
  );
}

export default Home;
