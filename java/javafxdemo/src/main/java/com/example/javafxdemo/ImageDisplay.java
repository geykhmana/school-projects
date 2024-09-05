package com.example.javafxdemo;

import javafx.application.Application;
import javafx.geometry.Rectangle2D;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;

public class ImageDisplay extends Application {
	public void start(Stage primaryStage) {
		Image img = new Image("E://Projects//Java//GUIDesign//index.png");
		ImageView imgView=new ImageView(img);
		
		StackPane pane=new StackPane(imgView);
		pane.setStyle("-fx-background-color: cornsilk");
		
		Scene scene = new Scene(pane,500,300);
		
		primaryStage.setScene(scene);
		primaryStage.show();
	}
	public static void main(String[] args) {
		launch(args);
	}
}
