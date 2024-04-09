package Main;

import Componente.Componenta;
import Componente.AndroidMessages;
import Componente.AppleCalendar;
import Componente.AppleMaps;
import Componente.AppleMusic;
import Componente.ApplePodcast;
import Componente.Assistant;
import Componente.Calendar;
import Componente.GPS;
import Componente.GoogleAssistant;
import Componente.GoogleCalendar;
import Componente.GoogleMaps;
import Componente.IMessage;
import Componente.Messaging;
import Componente.Music;
import Componente.PocketCasts;
import Componente.Podcast;
import Componente.Siri;
import Componente.Spotify;
import Factories.AppleCarPlayFactory;
import Factories.AndroidAutoFactory;
import Factories.CarFactory;

public class CarClient {
	public static void main(String[] args) {
		AppleCarPlayFactory AppleCarPlay = new AppleCarPlayFactory();
		AppleMaps appleMaps = AppleCarPlay.creeazaGPS();
		IMessage iMessage = AppleCarPlay.creeazaMesagerie();
		Siri siri = AppleCarPlay.creeazaAsistent();
		ApplePodcast applePodcast = AppleCarPlay.creeazaPodcast();
		AppleCalendar appleCalendar = AppleCarPlay.creeazaCalendar();
		AppleMusic appleMusic = AppleCarPlay.creeazaMuzica();

		AndroidAutoFactory AndroidAuto = new AndroidAutoFactory();
		GoogleMaps googleMaps = AndroidAuto.creeazaGPS();
		AndroidMessages androidMessages = AndroidAuto.creeazaMesagerie();
		GoogleCalendar googleCalendar = AndroidAuto.creeazaCalendar();
		GoogleAssistant googleAssistant = AndroidAuto.creeazaAsistent();
		PocketCasts pocketCasts = AndroidAuto.creeazaPodcast();
		Spotify spotify = AndroidAuto.creeazaMuzica();

//           googleMaps.creeazaComponenta();
//           appleMaps.creeazaComponenta();

	}
}
