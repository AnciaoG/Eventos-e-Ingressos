import React from 'react';
import { Link, NavLink } from 'react-router-dom';
import './Header.css';

export default function Header() {
  return (
    <header className="site-header">
      <div className="container header-content">
        <Link to="/" className="logo">EVENTOS+</Link>
        <nav className="nav-links">
          <NavLink to="/" end>Início</NavLink>
          <NavLink to="/#eventos">Eventos</NavLink>
          <NavLink to="/#contato">Contato</NavLink>
          <button className="btn">Entrar</button>
        </nav>
      </div>
    </header>
  );
}
