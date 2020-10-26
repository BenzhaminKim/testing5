package com.company;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class Main {

    public static void main(String[] args) throws SQLException, ClassNotFoundException {
	// write your code here
        String url;
        Connection con = null;
        try {
            Class.forName("com.mysql.jdbc.Driver");
            url="jdbc:mysql://localhost:3406/insurance_cp?useSSL=false&user=dev&password=secret";
            con = DriverManager.getConnection(url);
            System.out.println("Connection created");
            con.close();
            System.out.println("Connection closed");
        }
        catch (Exception e) {
            System.out.println(e.toString());
        }
    }
}
