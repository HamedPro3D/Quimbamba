<center> <h2> Proyecto Final </h2> 
**Integrante 1, *** Integrante 2

** Estudiante de Ingeniería Chanel Naomi Olier Watson, Código: 200110086 

*** Estudiante de Ingeniería Hamed J. Elneser Tejeda, Código: 200097207 

<b>Profesor:</b> Pedro Jose D. Posada Aguilar 

Programación Orientada a Objetos 

Fecha (17-11-22) 

Barranquilla-Colombia 
</center>

### **Estructura y contenido**

1. #### **Definiciones y especificación de requerimientos**
	*  <h5> Definición general del proyecto de software </h5> <p class=text-align-justify>Quimbamba es un juego 2D tipo Souls-like de acción y aventura. Inspirado en el famoso juego Zelda buscando crear un juego de alta dificultad que para los amantes de los clásicos 2D. </p>
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


	* ##### Procedimientos
		* **procedimientos de desarrollo:** 
			* **Herramientas utilizadas:<p class=text-align-justify>** Para la creación del programa se utilizó una variedad de herramientas, las cuales son: 
				  * **Visual Studio Code:** Un editor de código, en donde se escribió todo el código del programa.
			    * **Tiled:** Es un editor de mapas con en cual se diseñó el mapa del juego.
			    * **Craftpix.net:** Pagina que dispone recursos gráficos premiums y de libre uso. 
			    * **Aseprite:** Es un editor de gráficos rasterizados, con el cual se diseñaron los sprites del  juego; como los personajes, enemigos y otros.
			    * **Adobe Illustrator:** Es un editor de gráficos vectoriales con el cual se editaron los sprites del juego.</p>
			* **Planificación:** <p class=text-align-justify> El proceso de codificación del programa bastante educativo, ya que nos obligó a ir más allá de nuestros conocimientos previos. No está de más decir que no se sabia por donde empezar y al hacerlo habían muchos errores que no se sabían solucionar. También se tuvo que aprender ha hacer una cámara, una inteligencia artificial y a manjar el módulo de Python pymage.</p>
		* **Procedimientos de instalación y prueba:** 
			* **Requisitos no funcionales:**
				* Buen rendimiento
				* Cero bugs
			* **Especificaciones de prueba y ejecución:** 

			<p class=text-align-justify> Para este proyecto no se creará ejecutable por lo que el programa correrá directamente del editor de código VSC. EL interprete será el lenguaje de programación  <em><b>Python v3.10.7</b></em> </p>
2. #### Arquitectura del sistema
	* <h5> Descripción jerárquica </h5> <p class=text-align-justify> El programa se encuentra organizado por módulos de Python bajo el modelo <u>POO</u>. Por lo que agrupa una colección de objetos de la misma estructura para conformar una clase, siendo así cada objeto una instancia de su clase. </p>
	* <h5> Diagrama de módulos (UML) </h5>
		* <b> Imagen del UML </b>
		
		[UML_Quimbamba](https://github.com/HamedPro3D/Quimbamba/blob/2908d8725c81ee489447c97c70311d9617feacd4/UML/UML__Quimbamba-Actualizado.png)
		
		![UML__Quimbamba](https://github.com/HamedPro3D/Quimbamba/blob/2908d8725c81ee489447c97c70311d9617feacd4/UML/UML__Quimbamba-Actualizado.png?raw=true)
		* <b> Codigo del UML </b>
		<pre>
			@startuml Quimbamba
		    Title Diagrama UML de Quimbamba
		    class Ajustes #lightgreen;line:darkgreen{
		    Largo:int
		    Ancho:int
		    FPS:int
		    TILESIZE:int
		    alturavida:int
		    anchovida:int
		    anchobarraenergia:int
		    tamañocorazon:int
		    ubicacion:str
		    tamañofuente:int
		    WORLD_MAP:str
		    }
		    
		    class Armas #lightgreen;line:darkgreen{
		    jugador:int
		    image:str
		    grupos:float
		    }
		    
		    class Debug #lightgreen;line:darkgreen{
		    font:str
		    debug(info,y:int,x:int)
		    }
		    
		    class Enemigos #lightgreen;line:darkgreen{
		    nombremoustro:
		    pos:float
		    grupos:float
		    obstaculos:str
		    estado:int
		    image:str
		    rect:int
		    hitbox:int
		    nombremoustro:str
		    moustroinfo:str
		    vida:int
		    xp:int
		    velocidad:int
		    daño:int
		    resistencia:int
		    radioataque:int
		    deteccion:int
		    tipo:int
		    puedeatacar:Boolean
		    tiempoataque:int
		    esperaataque:int
		    importargraficos(name:str)
		    get_player_distance_direction(player)
		    tomarestado(jugador:int)
		    acciones(jugador:int)
		    animacion()
		    esperaataques()
		    update()
		    actualizacionenemigos(jugador:int)
		    }
		    
		    class Entidad #lightgreen;line:darkgreen{
		    grupos:float
		    framesi:int
		    animacionv:float
		    direccion:int
		    move(velovidad:int)
		    colision(direccion:int)
		    }
		    
		    class Estadisticas #lightgreen;line:darkgreen{
		    mostrars:str
		    font:(str,int)
		    tamañobarravida:int
		    tamañobarraenergia:int
		    mostrarbarra(actual:int, maximo:int, cuadrotrasero:int, color:str)
		    mostrarexperiencia(xp:int)
		    display(jugador:int)
		    }
		    
		    class Magia #lightgreen;line:darkgreen{
		    jugador:int
		    grupos:float
		    image:str
		    }
		    
		    class Jugador #lightgreen;line:darkgreen{
		    pos:float
		    grupos:float
		    obstaculos:str
		    image:str
		    rect:int
		    hitbox:int
		    estado:int
		    animaciondent:int
		    velocidadanimacion:float
		    direccion:int
		    velocidad:int
		    ataque: boolean
		    ataqueesp:int
		    sw:int
		    atacar:str
		    magia:str
		    estadisticas:int
		    vida:float
		    energia:float
		    xp:int
		    velocidad:int
		    animaciones()
		    input()
		    estados()
		    move(velocidad:int)
		    espera()
		    secuencia()
		    colicion(direccion:int )
		    update()
		    }
		            
		    class Main #lightgreen;line:darkgreen{
		    pantalla:str
		    frames:float
		    run()
		    }
		    
		    class Nivel #lightgreen;line:darkgreen{
		    mostrars:str
		    spritev:str
		    obstaculos: str
		    ataqueactual:int
		    spritesataque:str
		    spritesataqueenemigos:str
		    stats:int
		    crearmapa()
		    atacar()
		    magia()
		    logicaataquesp()
		    run()
		    
		    }
		    
		    class YCamaraGrupo #lightgreen;line:darkgreen{
		    mostrars:int
		    mitadancho:int
		    mitadlargo:int
		    offset:int
		    suelo_superficie: str
		    suelo_rect:int
		    custom_draw(jugador:int)
		    actualizacionenemigo(jugdor:int)
		    }
		    
		    class Soporte #lightgreen;line:darkgreen{
		    import_csv_layout(path:str)
		    import_folder(path:str)
		    }
		    
		    class Suelo #lightgreen;line:darkgreen{
		    pos:int
		    grupos:float
		    sprite_type:str
		    surface:str
		    image:int
		    }
		    
		    Ajustes " 1 " <--* "    1 " Main
		    Nivel--* " 1 "Main
		    Debug " * "-- "       1   "Main
		    Jugador " * " --> " 1 " Ajustes
		    Jugador " * " *-- " * "Soporte
		    Magia" * "--* " * "Jugador
		    Armas" * "--* " * "Jugador
		    Enemigos " * "--> " 1 "Ajustes
		    Enemigos " * " *-- " * " Soporte
		    Enemigos " * " *-- " * " Entidad
		    Nivel " * "--> " 1 "Ajustes
		    Nivel " * "--* " * "Jugador
		    Nivel " * "-- " * "Debug
		    Nivel " * "-- " * " Estadisticas
		    Nivel " * "-- " * "Magia
		    Nivel " * "-- " * "Enemigos
		    Nivel " * "*-- " * "Suelo
		    Nivel " * " *-- " * " Soporte
		    Nivel " * " *-- YCamaraGrupo: compone
		    Suelo " * " *--> " 1 " Ajustes
		</code></pre>
	* <h5> Descripción individual de los módulos </h5>

		* <b> Descripción general y propósito:</b>
			* <p class=text-align-justify> <b> Módulo Ajustes: </b> Se encarga de administrar las variables fijas que necesita el programa.</p>
			* <p class=text-align-justify> <b> Módulo Armas: </b> Se encarga de cargar las imágenes del arma según el estado del jugador.</p>
			* <p class=text-align-justify> <b> Módulo Debug: </b> Se encarga de depurar el programa para saber si los comandos se están ejecutando correctamente, en este caso nos los muestra tanto en pantalla como en consola.</p>
			* <p class=text-align-justify> <b> Módulo Enemigos: </b> Controla los enemigos que esta el el mapa. Tiene una pequeña IA que hace que el monstruo persiga al jugador según su ubicación cuando el jugador entra en un radio determinado.</p>
			* <p class=text-align-justify> <b> Módulo Entidad: </b> Controla las colisiones de los enemigos.</p>
			* <p class=text-align-justify> <b> Módulo  Estadisticas: </b> Crea y dibuja la barra de estadísticas (vida y experiencia) del personaje.</p>
			* <p class=text-align-justify> <b> Módulo Jugador: </b> Se encarga de todo lo relacionado con el jugador, lo que es dibujarlo, procesar los estados, las animaciones, las transformaciones y su movimiento.</p>
			* <p class=text-align-justify> <b> Módulo Magia:</b> Tiene una función similar al módulo arma solo que este es el encargado de cargar las imágenes del poder mágico según el estado del jugador</p>
			* <p class=text-align-justify> <b> Módulo Main: </b> Es el encargado de correr el programa llamando a las otras clases.</p>
			* <p class=text-align-justify> <b> Módulo Nivel: </b> Crea el mapa especifico del nivel con los aspectos gráficos visuales (las imágenes del los objetos y el suelo) y los no visuales (los box de colisiones). También Procesa los ataques del jugador para saber que debe borrar de pantalla. Tiene una clase llamada YCamaraGrupo la cual es la cámara que sigue al jugador</p>
			* <p class=text-align-justify> <b> Módulo Soporte: </b> Se encarga de gestionar los CSV del mapa, objetos y colisiones.</p>
			* <p class=text-align-justify> <b> Módulo suelo: </b> Se encarga de procesar la imagen del suelo.</p>
		* <b> Responsabilidad y restricciones:</b> <p class=text-align-justify> </p>

			* <p class=text-align-justify> <b> Módulo Armas: </b> </p> 
				* módulo pygame
				* módulo Jugador
			* <p class=text-align-justify> <b> Módulo Debug: </b> </p>
				* módulo pygame
			* <p class=text-align-justify> <b> Módulo Enemigos: </b></p>
				* módulo pygame
				* módulo Ajustes
				* módulo Entidad -> clase Entidades
				* módulo Soporte
			* <p class=text-align-justify> <b> Módulo Entidad: </b> </p>
				* módulo pygame
			* <p class=text-align-justify> <b> Módulo  Estadisticas: </b> </p>
				* módulo pygame
				* módulo Ajustes
			* <p class=text-align-justify> <b> Módulo Jugador: </b> </p>
				* módulo pygame
				* módulo Ajustes
				* módulo Entidad -> clase Entidades
			* <p class=text-align-justify> <b> Módulo Magia:</b> </p>
				* módulo pygame
				* módulo Jugado
			* <p class=text-align-justify> <b> Módulo Main: </b> </p>
				* módulo pygame
				* módulo sys
				* módulo Nivel
			* <p class=text-align-justify> <b> Módulo Nivel: </b> </p>
				* módulo pygame
				* módulo random
				* módulo Ajustes
				* módulo Soporte
				* módulo suelo -> clase piso
				* módulo Jugador->clase Jugador
				* módulo Debug->función debug
				* módulo Armas->clase arma
				* módulo Magia->clase Magia
				* módulo Estadisticas->clase stats
				* módulo Enemigos->clase enemigo
			* <p class=text-align-justify> <b> Módulo Soporte: </b> </p>
				* módulo csv->función reader
				* módulo os->función walk
			* <p class=text-align-justify> <b> Módulo suelo: </b> </p>
				* módulo pygame
				* módulo Ajuses
		

<h4> Repositorio de GitHub </h4>

[Quimbamba](https://github.com/HamedPro3D/Quimbamba)
	 


*[POO]: Programación Orientada a Objetos
*[UML]: Lenguaje Unificado de Modelado
*[VSC]: Visual Studio Code
