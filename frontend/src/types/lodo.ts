export interface RegistroLodo {
    id: string;
    fecha: string;
    placa: string;
    numViajes: number;	
    producto: string;	
    destino: string;	
    tipoVehiculo: string;
    valorUnitario: number;
    valorTotal: number;
}

export interface NuevoRegistroLodo {
    fecha: string;
    placa: string;
    numViajes: number;	
    producto: string;	
    destino: string;	
    tipoVehiculo: string;
    valorUnitario: number;
}

export interface DatosLodoEnvio {
    registros: RegistroLodo[];
    total: number;
}

export interface RespuestaAPI {
    success: boolean;
    message: string;
    data?: any;
}