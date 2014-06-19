package javatokens;

import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;

public class Main {

    public static String generateToken(String urlPath, String secretKey) throws NoSuchAlgorithmException
    {
        try {
            Mac mac = Mac.getInstance("HmacSHA1");
            SecretKeySpec secret = new SecretKeySpec(secretKey.getBytes(), "HmacSHA1");
            mac.init(secret);
            byte[] digest = mac.doFinal(urlPath.getBytes());
            String enc = new String(digest);

            StringBuilder bldr = new StringBuilder();
            for (int i = 0; i < 10; i++) {
                bldr.append(String.format("%02x", digest[i]));
            }
            return bldr.toString();
        } catch (InvalidKeyException ex) {
            Logger.getLogger(Main.class.getName()).log(Level.SEVERE, null, ex);
            return "";
        }
    }

    public static String makeUrlWithToken(String urlPath, String secretKey)
    {
        try {
            if (urlPath.contains("?"))
                return urlPath + "&encoded=0" + generateToken(urlPath, secretKey);
            else
                return urlPath + "?encoded=0" + generateToken(urlPath, secretKey);
        } catch (NoSuchAlgorithmException ex) {
            Logger.getLogger(Main.class.getName()).log(Level.SEVERE, null, ex);
            return "";
        }
    }
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        String secret = "aMSyStRoHpHVMflazeGefCofoKoRvDcalsdfkjEuRkbNDhOoekekuFNaMWaYrnprhfm";
        String path = "/path/to/resource?sessionid=12345&misc=abcde&stime=20081201060100&etime=20201201060100";
        String expected = "/path/to/resource?sessionid=12345&misc=abcde&stime=20081201060100&etime=20201201060100&encoded=051e88c0261c6a4d83dbc";

        String tokenized = makeUrlWithToken(path, secret);

        System.out.println("Original URL path:  " + path);
        System.out.println("Secret:             " + secret);
        System.out.println("Tokenized URL path: " + tokenized);
        System.out.println("Expected outcome:   " + expected);
    }

}
