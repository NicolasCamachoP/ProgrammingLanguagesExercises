package afdLib;

import java.util.HashMap;
import java.util.Map;

public class Node {
	private String state;
	private Map<String,Node> neighbors;
	private boolean isFinal;
	
	public String getState() {
		return state;
	}
	public void setState(String state) {
		this.state = state;
	}
	public Map<String, Node> getNeighbors() {
		return neighbors;
	}
	public void setNeighbors(Map<String, Node> neighbors) {
		this.neighbors = neighbors;
	}
	public boolean isFinal() {
		return isFinal;
	}
	public void setFinal(boolean isFinal) {
		this.isFinal = isFinal;
	}
	
	public Node(String state, boolean isFinal) {
		this.state = state;
		this.isFinal = isFinal;
		this.neighbors = new HashMap<String, Node>();
	}
	
	public boolean addNode(String key, Node neighbor) {
		if(this.neighbors.get(key) == null) {
			this.neighbors.put(key, neighbor);
			return true;
		}
		return false;
	}
	
	public boolean process(String input) {
		int size = input.length();
		if (size >= 1) {
			char entry = input.charAt(0);
			if (entry == '@') {
				if(this.neighbors.get("@") != null)
					return this.neighbors.get("@").process(input.substring(1, size));
				else
					return false;
			}
			else if (entry == '.') {
				if(this.neighbors.get(".") != null)
					return this.neighbors.get(".").process(input.substring(1, size));
				else
					return false;
			}
			else if (Character.isLetter(entry)) {
				if(this.neighbors.get("aZ") != null)
					return this.neighbors.get("aZ").process(input.substring(1, size));
				else
					return false;
			}else if(Character.isDigit(entry)) {
				if(this.neighbors.get(1)!=null) 
					return this.neighbors.get(1).process(input.substring(1, size));
				else
					return false;
			}
		}else {
			return this.isFinal;
		}
		return false;
	}
	
	
}
