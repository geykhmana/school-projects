package com.example.javafxdemo;

import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.stage.Stage;

//************************************************************************
//� StyleOptions.java � � � Author: Lewis/Loftus
//
//� Demonstrates the use of check boxes.
//************************************************************************

public class StyleOptions extends Application {

	public void start(Stage primaryStage) {
		StyleOptionsPane pane = new StyleOptionsPane();
		pane.setAlignment(Pos.CENTER);
		pane.setStyle("-fx-background-color: skyblue");
		
		Scene scene = new Scene(pane, 400, 150);
		
		primaryStage.setTitle("Style Options");
		primaryStage.setScene(scene);
		primaryStage.show();
	}
	public static void main(String[] args) {
		launch(args);
	}
}