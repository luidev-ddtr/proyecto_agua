# Documentacion para el Frontend

Recuerda investigas mas a fondo como es que funciona el framewrok de astro para que puedas modificarlo mas rapido

## 🚀 Project Structure

/
├── ✅ ZONAS SEGURAS (Puedes modificar aquí)
│   ├── public/              # 📸 Recursos públicos (imágenes, videos)
│   │   ├── fondoForm.webp   # Fondo para formularios
│   │   ├── logo.svg         # Logo editable (¡mantén el nombre!)
│   │   └── puente.webp      # Imágenes de contenido
│   │
│   └── src/                 # 💻 Código editable
│       ├── pages/           # 🌐 Páginas principales
│       │   ├── index.astro  # Página de inicio
│       │   ├── login.astro  # Login de usuarios
│       │   └── crud/        # Operaciones de base de datos
│       │       ├── personas/ # ABM de personas
│       │       └── pagos/    # Gestión de pagos
│       │
│       └── components/      # 🧩 Componentes reutilizables
│           ├── Header.astro # Barra de navegación
│           ├── Logo.astro   # Componente del logo
│           └── crud/        # Componentes CRUD
│               ├── personas/ # Formularios de personas
│               └── pagos/    # Formularios de pagos
│
└── 🚫 ZONAS PROHIBIDAS (No tocar)
    ├── .astro/              # Configuración automática de Astro
    ├── node_modules/        # Dependencias instaladas (autogenerado)
    ├── dist/                # Versión compilada (autogenerado)
    ├── .env                 # Contraseñas y claves
    └── [Otros archivos de configuración]


## 🧞 Commandos

All commands are run from the root of the project, from a terminal:

| Command                |               Action                             |
| :--------------------- | :------------------------------------------------|
| `pnpm install`         | Installs dependencies                            |
| `pnpm dev`             | Starts local dev server at `localhost:4321`      |
| `pnpm build`           | Build your production site to `./dist/`          |
| `pnpm run deploy`      | Deploy the pagues auto, with gh-pagues           |
| `pnpm preview`         | Preview your build locally, before deploying     |
| `pnpm astro ...`       | Run CLI commands like `astro add`, `astro check` |
| `pnpm astro -- --help` | Get help using the Astro CLI                     |

## 👀 Want to learn more?

Feel free to check [our documentation](https://docs.astro.build) or jump into our [Discord server](https://astro.build/chat).



## Agregar o quitar un componente al formulario sin romperlo
Ya tenemos algunos componentes hechos, pero para el formulario es un solo documento que puede 
ser dificil de manejar si no se conoce a produndidad, por eso en este ejemplo se modificara un compoenten

primero que nada ejecuta

```bash
pnpm run dev # Para poder ejecutar tu servidor de desarrollo
```


## 📝 Documentación Completa del Formulario de Registro de pago

### 🔍 Sección de Búsqueda

#### 🎯 Funcionalidad Principal
```javascript
x-data="{
  searchTerm: '',
  isLoading: false,
  results: [],
  error: null,
  hasSearched: false,
  
  async search() {
    // Implementación de búsqueda con:
    // - Validación de término (min 2 chars)
    // - Manejo de estados (loading/error)
    // - Transformación de datos
  }
}"
```
###  Componente de Búsqueda
```html
<div class="relative mb-6 mt-4">
  <div class="flex items-center gap-2 bg-white p-2 rounded-lg shadow-md border-2 border-blue-500">
    <svg><!-- Ícono de búsqueda --></svg>
    <input 
      type="text" 
      x-model="searchTerm"
      placeholder="Buscar por nombre o manzana..."
      class="flex-1 p-2 focus:outline-none text-gray-700"
    >
  </div>
</div>
```
### Sección de Formulario
```javascript
// Validación de cantidad (ejemplo completo)
validarCantidad() {
  this.form.cantidad = parseInt(this.form.cantidad);
  
  if (isNaN(this.form.cantidad)) {
    this.errors.cantidad = 'Debe ingresar un número válido';
    return false;
  }
  
  if (this.form.cantidad < 0 || this.form.cantidad > 1500) {
    this.errors.cantidad = 'Debe ser entre 0 y 1500';
    return false;
  }
  
  this.errors.cantidad = '';
  return true;
}
```

### Envío de Datos
```javascript
async submitForm() {
  const formData = {
    id_persona: this.form.id_persona,
    tomas: this.form.tomas,
    cantidad: this.form.cantidad
    // ...otros campos
  };

  try {
    const response = await fetch(`${window.API_ENDPOINT}/create_pay`, {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(formData)
    });
    // Manejo de respuesta
  } catch (error) {
    // Manejo de errores
  }
}
```
### Componentes visuales
```html
<table class="min-w-full">
  <tbody class="divide-y divide-gray-200">
    <template x-for="persona in results" :key="persona.id">
      <tr @click="selectItem(persona)" 
          :class="{
            'hover:bg-blue-100': persona.selectable,
            'bg-blue-50': activeItem?.id === persona.id
          }">
        <!-- Columnas con datos -->
      </tr>
    </template>
  </tbody>
</table>
```
### Notificaciones
```javascript
showNotification(message, type = 'success') {
  const notification = document.createElement('div');
  notification.className = `fixed top-4 right-4 px-4 py-2 rounded-md shadow-lg text-white ${
    type === 'success' ? 'bg-green-500' : 'bg-red-500'
  }`;
  notification.textContent = message;
  document.body.appendChild(notification);
  
  setTimeout(() => notification.remove(), 3000);
}
```

### 🔄 Flujo Completo
Búsqueda → 2. Selección → 3. Validación → 4. Envío → 5. Notificación





# 📝 Documentación del Componente de Edición de Personas

## 🌟 Introducción
Este componente permite visualizar y editar registros de personas en una tabla interactiva, con validaciones avanzadas y un modal de edición.

## 🏗 Estructura Principal

```html
<div x-data="{...}" x-init="fetchData">
  <!-- Estados -->
  <template x-if="isLoading">...</template>
  <template x-if="error">...</template>
  
  <!-- Tabla de resultados -->
  <template x-if="!isLoading && !error">
    <div class="overflow-x-auto rounded-lg shadow-lg">
      <table class="min-w-full bg-white">
        <!-- Cabecera y filas de datos -->
      </table>
    </div>
  </template>

  <!-- Modal de edición -->
  <div x-show="showModal" class="fixed inset-0 z-50">
    <!-- Contenido del modal -->
  </div>
</div>
```

### 🔍 Funcionalidades Clave
📊 Tabla de Datos
Carga asíncrona de datos desde API (/read_us)

Visualización paginada

Botones de acción por fila

### ✏️ Modal de Edición
Formulario con validaciones en tiempo real

Campos especiales:
```javascript
form: {
  id: null,
  nombre: '',
  apellidos: '',
  estado_especial: '', // 1-4
  manzana: '', // Select
  estudia: '0', // Radio
  fecha_nac: '' // DD/MM/AAAA
}
```

### Validaciones Avanzadas
```javascript
validarNombre() {
  // 3-30 caracteres, solo letras
}

formatearApellidos() {
  // 1-2 apellidos, 2-30 caracteres cada uno
  // Autocorrección de formato (Primera letra mayúscula)
}

formatearFechaInput() {
  // Autoformato DD/MM/AAAA
  // Validación de fecha real
}

scrollToFirstError() {
  // Enfoca y desplaza al primer campo con error
}

```

### 🔄 Flujo de Operación
```javascript
fetchData() {
  fetch(`${window.API_ENDPOINT}/read_us`)
    .then(/*...*/)
}

//Edicion
openEditModal(persona) {
  // Prepara datos para edición
}

//Guardado
saveChanges() {
  // Valida → Formatea → Envía a API (/update_us)
}
```
### 🎨 Componentes Visuales
```javascript
showNotification(message, type) {
  // Toast animado (éxito/error)
}
```
### 🖱 Botones de Acción
```html
<button @click="openEditModal(persona)"
        class="bg-blue-500 hover:bg-blue-600...">
  Editar
</button>
```
### ⚠️ Campos No Editables
Campo	Razón
Manzana	Definida por sistema
Fecha Nacimiento	Datos históricos


### 📌 Ejemplo de Uso
```javascript
// Para agregar nueva validación:
validarNuevoCampo() {
  if(!this.form.nuevo) {
    this.errors.nuevo = 'Requerido';
    return false;
  }
  return true;
}
```

### 🔄 Dependencias
Alpine.js (gestión de estado)

Fetch API (comunicación con backend)

Tailwind CSS (estilos)

