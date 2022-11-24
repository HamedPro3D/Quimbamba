## **Descripción general y propósito:**
* <p class=text-align-justify> <b> Módulo Ajustes: </b> Se encarga de administrar las variables fijas que necesita el programa.</p>
* <p class=text-align-justify> <b> Módulo Armas: </b> Se encarga de cargar las imagenes del arma según el estado del jugador.</p>
* <p class=text-align-justify> <b> Módulo Debug: </b> </p>
* <p class=text-align-justify> <b> Módulo Enemigos: </b> Contola los enemigos que esta el el mapa. Tiene una paqueña ia que hace que el monstruo persiga al jugador según su ubicación cuando el jugador entra en un radio determinado.</p>
* <p class=text-align-justify> <b> Módulo Entidad: </b> Controla las coliciones de los enemigos.</p>
* <p class=text-align-justify> <b> Módulo  Estadisticas: </b> Crea y dibuja la barra de estadisticas (vida y experiencia) del personaje.</p>
* <p class=text-align-justify> <b> Módulo Jugador: </b> Se encarga de todo lo relacionado con el jugador, lo que es dibujarlo, procesar los estados, las animaciones y las transformaciones.</p>
* <p class=text-align-justify> <b> Módulo Magia:</b> Tiene una función similar al módulo arma solo que este es el encargado de cargar las imagenes del poder magico según el estado del jugador</p>
* <p class=text-align-justify> <b> Módulo Main: </b> Es el encargado de correr el programa llamando a las otras clases.</p>
* <p class=text-align-justify> <b> Módulo Nivel: </b> Crea el mapa especifico del nivel con los aspectos graficos visuales (las imagenes del los objetos y el suelo) y los no visuales (los box de colisiones). Tambien Procesa los ataques del jugador para saber que debe borrar de pantalla. Tiene una clase llamada YCamaraGrupo la cual es la camara que sigue al jugador</p>
* <p class=text-align-justify> <b> Módulo Soporte: </b> Se encarga de gestionar los CSV del mapa, objetos y coliciones pasando los dados a dos listas</p>
* <p class=text-align-justify> <b> Módulo suelo: </b> </p>

## <b> Responsabilidad y restricciones:</b> <p class=text-align-justify> </p>

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
* <p class=text-align-justify> <b> Módulo Entidad: </b> 
	* módulo pygame</p>
* <p class=text-align-justify> <b> Módulo  Estadisticas: </b> 	
	* módulo pygame
	* módulo Ajustes</p>
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