import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';

function NavBar() {

  return (
    <Navbar variant="dark" style={{border: '0px', position: "sticky", background: 'rgb(39,43,48)', zIndex: '1'}} fixed={'top'} expand="lg">
      <Container >
        <Navbar.Brand style={{border: '0px'}}href="#home">WaddleBot</Navbar.Brand>
        <Navbar.Toggle style={{border: '0px'}} aria-controls="basic-navbar-nav" />
        <Navbar.Collapse style={{border: '0px'}} id="basic-navbar-nav">
          <Nav style={{border: '0px'}} className="me-auto">
            <Nav.Link style={{border: '0px'}} href="#home" onClick={(e) => {e.preventDefault(); window.location.replace('/#home');}}>Home</Nav.Link>
            <Nav.Link style={{border: '0px'}} href="#link" onClick={(e) => {e.preventDefault(); window.location.replace('/#features');}}>Features</Nav.Link>
            <Nav.Link style={{border: '0px'}} href="#commands" onClick={(e) => {e.preventDefault(); window.location.replace('/#commands');}}>Commands</Nav.Link>
            <Nav.Link style={{border: '0px'}} href="#support" onClick={(e) => {e.preventDefault(); window.location.replace('/#support');}}>Docs</Nav.Link>
            <Nav.Link style={{border: '0px'}} href="https://discord.com/oauth2/authorize?client_id=1060252204461740173&permissions=4398046511091&scope=bot">Add to Discord</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default NavBar;