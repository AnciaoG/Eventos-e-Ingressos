// src/App.jsx
import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import Home from './pages/Home';
import EventoDetail from './pages/EventoDetail';
import './App.css';

function App() {
  return (
    <div className="app-container">
      <Header />
      <main className="app-main">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/evento/:id" element={<EventoDetail />} />
        </Routes>
      </main>
      <Footer />
    </div>
  );
}

export default App;
