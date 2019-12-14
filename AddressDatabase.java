/*
 * Jonathan Wright
 * CIS150-401
 * Address Database
 * Program to connect to a database and navigate its address records in a GUI
 */

package programs;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.HBox;
import javafx.scene.layout.Pane;
import javafx.scene.layout.BorderPane;
import javafx.scene.text.Text;
import javafx.stage.Stage;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;

public class AddressDatabase extends Application {
	
	// Creates ArrayList to store addresses
	ArrayList<Address> addresses = new ArrayList<Address>();
	
	// Record index
	int index = 0;
	
	// Method to connect to database and store its information in the ArrayList
	public void initializeDB() {
		
		// Try for connecting to and reading from MySQL database
		try {
            // Loading the JDBC driver
            Class.forName("com.mysql.jdbc.Driver");
 
            // Establish the connection to the database
            String url = "jdbc:mysql://localhost:3306/javabook";
            Connection conn = DriverManager.getConnection(url, "jonathan", "temppass");
            Statement st = conn.createStatement();
            ResultSet srs = st.executeQuery("SELECT * FROM address");
            while (srs.next()) {
            	// Reads from database and creates address object to store in ArrayList
                Address address = new Address();
                address.setName(srs.getString("name"));
                address.setStreet(srs.getString("street"));
                address.setCity(srs.getString("city"));
                address.setState(srs.getString("state"));
                address.setZipcode(srs.getString("zipcode"));
                addresses.add(address);
            }
        
        // Catch for try
        } catch (Exception e) {
            System.err.println("Could not connect to database");
            System.err.println(e.getMessage());
            System.exit(0);
        }
	}
	
	// Method to create and return pane to display in scene
	protected BorderPane getPane() {
		
		// Connects to the database and creates fills ArrayList
		initializeDB();
		
		// Creates main BorderPane and sets additional panes with padding
		BorderPane pane = new BorderPane();
		Pane pane1 = new Pane();
		Pane pane2 = new HBox(5);
		pane.setCenter(pane1);
		pane.setBottom(pane2);
		pane2.setPadding(new Insets(0, 20, 0, 20));
		
		// Adds Text lines displaying first record to pane
		Text text1 = new Text(225, 40, "ADDRESS RECORDS");
		Text text2 = new Text(210, 100, addresses.get(index).toString());
		Text text3 = new Text(210, 230, "Displaying record " + (index + 1) + " of " + addresses.size());
		pane1.getChildren().addAll(text1, text2, text3);
		
		// Creates the five buttons to navigate the records and quit the program
		Button first = new Button("First");
		Button previous = new Button("Previous");
		Button next = new Button("Next");
		Button last = new Button("Last");
		Button quit = new Button("Quit");
		
		// Sets styles for each button
		first.setPrefWidth(100);
        first.setStyle("-fx-font: 16 arial; -fx-base: LightGray");
        previous.setPrefWidth(100);
        previous.setStyle("-fx-font: 16 arial; -fx-base: LightGray");
        next.setPrefWidth(100);
        next.setStyle("-fx-font: 16 arial; -fx-base: LightGray");
        last.setPrefWidth(100);
        last.setStyle("-fx-font: 16 arial; -fx-base: LightGray");
        quit.setPrefWidth(100);
        quit.setStyle("-fx-font: 16 arial; -fx-base: LightGray");
		
        // Adds buttons to pane
		pane2.getChildren().addAll(first, previous, next, last, quit);
		
		// Sets to first record on button press
		first.setOnAction(e -> {
			if (index != 0) {
				index = 0;
				text2.setText(addresses.get(index).toString());
				text3.setText("Displaying record " + (index + 1) + " of " + addresses.size());
			}
		});
		
		// Sets to previous record on button press
		previous.setOnAction(e -> {
			if (index != 0) {
				index -= 1;
				text2.setText(addresses.get(index).toString());
				text3.setText("Displaying record " + (index + 1) + " of " + addresses.size());
			}
		});
		
		// Sets to next record on button press
		next.setOnAction(e -> {
			if (index != addresses.size() - 1) {
				index += 1;
				text2.setText(addresses.get(index).toString());
				text3.setText("Displaying record " + (index + 1) + " of " + addresses.size());
			}
		});
		
		// Sets to last record on button press
		last.setOnAction(e -> {
			if (index != addresses.size() - 1) {
				index = addresses.size() - 1;
				text2.setText(addresses.get(index).toString());
				text3.setText("Displaying record " + (index + 1) + " of " + addresses.size());
			}
		});
		
		// Quits program on button press
		quit.setOnAction(e -> System.exit(0));
		
		// Returns pane
		return pane;
	}
	
	// Overrides start method to create stage
	@Override
	public void start(Stage primaryStage) {
		
		// Gets pane for scene
		primaryStage.setScene(new Scene(getPane(), 550, 280));
		
		//Setup the stage
		primaryStage.setTitle("Address Database");
		primaryStage.setResizable(false);
		primaryStage.show();
		
		
	}
	
	// Main method to launch the program
	public static void main(String[] args) {
		launch(args);
	}
}
