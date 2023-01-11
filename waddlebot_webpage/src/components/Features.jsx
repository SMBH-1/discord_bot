import React from "react";
import featurePic from "../assets/featurePic.jpg"
import { Container, Col, Row } from 'react-bootstrap'

function Features() {
  return (
    <div id={'features'} className="hero bg-primary">
      <Row>
        <Col>
        <img className="hdg" src={featurePic} width={500} style={{boxShadow: '300,0,0,0,0.5'}}></img>
          
        </Col>
        <Col>
        <h1 className="hdg">Here are the "Features"</h1>
        </Col>
      </Row>
    </div>
    
  );
}

export default Features;
