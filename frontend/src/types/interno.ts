export interface RegistroInterno {
  id: string;
  fecha: string;
  placa: string;
  numViajes: number;
  tipoVehiculo: string;
  valorUnitario: number;
  valorTotal: number;
}

export interface NuevoRegistroInterno {
  fecha: string;
  placa: string;
  numViajes: number;
  tipoVehiculo: string;
  valorUnitario: number;
}

export interface DatosInternoEnvio {
  registros: RegistroInterno[];
  total: number;
}

export interface RespuestaAPI {
  success: boolean;
  message: string;
  data?: any;
} 