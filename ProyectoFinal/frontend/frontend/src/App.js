import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  state = {
    todos: []
  };

  async componentDidMount() {
    try {
      const res = await fetch('http://127.0.0.1:8000/index/');
      const todos = await res.json();
      console.log(todos)
      this.setState({
        todos
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
      <div>
        {this.state.todos.map(item => (
          <div key={item.id}>
            <h1>Titulo: {item.titulo}</h1>
            <br></br>
            <span>Contenido: {item.contenido}</span>
            <br></br>
            <span>Fecha: {item.fecha }</span>
            <br></br>
            <span>Usuario: {item.id_admin}</span>
          </div>
        ))}
      </div>
    );
  }
}

export default App;