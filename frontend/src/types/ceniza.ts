export interface RegistroCeniza {
  id: string;
  fecha: string;
  placa: string;
  destino: string;
  numViajes: number;
  tipoVehiculo: string;
  valorUnitario: number;
  valorTotal: number;
}

export interface NuevoRegistroCeniza {
  fecha: string;
  placa: string;
  destino: string;
  numViajes: number;
  tipoVehiculo: string;
  valorUnitario: number;
}

export interface DatosCenizaEnvio {
  registros: RegistroCeniza[];
  total: number;
}

export interface RespuestaAPI {
  success: boolean;
  message: string;
  data?: any;
} 