import java.lang.String;

public class Media
{
    protected String title_;
    protected int length_;

    public Media(String title, int length)
    {
        title_ = title;
        length_ = length;
    }

    private Media() {} // disable default constructor

    public String getTitle()
    {
        return title_;
    }

    public int getLength()
    {
        return length_;
    }
}
