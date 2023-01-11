import React from "react";
import CommandCard from "./CommandCard";
import { Container, Col, Row } from "react-bootstrap";

function Commands() {
  return (
    <Container id={'commands'} className="hero bg-dark">
      <Col>
        <Row>
          <h1 className="hdg" style={{paddingTop: '20px'}}>
            Simple, useful commands
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
            <CommandCard 
              name={"/help"}
              description="display all available music bot commands"
            />
            <CommandCard 
              name={"/play"}
              description="search for a song on YouTube and play it in your current channel"
              args="<keywords>"
            />
            <CommandCard 
              name={"/queue"}
              description="display the current music queue"
            />
            <CommandCard 
              name={"/skip"}
              description="skip the current song"
            />
            <CommandCard 
              name={"/clear"}
              description="stop music and clear the queue"
            />
            <CommandCard 
              name={"/leave"}
              description="disconnect the music bot from the voice channel"
            />
            <CommandCard 
              name={"/pause"}
              description="pause the current song"
            />
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
