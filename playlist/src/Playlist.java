import java.lang.String;
import java.lang.System;

public class Playlist
{
    private static final int MAX_MEDIA = 100;
    private static final int MINUTES_IN_HOUR = 60;

    private Media[] media_;
    private int count_;

    public Playlist()
    {
        media_ = new Media[MAX_MEDIA];
        count_ = 0;
    }

    public void addMedia(Media media)
    {
        media_[count_] = media;
        ++count_;
    }

    public int getLength()
    {
        int length = 0;

        for (int i = 0; i < count_; ++i)
        {
            length += media_[i].getLength();
        }

        return length;
    }

    public String toString()
    {
        int length = getLength();
        int hours = length / MINUTES_IN_HOUR;
        int minutes = length % MINUTES_IN_HOUR;

        String result = "";
        if (hours > 0)
        {
            result = hours + "h";
        }
        if (minutes > 0)
        {
            if (hours > 0)
            {
                result += " e ";
            }
            result += minutes + "min";
        }

        return result;
    }

    public static void main(String args[])
    {
        Playlist playlist = new Playlist();

        Song song1 = new Song("Agua de beber", "Astrud Gilberto", "Antonio Carlos Jobim", 140);
        Song song2 = new Song("O mar serenou", "Clara Nunes", "Candeia", 179);
        Song song3 = new Song("Rapaz Folgado", "Martinho da Vila e Mart'nália", "Noel Rosa", 180);
        playlist.addMedia(song1);
        playlist.addMedia(song2);
        playlist.addMedia(song3);

        Video video1 = new Video("Despacito", "Musica", "Luis Fonsi", 5926796, 280);
        Video video2 = new Video("Gangnam Style", "Musica", "Officialpsy", 3276192, 252);
        playlist.addMedia(video1);
        playlist.addMedia(video2);

        System.out.println("Playlist total length = " + playlist);
    }
}
