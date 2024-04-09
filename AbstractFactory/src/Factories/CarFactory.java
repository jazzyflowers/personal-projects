package Factories;

import Componente.Assistant;
import Componente.Calendar;
import Componente.GPS;
import Componente.Messaging;
import Componente.Music;
import Componente.Podcast;


public abstract class CarFactory {
	public abstract Messaging creeazaMesagerie();
	public abstract Calendar creeazaCalendar();
	public abstract GPS creeazaGPS();
	public abstract Music creeazaMuzica();
	public abstract Assistant creeazaAsistent();
	public abstract Podcast creeazaPodcast();

}
