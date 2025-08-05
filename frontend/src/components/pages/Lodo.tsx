import React from 'react';
import './styles/Page.css';

const Lodo: React.FC = () => {
  return (
    <div className="page-container">
      <div className="page-content">
        <h1>Página de LODO</h1>
        <p>Esta es la página para la opción LODO.</p>
        <a href="/main" className="back-button">← Volver al menú</a>
      </div>
    </div>
  );
};

export default Lodo; 