import React from "react";
import featurePic from "../assets/featurePic.jpg"
import { Container, Col, Row } from 'react-bootstrap'

function Features() {
  return (
    <div id={'features'} className="hero bg-primary">
      <Row className="d-flex align-items-center">
        <Col>
        <img className="hdg" src={featurePic} width={500} style={{boxShadow: '300,0,0,0,0.5'}}></img>
          
        </Col>
        <Col>
        <h1 className="hdg">Features</h1>
        <button type="button" class="btn btn-warning">Utility</button><button type="button" class="btn btn-warning">Music</button><br/>
        <button type="button" class="btn btn-warning">AI Chat</button><button type="button" class="btn btn-warning">Gaming</button>
        <br />
        <br />
        <br />
        <a href="https://discord.com/oauth2/authorize?client_id=1060252204461740173&permissions=4398046511091&scope=bot">
        <button type="button" class="btn btn-info">Add to Discord</button>
        </a>
        </Col>

        
      </Row>
    </div>
    
  );
}

export default Features;
