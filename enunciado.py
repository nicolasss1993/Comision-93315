"""
Entrega de Proyecto Final
Introducción

En esta instancia final del curso vas a preparar la entrega completa de tu aplicación web desarrollada con Django. El objetivo es revisar el alcance del proyecto, verificar que incluya las funcionalidades mínimas requeridas y preparar la aplicación para ser compartida y evaluada.
Durante esta etapa trabajarás sobre tres aspectos clave:
la validación de que tu aplicación cumple con los requisitos funcionales establecidos,
la preparación del proyecto para su despliegue,
y la documentación profesional del proyecto.
Además de comprobar que la aplicación funcione correctamente, deberás generar una forma clara de acceder al proyecto y comprender su funcionamiento. Para ello prepararás una URL pública o simulada y elaborarás una documentación que explique cómo instalar, ejecutar y utilizar la aplicación.
Esta actividad representa el cierre del proceso de aprendizaje del curso, integrando conocimientos técnicos y habilidades de documentación propias del desarrollo profesional de software.

Teoría
Alcance del Proyecto Final: Análisis Detallado
El alcance del proyecto final define qué funcionalidades y características debe incluir tu aplicación web tipo blog para considerarse completa y funcional. En este caso, los requisitos mínimos son:
Administración (Admin): Acceso al panel administrativo de Django para gestionar contenido y usuarios.
Registro y Perfiles de Usuario: Permitir que los usuarios se registren, inicien sesión y gestionen su perfil.
Páginas Funcionales: Creación y visualización de entradas de blog, páginas estáticas y navegación.
Formularios con Validación: Formularios para crear o editar contenido, con validaciones que aseguren la integridad de los datos.
Importante: Analizar si tu proyecto cumple con estos criterios es fundamental para garantizar que la entrega sea exitosa y cumpla con las expectativas del programa.
Preparación para Despliegue y Entrega (URL Pública)
Para que tu aplicación sea accesible desde cualquier lugar, debes desplegarla y generar una URL pública. Los pasos clave incluyen:
Configuración de settings.py: Ajusta parámetros como ALLOWED_HOSTS, configuración de archivos estáticos (STATIC_URL, STATIC_ROOT) y archivos media (MEDIA_URL, MEDIA_ROOT).
Manejo de Archivos Estáticos y Media: Asegúrate de recolectar los archivos estáticos con collectstatic y que estén accesibles en el entorno de despliegue.
Archivo requirements.txt: Incluye todas las dependencias necesarias para que el entorno de despliegue pueda instalar los paquetes con pip install -r requirements.txt.
Generación de URL Pública: Puedes usar servicios gratuitos como Heroku, PythonAnywhere, o herramientas como Ngrok para exponer tu servidor local temporalmente.
Ejemplo: Ngrok permite crear un túnel seguro a tu servidor local, generando una URL pública que puedes compartir para demostraciones rápidas.
Contexto
En la industria tecnológica, entregar un proyecto funcional y bien documentado es tan importante como desarrollarlo correctamente. Las empresas valoran que los desarrolladores no solo creen soluciones, sino que también las desplieguen y comuniquen claramente cómo usarlas y mantenerlas. En este sentido, preparar una URL pública accesible y un repositorio con instrucciones claras es una práctica estándar que facilita la colaboración, revisión y despliegue en entornos reales.
Además, el análisis del alcance del proyecto te ayuda a verificar que todas las funcionalidades esenciales estén implementadas y funcionando, evitando sorpresas en la entrega final. La correcta configuración para despliegue y la documentación detallada son habilidades clave que te preparan para proyectos profesionales y colaborativos en el mundo real.
En el desarrollo profesional de software no solo es importante construir una aplicación funcional, sino también presentarla y documentarla correctamente.
Las empresas también valoran que los desarrolladores sean capaces de:
compartir sus proyectos de manera accesible
documentar los pasos necesarios para ejecutar una aplicación
preparar proyectos para su despliegue
facilitar la evaluación y revisión del código
Disponer de una URL pública, un repositorio organizado y una documentación clara son prácticas habituales en entornos de trabajo colaborativos.
El proceso de verificar el alcance del proyecto, preparar su despliegue y documentarlo adecuadamente permite acercarse a las prácticas reales utilizadas en equipos de desarrollo profesionales.
Práctica
Para consolidar lo aprendido, realiza las siguientes actividades:
Verifica el Alcance de tu Proyecto: Revisa que tu aplicación incluya todas las funcionalidades mínimas: panel admin, registro y perfiles, páginas y formularios con validación.
Prepara tu Proyecto para Despliegue:
Ajusta el archivo settings.py según las indicaciones.
Asegúrate de tener un archivo requirements.txt actualizado.
Ejecuta collectstatic para los archivos estáticos.
Genera una URL Pública: Utiliza un servicio gratuito (Heroku, PythonAnywhere) o Ngrok para exponer tu aplicación.
Documenta tu Proyecto: Crea un README que incluya:
Descripción del proyecto.
Pasos para ejecutar localmente.
URL pública para acceso.
Capturas de pantalla que evidencien las funcionalidades.
Recuerda: Esta entrega es la culminación de tu aprendizaje. Asegúrate de que todo funcione correctamente y que la documentación sea clara y completa.
Formato de entrega
La entrega del proyecto final deberá realizarse mediante un URL a una presentación en Google Slides que funcione como un README e informe visual del proyecto.
El objetivo de esta presentación es documentar de forma clara el funcionamiento de la aplicación desarrollada, incluyendo capturas de pantalla, explicación de las funcionalidades y referencias al repositorio del proyecto.
La presentación debe permitir comprender el proyecto, su funcionamiento y cómo ejecutarlo.
Elementos que debe incluir la entrega
1. Enlace al repositorio de GitHub
La presentación debe incluir la URL del repositorio público en GitHub donde se encuentre alojado el proyecto.
El repositorio debe contener:
Código completo de la aplicación.
Estructura organizada del proyecto.
Archivo requirements.txt con las dependencias necesarias.
Archivo README.md con la documentación del proyecto.
2. Descripción del proyecto
Explicación clara y breve que incluya:
propósito del proyecto
problema que busca resolver
funcionalidades principales de la aplicación
tipo de usuario al que está orientado
3. Funcionalidades principales
Descripción de las funcionalidades implementadas en la aplicación.
Se recomienda acompañar cada funcionalidad con capturas de pantalla que evidencien su funcionamiento.
Por ejemplo:
panel de administración
registro o autenticación de usuarios
páginas principales de la aplicación
formularios y creación de contenido
4. Instrucciones para ejecutar el proyecto
Explicar brevemente cómo ejecutar la aplicación en un entorno local.
Debe incluir:
requisitos previos (por ejemplo: Python, entorno virtual)
instalación de dependencias
ejecución del servidor de desarrollo
Estas instrucciones pueden presentarse como una versión resumida del README del repositorio.
5. Despliegue de la aplicación
Incluir:
enlace a la URL pública del proyecto (si se encuentra desplegado)
breve explicación del entorno utilizado para el despliegue
(por ejemplo: Render, Railway, PythonAnywhere, etc.)
Si el proyecto no se encuentra desplegado, puede incluirse una simulación del proceso de despliegue explicando cómo se realizaría.
6. Evidencia visual del funcionamiento
La presentación debe incluir capturas que demuestren el funcionamiento de la aplicación.
Se recomienda incluir:
panel de administración
registro de usuarios
navegación entre páginas
formularios funcionando
ejemplos de contenido creado
Cada captura debe incluir una breve descripción de lo que se está mostrando.
Recomendaciones
Antes de realizar la entrega, verificar que:
el repositorio de GitHub sea público
el enlace al repositorio esté correctamente incluido en la presentación
las capturas de pantalla evidencien claramente las funcionalidades
la presentación tenga una estructura clara y ordenada
Entregable: [object Object]

"""
