package com.example.javafxdemo;

import java.util.Random;
import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;
public class Boxes extends Application {
	public void start(Stage primaryStage) {
		Group root = new Group();
		Random gen = new Random();
		for (int count = 1; count <= 50; count++) {
			int x = gen.nextInt(350) + 1;
			int y = gen.nextInt(350) + 1;
			
			int width = gen.nextInt(50) + 1;
			int height = gen.nextInt(50) + 1;
			
			Color fill = null;
			if (width < 10)
				fill = Color.YELLOW;
			else if (height < 10)
				fill = Color.GREEN;
			
			Rectangle box = new Rectangle(x, y, width, height);
			box.setStroke(Color.WHITE);
			box.setFill(fill);
			
			root.getChildren().add(box);
		}
		Scene scene = new Scene(root, 400, 400, Color.BLACK);
		primaryStage.setTitle("Boxes");
		primaryStage.setScene(scene);
		primaryStage.show();
	}
	public static void main(String[] args) {
		launch(args);
	}
}
