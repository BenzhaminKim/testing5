package com.company;

import java.io.IOException;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;

public class ClientDemo {
	public static void main(String[] args) {
		String reqStr = "         BAS00201TN135170 0200UBIRQ 20000002018060417293000000000        201806040101                                                                           20180604155402         010858214118012131";
		String address = "127.0.0.1";
		String port = "8088";
		Socket socket = null;
		try {
			socket = new Socket(address, Integer.parseInt(port));
		} catch (NumberFormatException e) {
			System.out.println("Bad port format. Please enter a number.\n");
			System.exit(2);
		} catch (UnknownHostException e) {
			System.out.println("Cannot find the specified host. Please check host name...\n");
			System.exit(3);
		} catch (IOException e) {
			System.out.println(" >Cannot connect with server...");
			System.out.println(" >Please check if port number corresponds to port number in server...");
			System.out.println(" >Possibly server is not operating. Please try again later...\n");
			System.exit(4);
		} catch(IllegalArgumentException e) {
			System.out.println("Please enter a number between 0 and 65535 for the port.\n");
			System.exit(2);
		}
		
		try {
			OutputStream output = socket.getOutputStream();
			
			PrintWriter writer = new PrintWriter(output, true);
			writer.println("This is a message sent to the server");
			output.close();
			
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
