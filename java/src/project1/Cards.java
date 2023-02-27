package project1;

public class Cards {
    public static void main(String[] args) {
        enum Rank {
            ace,
            two,
            three,
            four,
            five,
            six,
            seven,
            eight,
            nine,
            ten,
            jack,
            queen,
            king,
        }
        Rank highCard = Rank.ace;
        Rank faceCard = Rank.king;
        Rank card1 = Rank.seven;
        Rank card2 = Rank.three;
        System.out.println("A blackjack hand: " + highCard + " and " + faceCard);
        int card1Val = card1.ordinal() + 1;
        int card2Val = card2.ordinal() + 1;
        System.out.println("A two card hand: " + card1 + " and " + card2);
        System.out.println("Hand value: " + (card1Val+card2Val));
    }
}
