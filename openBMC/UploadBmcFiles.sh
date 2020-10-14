#!/bin/bash

# Warn user of JavaFX dependency
echo "WARNING: JavaFX needs to be installed for this application to run"
echo "Get JavaFX here: https://gluonhq.com/products/javafx/"
echo "Unzip to the same folder as the UploadBmcFiles.jar app"

java --module-path javafx-sdk-*/lib --add-modules javafx.controls -jar UploadBmcFiles.jar
