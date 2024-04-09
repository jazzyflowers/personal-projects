package Factories;

import Componente.AndroidMessages;
import Componente.GoogleAssistant;
import Componente.GoogleCalendar;
import Componente.GoogleMaps;
import Componente.Messaging;
import Componente.PocketCasts;
import Componente.Spotify;

public class AndroidAutoFactory extends CarFactory {
	
	@Override
	public AndroidMessages creeazaMesagerie(){
		return new AndroidMessages();
	}
	@Override
	public GoogleCalendar creeazaCalendar(){
		return new GoogleCalendar();
	}
	@Override
	public GoogleAssistant creeazaAsistent(){
		return new GoogleAssistant();
	}
	@Override
	public GoogleMaps creeazaGPS(){
		return new GoogleMaps();
	}
	@Override
	public PocketCasts creeazaPodcast(){
		return new PocketCasts();
	}
	@Override
	public Spotify creeazaMuzica(){
		return new Spotify();
	}
}
