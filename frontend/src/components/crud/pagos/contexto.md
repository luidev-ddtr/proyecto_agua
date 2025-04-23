El enfoque que estás utilizando se conoce como "Islands Architecture" (Arquitectura de Islas) cuando combinas JavaScript en línea (is:inline) con Alpine.js, manteniendo la modularidad y separación de responsabilidades.

Características clave de este enfoque:
JavaScript colocado cerca del markup relevante:

El código JS está en el mismo archivo HTML (pero en bloques <script> separados)

Se usa is:inline para mantenerlo debuggable

Pero organizado en componentes modulares con Alpine.js

Ventajas específicas de tu implementación:

Debugging más fácil: El código no está minificado/ofuscado

Co-locación: La lógica está cerca del markup que la usa

Modularidad: Cada componente Alpine (x-data) es una unidad autocontenida

Separación de responsabilidades:

Alpine.js maneja el estado y la UI

El backend maneja la lógica de negocio/persistencia

Patrones relacionados que estás aplicando:

Component-Based Architecture: (como en React/Vue, pero más ligero)

Progressive Enhancement: Alpine.js mejora el HTML estático

SPA-like patterns: Sin llegar a ser una SPA completa

Cómo se compara con otros enfoques:
Enfoque	Ejemplo	Ventajas en tu caso
Islands + Alpine	Tu solución	Debugging fácil, modularidad
SPA clásica	React/Vue completo	Demasiado complejo para tu necesidad
HTML + JS separado	jQuery clásico	Menos organizado, difícil debugging
Server-centric	HTMX	Menos control client-side
Buenas prácticas que estás siguiendo:
Single File Components implícitos:

Cada bloque Alpine.js actúa como un componente

State management localizado:

El estado vive en x-data, no en variables globales

Separation of Concerns:

HTML (estructura), Alpine (comportamiento), CSS (estilos)

Progressive Disclosure:

La complejidad JS solo aparece donde se necesita

Recomendación final: Si quieres investigar más, busca "Alpine.js Islands Architecture" o "Progressively Enhanced SPA". Es un enfoque moderno para aplicaciones que no justifican React/Vue pero necesitan más organización que jQuery tradicional.