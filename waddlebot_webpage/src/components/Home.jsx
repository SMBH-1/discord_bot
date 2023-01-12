import React from "react";
import { Container, Col, Row } from "react-bootstrap";

function Home() {
  return (
    <div id={'home'} className="hero icon text-light">
      <Row>
        <Col xs={8} style={{paddingRight: '200px'}}>
          <h1 className="hdg"> WaddleBot </h1>
          <h6 > making your server as smart as... <em>a penguin?</em></h6>
        </Col>
        <Col >
          
        </Col>
      </Row>
    </div>
  );
}

export default Home;
