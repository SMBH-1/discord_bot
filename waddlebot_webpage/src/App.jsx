import { useState } from 'react'
import "bootswatch/dist/slate/bootstrap.min.css"
import "./App.css"
import reactLogo from './assets/react.svg'
import NavBar from './components/NavBar'
import Home from './components/Home'
import Features from './components/Features'
import Commands from './components/Commands'
import Support from './components/Support'


function App() {

  return (
    <>
    <NavBar />

    <Home />

    <Features />

    <Commands />

    <Support />

    </>
    
  )
}

export default App
