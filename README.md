# Portafolio Profesional Estático - Evaluación
## Objetivo
Desarrollar una aplicación web en Django donde cada integrante (máximo 3) valor 3.0:
- Cree una app independiente
- Diseñe su hoja de vida
- Trabaje únicamente con HTML y CSS
- Use ramas bajo GitFlow
- Integre cambios mediante Pull Request hacia develop

### Contexto del Proyecto
Sistema: Portafolio Profesional Estático
Cada integrante desarrollará una sección independiente donde se visualice su hoja de vida, sin uso de base de datos ni lógica compleja, (no vistas genéricas).

Estructura del Proyecto (conceptual)

- Proyecto Django principal
- Tres apps (una por integrante)
- Carpeta de templates separada por desarrollador
- Carpeta de estilos CSS organizada por cada integrante
- Condiciones Generales
- Máximo 3 integrantes
-  Cada integrante desarrolla:
- Una app Django
- Un template HTML propio
- Sus propios estilos CSS
- No se permite:
- Modelos
- Base de datos
Solo se permite:
- HTML
- CSS
- JavaScript
- Cada funcionalidad debe trabajarse en una rama independiente
- No se permite modificar el trabajo de otro integrante sin Pull Request

### Asignación por Integrante
Dev 1, 2 y 3
Desde la Rama principal crea rama DEV:
En DEV genera feature/dev1-hoja-vida
Requerimientos:
- Crear su app
- Diseñar su hoja de vida en HTML
- Incluir:
- Datos personales
- Perfil profesional
- Formación académica
- Enlace a repositorios

### Rama adicional:
- feature/dev1-estilos
Requerimientos:
- Diseñar estilos CSS propios
- Aplicar:
Estructura tipo tarjeta
- Espaciado adecuado
Bordes y sombras
- Adaptación básica a diferentes tamaños de pantalla
- Así cada uno de los desarrolladores
Flujo de Trabajo (GitFlow)
 
***1. Crear rama***
- Partir desde develop
- Crear rama tipo feature/*

***2. Commits***
- Cada cambio debe ser un commit
independiente
- Deben ser claros y descriptivos
Ejemplo:
- creación de estructura HTML
- organización de secciones
- aplicación de estilos

***3. Subida de cambios***
- Subir la rama al repositorio remoto
- Mantener sincronización con develop

***4. Pull Request***
- Cada funcionalidad debe enviarse a
develop
- Revisión obligatoria por otro integrante
- No se permite integrar sin revisión

### Integración Final

- Consolidar todos los cambios en develop
- Crear versión de liberación de todos los
portafolios
- Validar que todas las páginas funcionen
correctamente
- Publicar versión final en main haciendo
push
- Generar un git tag de la versión completa