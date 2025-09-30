import React from 'react';
import { useNavigate } from 'react-router-dom';
import './styles/Menu.css';

const Menu: React.FC = () => {
	const navigate = useNavigate();

	return (
		<div className="menu-page-container">
			<div className="menu-card">
				<div className="logo-slot" aria-label="Logo principal">
					<img className="logo-image" src="./images/Logo.jpg" alt="Logo" />
				</div>
				<h1 className="menu-title">Menú principal</h1>

				<div className="menu-actions">
					<button className="menu-button" onClick={() => navigate('/relaciones')}>
						Relaciones
					</button>
					<button className="menu-button" onClick={() => navigate('/tareas')}>
						Tareas
					</button>
					<button className="menu-button" onClick={() => navigate('/cotizaciones')}>
						Cotizaciones
					</button>
				</div>
			</div>
		</div>
	);
};

export default Menu;


