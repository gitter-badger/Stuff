import java.awt.Toolkit;
import java.awt.datatransfer.DataFlavor;
import java.awt.datatransfer.Transferable;
import java.awt.image.BufferedImage;
import java.io.File;
import javax.imageio.ImageIO;

public class ClipImage {

    public static void main(String[] args) throws Exception {
        Transferable t = Toolkit.getDefaultToolkit().getSystemClipboard().getContents(null);
        BufferedImage image = (BufferedImage) t.getTransferData(DataFlavor.imageFlavor);
        String name = Integer.toHexString((int) (System.currentTimeMillis() / 1000L)) + ".png";
        ImageIO.write(image, "png", new File(name));
        System.out.println(name);
    }
}