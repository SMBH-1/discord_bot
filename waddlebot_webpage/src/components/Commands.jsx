import React from "react";
import CommandCard from "./CommandCard";
import { Container, Col, Row } from "react-bootstrap";

function Commands() {
  return (
    <Container id={"commands"} className="hero bg-dark bt-3">
      <Col>
        <Row>
          <h1 className="hdg pb-3" >
            Simple, useful commands
          </h1>
        </Row>

        <Row>
          <Col>
            <h3> Music </h3>
          </Col>
          <Col>
            {" "}
            <h3>Utility</h3>
          </Col>
          <Col>
            <h3> General</h3>
          </Col>
        </Row>

        {/* Add your command cards below. 

      Command cards will take the following props:
        name (string) - The command used to execute the feature
        description (string) - What the command does
        args - Arguments for the command, if any
        cooldown - Cooldown for the command, if any

       */}
        <Row>
          <Col>
            <CommandCard
              name={"/play"}
              description="search for a song on YouTube and play it in your current channel"
              args="<keywords>"
            />
            <CommandCard
              name={"/leave"}
              description="disconnect the music bot from the voice channel"
            />
          </Col>
          <Col>
            <CommandCard
              name={"!chatbot"}
              description="have a conversation with ChatGPT"
            />
            <CommandCard
              name={"!commands"}
              description="view a list of all available commands"
            />
            <CommandCard
              name={"!server"}
              description="display basic server statistics"
            />
          </Col>
          <Col>
            <CommandCard
              name={"/resume"}
              description="resume the current song"
            />
          </Col>
        </Row>
      </Col>
    </Container>
  );
}

export default Commands;
