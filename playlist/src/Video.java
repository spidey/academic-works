import java.lang.String;

public class Video extends Media
{
    private String subject_;
    private String channel_;
    private int views_;

    private Video() // disable default constructor
    {
        /*
         * Force compilation referencing the non default constructor of the
         * super class. If it explicitly calls super passing parameters, the
         * default constructor won't be used.
         */
        super("", 0);
    }

    public Video(String title, String subject, String channel, int views,
            int length)
    {
        super(title, length);
        subject_ = subject;
        channel_ = channel;
        views_ = views;
    }

    public String getSubject()
    {
        return subject_;
    }

    public String getChannel()
    {
        return channel_;
    }

    public int getViews()
    {
        return views_;
    }

    @Override
    public int getLength()
    {
        int length = length_;

        if (views_ >= 10000)
        {
            length += (5 * length_) / 100;
        }
        else if (views_ >= 1000)
        {
            length += (2 * length_) / 100;
        }

        return length;
    }
}
