export interface RegistroEscoria {
  id: string;
  fecha: string;
  placa: string;
  destino: string;
  numViajes: number;
  tipoVehiculo: string;
  valorUnitario: number;
  valorTotal: number;
}

export interface NuevoRegistroEscoria {
  fecha: string;
  placa: string;
  destino: string;
  numViajes: number;
  tipoVehiculo: string;
  valorUnitario: number;
}

export interface DatosEscoriaEnvio {
  registros: RegistroEscoria[];
  total: number;
}

export interface RespuestaAPI {
  success: boolean;
  message: string;
  data?: any;
} 