import React, { useState } from 'react';
import type { RegistroEscoria, NuevoRegistroEscoria} from '../../types/escoria';
import { envioService } from '../../service/escoria';
import './styles/Page.css';
import './styles/Table.css';

const Escoria: React.FC = () => {
  const [registros, setRegistros] = useState<RegistroEscoria[]>([]);
  const [nuevoRegistro, setNuevoRegistro] = useState<NuevoRegistroEscoria>({
    fecha: '',
    placa: '',
    destino: '',
    numViajes: 0,
    tipoVehiculo: 'Volqueta doble troque',
    valorUnitario: 0
  });

  const [enviando, setEnviando] = useState(false);

  const tiposVehiculo = ['Volqueta doble troque', 'Volqueta sencilla'];

  const calcularValorTotal = (numViajes: number, valorUnitario: number) => {
    return numViajes * valorUnitario;
  };

  const agregarRegistro = () => {
    if (nuevoRegistro.fecha && nuevoRegistro.placa && nuevoRegistro.destino && nuevoRegistro.numViajes > 0 && nuevoRegistro.valorUnitario > 0) {
      const registro: RegistroEscoria = {
        id: Date.now().toString(),
        ...nuevoRegistro,
        valorTotal: calcularValorTotal(nuevoRegistro.numViajes, nuevoRegistro.valorUnitario)
      };
      setRegistros([...registros, registro]);
    }
  };

  const eliminarRegistro = (id: string) => {
    setRegistros(registros.filter(registro => registro.id !== id));
  };


  const editarRegistro = (id: string, campo: keyof RegistroEscoria, valor: string | number) => {
    setRegistros(registros.map(registro => {
      if (registro.id === id) {
        const registroActualizado = { ...registro, [campo]: valor };
        if (campo === 'numViajes' || campo === 'valorUnitario') {
          registroActualizado.valorTotal = calcularValorTotal(
            campo === 'numViajes' ? Number(valor) : registro.numViajes,
            campo === 'valorUnitario' ? Number(valor) : registro.valorUnitario
          );
        }
        return registroActualizado;
      }
      return registro;
    }));
  };


  const enviarDatos = async () => {
    const sumaTotal = registros.reduce((suma, registro) => suma + registro.valorTotal, 0);
    
    // Validar datos antes de enviar
    const validacion = envioService.validarDatosEscoria({
      registros,
      total: sumaTotal
    });

    if (!validacion.valido) {
      alert(validacion.mensaje);
      return;
    }

    setEnviando(true);
    try {
      const resultado = await envioService.enviarEscoria({
        registros,
        total: sumaTotal
      });

      if (resultado.success) {
        alert(resultado.message);
        setRegistros([]); // Limpiar registros después de enviar exitosamente
      } else {
        alert(resultado.message);
      }
    } catch (error) {
      console.error('Error al enviar datos:', error);
      alert('Error inesperado al enviar los datos');
    } finally {
      setEnviando(false);
    }
  };

  const sumaTotal = registros.reduce((suma, registro) => suma + registro.valorTotal, 0);

  return (
    <div className="page-container">
      <div className="page-content">
        <h1>Registro de ESCORIA</h1>
        
        {/* Formulario para agregar nuevo registro */}
        <div className="form-section">
          <h3>Agregar Nuevo Registro</h3>
          <div className="form-grid">
            <div className="form-group">
              <label>Fecha:</label>
              <input
                type="date"
                value={nuevoRegistro.fecha}
                onChange={(e) => setNuevoRegistro({...nuevoRegistro, fecha: e.target.value})}
              />
            </div>
            
            <div className="form-group">
              <label>Placa:</label>
              <input
                type="text"
                value={nuevoRegistro.placa}
                onChange={(e) => setNuevoRegistro({...nuevoRegistro, placa: e.target.value})}
                placeholder="ABC-123"
              />
            </div>
            
            <div className="form-group">
              <label>Destino:</label>
              <input
                type="text"
                value={nuevoRegistro.destino}
                onChange={(e) => setNuevoRegistro({...nuevoRegistro, destino: e.target.value})}
                placeholder="Ubicación de destino"
              />
            </div>
            
            <div className="form-group">
              <label># de Viajes:</label>
              <input
                type="number"
                value={nuevoRegistro.numViajes}
                onChange={(e) => setNuevoRegistro({...nuevoRegistro, numViajes: Number(e.target.value)})}
                min="1"
              />
            </div>
            
            <div className="form-group">
              <label>Tipo de Vehículo:</label>
              <select
                value={nuevoRegistro.tipoVehiculo}
                onChange={(e) => setNuevoRegistro({...nuevoRegistro, tipoVehiculo: e.target.value})}
              >
                {tiposVehiculo.map(tipo => (
                  <option key={tipo} value={tipo}>{tipo}</option>
                ))}
              </select>
            </div>
            
            <div className="form-group">
              <label>Valor Unitario:</label>
              <input
                type="number"
                value={nuevoRegistro.valorUnitario}
                onChange={(e) => setNuevoRegistro({...nuevoRegistro, valorUnitario: Number(e.target.value)})}
                min="0"
                step="0.01"
              />
            </div>
            
            <div className="form-group">
              <button onClick={agregarRegistro} className="add-button">
                Agregar Registro
              </button>
            </div>
          </div>
        </div>

        {/* Tabla de registros */}
        <div className="table-section">
          <h3>Registros de ESCORIA</h3>
          {registros.length === 0 ? (
            <p className="no-data">No hay registros aún. Agrega el primer registro arriba.</p>
          ) : (
            <div className="table-container">
              <table className="data-table">
                <thead>
                  <tr>
                    <th>Fecha</th>
                    <th>Placa</th>
                    <th>Destino</th>
                    <th># Viajes</th>
                    <th>Tipo de Vehículo</th>
                    <th>Valor Unitario</th>
                    <th>Valor Total</th>
                    <th>Acciones</th>
                  </tr>
                </thead>
                <tbody>
                  {registros.map((registro) => (
                    <tr key={registro.id}>
                      <td>
                        <input
                          type="date"
                          value={registro.fecha}
                          onChange={(e) => editarRegistro(registro.id, 'fecha', e.target.value)}
                        />
                      </td>
                      <td>
                        <input
                          type="text"
                          value={registro.placa}
                          onChange={(e) => editarRegistro(registro.id, 'placa', e.target.value)}
                        />
                      </td>
                      <td>
                        <input
                          type="text"
                          value={registro.destino}
                          onChange={(e) => editarRegistro(registro.id, 'destino', e.target.value)}
                        />
                      </td>
                      <td>
                        <input
                          type="number"
                          value={registro.numViajes}
                          onChange={(e) => editarRegistro(registro.id, 'numViajes', Number(e.target.value))}
                          min="1"
                        />
                      </td>
                      <td>
                        <select
                          value={registro.tipoVehiculo}
                          onChange={(e) => editarRegistro(registro.id, 'tipoVehiculo', e.target.value)}
                        >
                          {tiposVehiculo.map(tipo => (
                            <option key={tipo} value={tipo}>{tipo}</option>
                          ))}
                        </select>
                      </td>
                      <td>
                        <input
                          type="number"
                          value={registro.valorUnitario}
                          onChange={(e) => editarRegistro(registro.id, 'valorUnitario', Number(e.target.value))}
                          min="0"
                          step="0.01"
                        />
                      </td>
                      <td className="valor-total">
                        ${registro.valorTotal.toLocaleString()}
                      </td>
                      <td>
                        <button
                          onClick={() => eliminarRegistro(registro.id)}
                          className="delete-button"
                        >
                          🗑️
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
              
              <div className="total-section">
                <h3>Total General: ${sumaTotal.toLocaleString()}</h3>
                <button 
                  onClick={enviarDatos} 
                  className="send-button"
                  disabled={enviando}
                >
                  {enviando ? 'Enviando...' : 'Enviar a API'}
                </button>
              </div>
            </div>
          )}
        </div>


        <a href="/menu" className="back-button">← Volver al menú</a>
      </div>
    </div>
  );
};

export default Escoria; 