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

export interface RegistroEscoriaSubtabla {
  id: string;
  fecha: string;
  placa: string;
  numViajes: number;
  destino: string;
  tipoVehiculo: string;
  valorUnitario: number;
  valorTotal: number;
}

export interface NuevoRegistroEscoriaSubtabla {
  fecha: string;
  placa: string;
  numViajes: number;
  destino: string;
  tipoVehiculo: string;
  valorUnitario: number;
}

export interface DatosEscoriaEnvio {
  registros: RegistroEscoria[];
  registrosSubtabla: RegistroEscoriaSubtabla[];
  total: number;
  totalSubtabla: number;
}

export interface RespuestaAPI {
  success: boolean;
  message: string;
  data?: any;
} 