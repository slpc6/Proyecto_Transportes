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

export interface RegistroCenizaSubtabla {
  id: string;
  fecha: string;
  placa: string;
  material: string;
  numViajes: number;
  tipoVehiculo: string;
  destino: string;
  valorUnitario: number;
  valorTotal: number;
}

export interface NuevoRegistroCenizaSubtabla {
  fecha: string;
  placa: string;
  material: string;
  numViajes: number;
  tipoVehiculo: string;
  destino: string;
  valorUnitario: number;
}

export interface DatosCenizaEnvio {
  registros: RegistroCeniza[];
  registrosSubtabla: RegistroCenizaSubtabla[];
  total: number;
  totalSubtabla: number;
}

export interface RespuestaAPI {
  success: boolean;
  message: string;
  data?: any;
} 