import React, { useState, useRef } from 'react'
import "./App.css"
import "bootswatch/dist/slate/bootstrap.min.css"
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';

import NavBar from './components/NavBar'
import Home from './components/Home'
import Features from './components/Features'
import Commands from './components/Commands'
import Support from './components/Support'
import CommandTable from './components/CommandTable'


function App() {


  return (
    <>
    {/* <Navbar variant="dark" style={{border: '0px'}} expand="lg">
      <Container >
        <Navbar.Brand style={{border: '0px'}}href="#home">WaddleBot</Navbar.Brand>
        <Navbar.Toggle style={{border: '0px'}} aria-controls="basic-navbar-nav" />
        <Navbar.Collapse style={{border: '0px'}} id="basic-navbar-nav">
          <Nav style={{border: '0px'}} className="me-auto">
            <Nav.Link style={{border: '0px'}} >Home</Nav.Link>
            <Nav.Link style={{border: '0px'}} >Features</Nav.Link>
            <Nav.Link style={{border: '0px'}} >Commands</Nav.Link>
            <Nav.Link style={{border: '0px'}} >Support</Nav.Link>
            <Nav.Link style={{border: '0px'}} href="https://discord.com/oauth2/authorize?client_id=1060252204461740173&permissions=4398046511091&scope=bot">Add to Discord</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar> */}
    <NavBar />

    <Home className='home'/>

    <Features className='features'/>

    <Commands className='commands'/>

    <Support className='support'/>
    <CommandTable />

    </>
    
  )
}

export default App
