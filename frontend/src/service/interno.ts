import api from './api';
import type { DatosInternoEnvio, RespuestaAPI } from '../types/interno';

export const envioService = {
  async enviarInterno(datos: DatosInternoEnvio): Promise<RespuestaAPI> {
    try {
      const response = await api.post('/interno', datos);
      return {
        success: true,
        message: 'Datos enviados exitosamente',
        data: response.data
      };
    } catch (error: any) {
      let message = 'Error al enviar los datos';
      
      if (error.response) {
        message = error.response.data?.message || `Error ${error.response.status}: ${error.response.statusText}`;
      } else if (error.request) {
        message = 'No se pudo conectar con el servidor. Verifica que la API esté ejecutándose.';
      } else {
        message = error.message || 'Error desconocido al enviar los datos';
      }
      
      return {
        success: false,
        message,
        data: null
      };
    }
  },

  validarDatosInterno(datos: DatosInternoEnvio): { valido: boolean; mensaje: string } {
    if (!datos.registros || datos.registros.length === 0) {
      return { valido: false, mensaje: 'No hay registros para enviar' };
    }

    for (const registro of datos.registros) {
      if (!registro.fecha || !registro.placa) {
        return { valido: false, mensaje: 'Todos los campos son obligatorios' };
      }

      if (registro.numViajes <= 0 || registro.valorUnitario <= 0) {
        return { valido: false, mensaje: 'El número de viajes y valor unitario deben ser mayores a 0' };
      }
    }

    return { valido: true, mensaje: 'Datos válidos' };
  }
}; 