package Factories;

import Componente.AppleCalendar;
import Componente.AppleMaps;
import Componente.AppleMusic;
import Componente.ApplePodcast;
import Componente.IMessage;
import Componente.Siri;

public class AppleCarPlayFactory extends CarFactory {
	@Override
	public AppleMaps creeazaGPS(){
	        return new AppleMaps();
	    }
	@Override
	    public AppleMusic creeazaMuzica() {
	        return new AppleMusic();
	    }
	@Override
	    public IMessage creeazaMesagerie() {
	        return new IMessage();
	    }
	@Override
	    public Siri creeazaAsistent() {
	        return new Siri();
	    }
	@Override
	    public ApplePodcast creeazaPodcast() {
	        return new ApplePodcast();
	    }
	@Override
	    public AppleCalendar creeazaCalendar() {
	        return new AppleCalendar();
	    }
}
