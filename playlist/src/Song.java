import java.lang.String;

public class Song extends Media
{
    private String singer_;
    private String composer_;

    private Song() // disable default constructor
    {
        /*
         * Force compilation referencing the non default constructor of the
         * super class. If it explicitly calls super passing parameters, the
         * default constructor won't be used.
         */
        super("", 0);
    }

    public Song(String title, String singer, String composer, int length)
    {
        super(title, length);
        singer_ = singer;
        composer_ = composer;
    }

    public String getSinger()
    {
        return singer_;
    }

    public String getComposer()
    {
        return composer_;
    }
}
