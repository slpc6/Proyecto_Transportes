import api from './api';
import type { DatosCenizaEnvio, RespuestaAPI } from '../types/ceniza';

export const envioService = {

  async enviarCeniza(datos: DatosCenizaEnvio): Promise<RespuestaAPI> {
    try {
      const response = await api.post('/ceniza', datos);
      return {
        success: true,
        message: 'Datos enviados exitosamente',
        data: response.data
      };
    } catch (error: any) {
      let message = 'Error al enviar los datos';
      
      if (error.response) {
        // El servidor respondió con un código de error
        message = error.response.data?.message || `Error ${error.response.status}: ${error.response.statusText}`;
      } else if (error.request) {
        // La petición fue hecha pero no se recibió respuesta
        message = 'No se pudo conectar con el servidor. Verifica que la API esté ejecutándose.';
      } else {
        // Algo más causó el error
        message = error.message || 'Error desconocido al enviar los datos';
      }
      
      return {
        success: false,
        message,
        data: null
      };
    }
  },


  validarDatosCeniza(datos: DatosCenizaEnvio): { valido: boolean; mensaje: string } {
    if (!datos.registros || datos.registros.length === 0) {
      return {
        valido: false,
        mensaje: 'No hay registros para enviar'
      };
    }

    // Validar registros principales
    for (const registro of datos.registros) {
      if (!registro.fecha || !registro.placa || !registro.destino) {
        return {
          valido: false,
          mensaje: 'Todos los campos son obligatorios en la tabla principal'
        };
      }

      if (registro.numViajes <= 0 || registro.valorUnitario <= 0) {
        return {
          valido: false,
          mensaje: 'El número de viajes y valor unitario deben ser mayores a 0 en la tabla principal'
        };
      }
    }

    return {
      valido: true,
      mensaje: 'Datos válidos'
    };
  }
};
