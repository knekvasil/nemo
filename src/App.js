import React, {useState, useEffect} from 'react';
import './App.css';

function App() {
  const [currentData, setCurrentData] = useState(0);

  useEffect(() => {
    fetch('/users/all/').then(res => res.json()).then(jsData => {
      setCurrentData(jsData.data);
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h3>The requested data is:</h3>
        <p>{currentData}</p>
      </header>
    </div>
  );
}

export default App;
