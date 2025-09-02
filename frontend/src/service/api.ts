// Servicio para la gestion de la API

//External imports
import axios from 'axios';

const API = import.meta.env.API_BASE_URL

const api = axios.create({
  
  baseURL: API,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 10000, // 10 segundos
});

// Interceptor para manejar errores globalmente
api.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error('Error en la API:', error);
    if (error.response) {
      // El servidor respondió con un código de error
      console.error('Respuesta del servidor:', error.response.data);
    } else if (error.request) {
      // La petición fue hecha pero no se recibió respuesta
      console.error('No se recibió respuesta del servidor');
    } else {
      // Algo más causó el error
      console.error('Error en la petición:', error.message);
    }
    return Promise.reject(error);
  }
);

export default api;