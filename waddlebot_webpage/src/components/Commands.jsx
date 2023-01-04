import React from "react";
import CommandCard from "./CommandCard";
import { Container, Col, Row } from "react-bootstrap";

function Commands() {
  return (
    <Container className="hero bg-dark">
      <Col>
        <Row>
          <h1 className="hdg">
            maybe some sample commands w a link to commands/docs page
          </h1>
        </Row>

        <Row>
          <h3> Type of Command </h3>
        </Row>

        {/* Add your command cards below. 

      Command cards will take the following props:
        name (string) - The command used to execute the feature
        description (string) - What the command does
        args - Arguments for the command, if any
        cooldown - Cooldown for the command, if any

       */}
        <Row>
          <Col s={6}>
            <CommandCard
              name={"testcommand"}
              description="description of command goes here"
              args="arguments"
              cooldown="10s"
            />
          </Col>
          <Col s={6}>
            <CommandCard
              name={"help"}
              description="show a list of all available commands"
            />
            <CommandCard
              name={"!lookup"}
              description="look up a WoW character to determine their highest arena achievement"
            />
          </Col>
        </Row>
      </Col>
    </Container>
  );
}

export default Commands;
