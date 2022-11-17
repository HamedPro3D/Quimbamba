<p class=text-align-justify> <h2> Proyecto Final </h2> 
**Integrante 1, *** Integrante 2

** Estudiante de Ingeniería Chanel Naomi Olier Watson, Código: 200110086 

*** Estudiante de Ingeniería Hamed J. Elneser Tejeda, Código: xxxxxxxxxx 

<b>Profesor:</b> Pedro Jose D. Posada Aguilar 

Programación Orientada a Objetos 

Fecha (17-11-22) 

Barranquilla-Colombia 
</p>

### **Estructura y contenido**

1. #### **Definiciones y especificación de requerimientos**
	*  <h5> Definición general del proyecto de software </h5> <p class=text-align-justify>[nombre del juego] es un juego 2D tipo Souls-like de acción y aventura. Inspirado en el famoso juego Zelda buscando crear un juego de alta dificultad que para los amantes de los clásicos 2D. </p>
	* ##### **Especificación de requerimientos del proyecto** 
		* **Requerimientos generales:**
			* Un solo jugador
			* Buena jugabilidad
		* **Requerimientos funcionales:**
			* Visualizar cuando se pierde una vida
			* Mostrar notificación de perdida de vida
			* Visualizar el menú de opciones
			* Poder seccionar el personaje deseado para la partida.
			*  Visualizar animación del personaje caminando (hacia izquierda y derecha)
			*  Ingresar al juego
			*  Salir del juego
			*  Avanzar al siguiente nivel
			*  Notificación de nivel completado

		* **Información de autoria y legacy del proyecto**: <p class=text-align-justify> <em>explicitar si el proyecto de software forma parte de desarrollos previos/preexistentes o si es original, y en el caso correspondiente, detalles de retro-compatibilidad. </em> </p>
		* **Alcances del sistema:** <p class=text-align-justify><em> las limitaciones y alcances del desarrollo, de acuerdo a los objetivos previamente establecidos. </em> </p>

	* ##### Procedimientos
		* **procedimientos de desarrollo:** 
			* **Herramientas utilizadas:<p class=text-align-justify>** Para la creación del programa se utilizó una variedad de herramientas, las cuales son: 
				* Visual Studio Code: Un editor de código, en donde se escribió todo el código del programa.
				* Tiled: Es un editor de mapas con en cual se diseñó el mapa del juego.
				* Craftpix.net: Pagina que dispone recursos gráficos premiums y de libre uso. 
				* Aseprite: Es un editor de gráficos rasterizados, con el cual se diseñaron los sprites de los personajes.</p>
			* **Planificación:** <p class=text-align-justify> <em>una descripción global de la metodología utilizada para encarar y resolver el problema; por ejemplo: los pasos ejecutados a lo largo de la resolución del proyecto, a grandes rasgos.</em> </p>
		* **Procedimientos de instalación y prueba:** 
			* **Requisitos no funcionales:**
				* Buen rendimiento
				* Cero bugs
			* **Especificaciones de prueba y ejecución:** 
			<p class=text-align-justify> Para este proyecto no se creará ejecutable por lo que el programa correrá directamente del editor de código VSC. EL interprete será el lenguaje de programación  <em><b>Python v3.10.</b></em> </p>

2. #### Arquitectura del sistema
	* <h5> Descripción jerárquica </h5> <p class=text-align-justify> El programa se encuentra organizado por módulos de Python bajo el modelo <u>POO</u>. Por lo que agrupa una colección de objetos de la misma estructura para conformar una clase, siendo así cada objeto una instancia de su clase. </p>
	* <h5> Diagrama de módulos (UML) </h5>
		* <b> Imagen del UML </b>
		![UML__Quimbamba](https://user-images.githubusercontent.com/105728306/202447113-118f2d9d-8beb-472e-b100-7fc7e5006c53.png)
		* <b> Codigo del UML </b>
		<pre>
			@startuml Quimbamba
			Title Diagrama UML de Quimbamba
			class Ajustes #lightgreen;line:darkgreen{
			Largo: int
			Ancho: int
			FPS: int
			TILESIZE: int
			WORLD_MAP: str
			}
			
			class Debug #lightgreen;line:darkgreen{
			font: str
			debug(info, y: int, x: int)
			}
			
			class Jugador #lightgreen;line:darkgreen{
			pos: float
			grupos: float
			obstaculos: str
			image: str
			rect: int
			hitbox: int
			estado: str
			animaciondent: int
			velocidadanimacion: float
			direccion: int
			velocidad: int
			ataque: boolean
			ataqueesp: int
			sw: int
			animaciones(self)
			input(self)
			estados(self)
			move(self, velocidad: int)
			espera(self)
			secuencia(self)
			colicion(self, direccion: int )
			update(self)
			}
			        
			class Main #lightgreen;line:darkgreen{
			pantalla: str
			frames: float
			run(self)
			}
			
			class Nivel #lightgreen;line:darkgreen{
			mostrars: str
			spritev: str
			obstaculos: str
			crearmapa(self)
			run(self)
			}
			
			class YCamaraGrupo #lightgreen;line:darkgreen{
			mostrars: int
			mitadancho: int
			mitadlargo: int
			offset: int
			suelo_superficie: str
			suelo_rect: int
			custom_draw(self, jugador: int)
			}
			
			class Soporte #lightgreen;line:darkgreen{
			import_csv_layout(path: str)
			import_folder(path: str)
			}
			
			class Suelo #lightgreen;line:darkgreen{
			pos: int
			grupos: float
			sprite_type: str
			surface: str
			image: int
			}
			
			Ajustes " 1 " <--* "    1 " Main
			Nivel--* " 1 "Main
			Debug " * "-- "       1   "Main
			Jugador " * " --> " 1 " Ajustes
			Jugador " * " *-- " * "Soporte
			Nivel " * "--> " 1 "Ajustes
			Nivel " * "--* " * "Jugador
			Nivel " * "-- " * "Debug
			Nivel " * "*-- " * "Suelo
			Nivel " * " *-- " * " Soporte
			Nivel " * " *-- YCamaraGrupo: compone
			Suelo " * " *--> " 1 " Ajustes
	</code></pre>
	* <h5> Descripción general de los módulos </h5>
		<p class=text-align-justify><em>*Para cada módulo o parte del sistema, se debería realizar una breve descripción del mismo, la cual debería incluir mínimamente:  </em></p>
		* <b> Descripción general y propósito:</b><p class=text-align-justify><em> ¿qué es y qué debería hacer el módulo? </em></p>
		* <b> Responsabilidad y restricciones:</b> <p class=text-align-justify><em> ¿cuál es su función específica dentro del sistema? ¿qué cosas puede y no puede hacer? </em></p>
		* <b> Dependencias:</b> <p class=text-align-justify><em>  Indicar cuales son los requisitos del módulo, es decir se debe contestar a preguntas tales como _¿qué necesita o requiere el módulo para funcionar? ¿necesita de servicios brindados por otros módulos o por librerías externas?</em></p>
		* <b> Implementación: </b><p class=text-align-justify><em> indicar en qué archivo o archivos se encuentra la implementación del módulo.
		
			No es el objetivo de esta sección dar detalles de _cómo_ se realiza la implementación de los módulos, sino únicamente dar una idea general de _para qué_ existe el módulo dentro del sistema. </em></p>
	* <h5> Dependencias externas </h5><p class=text-align-justify><em>Si el software utiliza librerías o servicios externos estos deben listarse junto con una breve descripción de las mismas.</p>
	Adicionalmente en esta sección se deben listar los **aspectos técnicos** o **tecnologías empleadas** en el proyecto, tales como el lenguaje de programación, _frameworks_, librerías, etc.</p>
	Puede resultar de utilidad incluir junto a estos una breve descripción de las decisiones de diseño asociadas que llevaron a elegir la o las tecnologías en particular, es decir responder a _¿por qué se utilizó esta tecnología y no otra?_</em></p>
3. <h4> Documentación técnica </h4>
	 <p class=text-align-justify><em> Se indica el propósito y breve descripción de cada método/función, con su prototipo indicando argumentos (nombre, tipo, propósito de cada uno) y respuesta (tipo, descripción).</p> 
	<p class=text-align-justify>Para llevar a cabo esta tarea, es posible utilizar una variedad de herramientas de generación de documentación automática, a partir del código en el encabezado de cada función (por ejemplo Javadoc, PHPDoc, Doxygen, etc).
	<p class=text-align-justify> La documentación técnica debe pensarse como el manual del programador, y debe apuntar a aquellas personas que estarán a cargo de mantener, ampliar, o crear un proyecto derivado a partir de nuestro proyecto. </em></p>


*[POO]: Programación Orientada a Objetos
*[UML]: Lenguaje Unificado de Modelado
*[VSC]: Visual Studio Code
