import React, { Component } from 'react';
import logo from './books.svg';
import './App.css';

class App extends Component {
  render() {
    return (
	<div className="App">
    <img src={logo} className="App-logo" alt="logo" /><h1>LeoBook</h1>
	</div>
    );
  }
}

export default App;