import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import EventoList from './components/EventoList';
import EventoDetail from './components/EventoDetail';  // ← verificar nome correto
import './App.css';

function App() {
  return (
    <div className="app-container">
      <header className="app-header">
        <h1><Link to="/" className="logo">EVENTOS+</Link></h1>
      </header>

      <main className="app-main">
        <Routes>
          <Route path="/" element={<EventoList />} />
          <Route path="/evento/:id" element={<EventoDetail />} />
        </Routes>
      </main>

      <footer className="app-footer">
        <small>Frontend consumindo API Django — Eventos & Ingressos</small>
      </footer>
    </div>
  );
}

export default App;
