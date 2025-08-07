// Servicio para la gestion de la API

//External imports
import axios from 'axios';

const API_BASE_URL = 'http://192.168.1.42:8000/';

const api = axios.create({
  baseURL: API_BASE_URL,
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