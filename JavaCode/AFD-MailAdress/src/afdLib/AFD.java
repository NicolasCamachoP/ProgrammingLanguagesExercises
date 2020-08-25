package afdLib;

public class AFD {
	private Node startNode;
	
	public Node getStartNode() {
		return startNode;
	}

	public void setStartNode(Node startNode) {
		this.startNode = startNode;
	}

	public boolean testString(String input) {
		return startNode.process(input);
	}

}
