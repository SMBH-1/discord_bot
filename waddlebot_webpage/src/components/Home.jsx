import React from "react";
import { Container, Col, Row } from "react-bootstrap";

function Home() {
  return (
    <div id={'home'} className="hero icon text-light">
      <Row>
        <Col xs={9} style={{paddingRight: '200px'}}>
        <h6 > <em>keep all of your penguins on the iceberg with...</em></h6>
          <h1 className="title"> Waddle<span className="text-dark">Bot</span> </h1>
          
        </Col>
        <Col >
          
        </Col>
      </Row>
    </div>
  );
}

export default Home;
