<p class=text-align-center> <h2> Proyecto Final </h2> 
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
			* **Obtención e instalación:** <p class=text-align-justify><em> una guía sencilla que explique el procedimiento básico para obtener e instalar el sistema. La guía debe estar dirigida a usuarios con nivel de experiencia preestablecido en la **definición general del proyecto**. </em> </p>
			* **Especificaciones de prueba y ejecución:** 
			<p class=text-align-justify> <em>  datos técnicos sobre la plataforma y/o entornos a utilizar en la prueba o ejecución del software en cuestión. </em> </p>

2. #### Arquitectura del sistema
	* <h5> Descripción jerárquica </h5> <p class=text-align-justify> El programa se encuentra organizado por módulos de Python bajo el modelo <u>POO</u>. Por lo que agrupa una colección de objetos de la misma estructura para conformar una clase, siendo así cada objeto una instancia de su clase. </p>
	* <h5> Diagrama de módulos (UML) </h5>
		* <b> Imagen del UML </b>
		* <b> Codigo del UML </b>
		<pre>
		@startuml
		class Ajustes{
		
		Largo: int
		Ancho: int
		FPS: int
		TILESIZE: int
		WORLD_MAP: str
		
		}
		
		class Debug{
		font: str
		debug(info, y: int, x: int)
		}
		
		class Jugador{
		pos: float
		grupos:
		obstaculos:
		image: str
        rect: float
        hitbox: float
        estado: str
        animaciondent: int
        velocidadanimacion: float
        direccion: 
        velocidad: int
        ataque: boolean
        ataqueesp: None
        sw: int
        animaciones(ubicacionp: str, animacionp: dic, todopath: str)
		input(teclas: str, tiempoataque: float, ataque: boolean, direccion, estado: str, image, sw: int)
		estados(direccion, estado: str)
		move(velocidad: int, direccion: list, estado: str, rect, hitbox)
		espera(tiempoactual: float, ataque: boolean, tiempoataque: float)
		secuencia(animacion: str, animaciondent: int, velocidadanimacion: float, image:, hitbox: , todopath: str)
		colicion(direccion: , sprite: , obstacuolos: , hitbox: , )
		update(self)
		}
		
		class Main{
		pantalla: str
		frames: float
		nivel:
		run(pantalla:str, nievel:, FPS: int)
		}
		
		class Nivel{
		mostrars:
		spritev:
		obstaculos:
		crearmapa(layouts: dic, graphics: dic)
		run(spritev)
		}
		
		class YCamaraGrupo{
		mostrars:
		mitadancho:
		mitadlargo:
		offset:
		suelo_superficie:
		suelo_rect:
		custom_draw(self, jugador)
		
		class Soporte{
		impor_csv_layout(path: str)
		import_folder(path: str)
		}
		
		class Suelo{
		pos:
		grupos:
		sprite_type:
		surface:
		image:
		}
</code></pre>
	* <h5> Descripción general de los módulos </h5>
		* <b> Descripción general y propósito: </b>
		* <b> Responsabilidad y restricciones: </b>
		* <b> Dependencias: </b>
		* <b> Implementación: </b>
	* <h5> Dependencias externas </h5>
3. <h4> Diseño del modelo de datos </h4>
4. <h4> Descripción de proceso y servicios ofrecidos por el sistema </h4>
5. <h4> Documentación técnica </h4>
### Aspectos relevantes
### Herramientas 

*[POO]: Programación Orientada a Objetos
*[UML]: Lenguaje Unificado de Modelado
