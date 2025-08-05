import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './styles/Main.css';

const Main: React.FC = () => {
  const [selectedOption, setSelectedOption] = useState<string>('');
  const navigate = useNavigate();

  const options = [
    { value: 'CENIZA', label: 'CENIZA', path: '/ceniza' },
    { value: 'ESCORIA', label: 'ESCORIA', path: '/escoria' },
    { value: 'INTERNO', label: 'INTERNO', path: '/interno' },
    { value: 'LODO', label: 'LODO', path: '/lodo' }
  ];

  const handleOptionChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    const selected = event.target.value;
    setSelectedOption(selected);
    
    if (selected) {
      const option = options.find(opt => opt.value === selected);
      if (option) {
        navigate(option.path);
      }
    }
  };

  return (
    <div className="main-container">
      <div className="menu-selector">
        <h2>Selecciona una opción</h2>
        <div className="select-wrapper">
          <select
            value={selectedOption}
            onChange={handleOptionChange}
            className="option-select"
          >
            <option value="">-- Selecciona una opción --</option>
            {options.map((option) => (
              <option key={option.value} value={option.value}>
                {option.label}
              </option>
            ))}
          </select>
        </div>
        {selectedOption && (
          <div className="selected-info">
            <p>Redirigiendo a: <strong>{selectedOption}</strong></p>
          </div>
        )}
      </div>
    </div>
  );
};

export default Main;
