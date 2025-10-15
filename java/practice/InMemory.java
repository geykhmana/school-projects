import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class InMemory {
    public static void main(String[] args) {
        try {
            Connection conn = DriverManager.getConnection("jdbc:h2:mem:testdb;DB_CLOSE_DELAY=-1");

            conn.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
