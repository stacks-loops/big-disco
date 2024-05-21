import React from 'react'
import DinoForm from './DinoForm.js'
import './App.css';

function App() {
    const handleSubmit = (event) => {
      event.preventDefault();
    }


  return (
    <div className="App">
      <DinoForm onSubmit={handleSubmit} />
  </div>
  );
}


export default App;
