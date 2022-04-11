import java.util.Scanner;
import javax.crypto.*;

public class DES
{
	Cipher ecipher,dcipher;
	public static void main(String args[])
	{
		System.out.println("Enter any String :");
		Scanner sc=new Scanner(System.in);
		String input=sc.nextLine();
		try
		{
			KeyGenerator k=KeyGenerator.getInstance("DES");
			SecretKey key=k.generateKey();
			DES en=new DES(key);
			String ct=en.encrypt(input);
			String decrypted=en.decrypt(ct);
			
			System.out.println("Original string is:"+input);
			System.out.println("Encrypted string is : "+ct);
			System.out.println("Decrypted String is : "+decrypted);
			
		}
		catch(Exception e)
		{
			System.out.println(e);
		}

		sc.close();

	}
	public DES(SecretKey key)
	{
		try
		{
			ecipher=Cipher.getInstance("DES");
			ecipher.init(Cipher.ENCRYPT_MODE,key);
			dcipher=Cipher.getInstance("DES");
			dcipher.init(Cipher.DECRYPT_MODE,key);
		}
		catch(Exception e)
		{
			System.out.println(e);
		}
	}
	public String encrypt(String str)
	{
		
		try
		{
			byte[] b=str.getBytes();
			byte[] enc=ecipher.doFinal(b);
			return new String(enc);
		
		}
		catch(Exception e)
		{
			System.out.println(e);
		}
		return null;
		
	}
	public String decrypt(String str)
	{
		try
		{
			byte[] b=str.getBytes(); 
			byte[] dec=dcipher.doFinal(b);
			return new String(dec);
		
		}
		catch(Exception e)
		{
			System.out.println(e);
		}
		return null;
	}
}