package afdLib;

public class testAFD {

	public static void main(String[] args) {
		Node q0 = new Node("q0",false);
		Node q1 = new Node("q1",false);
		Node q2 = new Node("q2",false);
		Node q3 = new Node("q3",false);
		Node q4 = new Node("q4",false);
		Node q5 = new Node("q5",true);
		q5.addNode("aZ", q5);
		q5.addNode(".", q4);
		q4.addNode("aZ", q5);
		q3.addNode(".", q4);
		q3.addNode("aZ", q3);
		q2.addNode("aZ", q3);
		q1.addNode("@", q2);
		q1.addNode("aZ", q1);
		q0.addNode("aZ", q1);
		AFD automata = new AFD();
		automata.setStartNode(q0);
		String input = "debe@servir.com.net";
		System.out.println(automata.testString(input));

	}		

}
