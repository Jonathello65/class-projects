/*
 * Jonathan Wright
 * CIS150-401
 * Address Object
 * Creates object to store information of an address
 */

package programs;

public class Address {

	// Properties of an address
	private String name;
	private String street;
	private String city;
	private String state;
	private String zipcode;
	
	// No arg constructor for address
	public Address() {
		this.name = "";
		this.street = "";
		this.city = "";
		this.state = "";
		this.zipcode = "";
	}
	
	// Address constructor taking all parameters
	public Address(String name, String street, String city, String state, String zipcode) {
		this.name = name;
		this.street = street;
		this.city = city;
		this.state = state;
		this.zipcode = zipcode;
	}
	
	// Getter for name
	public String getName() {
		return name;
	}
	
	// Setter for name
	public void setName(String name) {
		this.name = name;
	}
	
	// Getter for street
	public String getStreet() {
		return street;
	}
	
	// Setter for street
	public void setStreet(String street) {
		this.street = street;
	}
	
	// Getter for city
	public String getCity() {
		return city;
	}
	
	// Setter for city
	public void setCity(String city) {
		this.city = city;
	}
	
	// Getter for state
	public String getState() {
		return state;
	}
	
	// Setter for state
	public void setState(String state) {
		this.state = state;
	}
	
	// Getter for zipcode
	public String getZipcode() {
		return zipcode;
	}
	
	// Setter for zipcode
	public void setZipcode(String zipcode) {
		this.zipcode = zipcode;
	}
	
	@Override
	public String toString() {
		return ("Name:  " + name + "\nStreet:  " + street + 
				"\nCity:  " + city + "\nState:  " + state + "\nZipcode:  " + zipcode);
	}
}
