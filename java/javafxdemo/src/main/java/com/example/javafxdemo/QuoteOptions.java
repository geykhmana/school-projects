package com.example.javafxdemo;

import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class QuoteOptions extends Application {
	public void start(Stage primaryStage) {
		QuoteOptionsPane pane = new QuoteOptionsPane();
		pane.setAlignment(Pos.CENTER);
		pane.setStyle("-fx-background-color: lightgreen");
		
		Scene scene = new Scene(pane, 500, 150);
		
		primaryStage.setTitle("Quote Options");
		primaryStage.setScene(scene);
		primaryStage.show();
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		launch(args);
	}

}
