---
title: "Get and Set Scene Properties Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Scene_Properties_Example_CSharp.htm"
---

# Get and Set Scene Properties Example (C#)

This example shows how to get a model's scene and get and set some scene properties.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a model document.
 // 2. Open an Immediate window.
 //
 // Postconditions: Inspect the Immediate window.
  // ---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace Scene_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         SWScene Scene;
         ModelDoc2 swModel;
         Configuration swConfig;
         MathPoint swPoint;
         MathVector swVector;
         double[] point;
         double[] vect;

         public void Main()
         {
             swModel = (ModelDoc2)swApp.ActiveDoc;

             swConfig = (Configuration)swModel.GetActiveConfiguration();
             Debug.Print("Configuration: " + swConfig.Name);

             Scene = swConfig.GetScene();

             string P2SFilename = null;
             Scene.GetP2SFileName(ref P2SFilename);
             Debug.Print("Scene file: " + P2SFilename);

             Debug.Print("Scene background top gradient color: " + Scene.BackgroundTopGradientColor);
             Debug.Print("Scene background bottom gradient color: " + Scene.BackgroundBottomGradientColor);

             Scene.GetFloorNormal(ref swPoint, ref swVector);
             point = (double[])swPoint.ArrayData;
             Debug.Print("Scene floor normal point: " + point[0] + ", " + point[1] + ", " + point[2]);
             vect = (double[])swVector.ArrayData;
             Debug.Print("Scene floor normal vector: " + vect[0] + ", " + vect[1] + ", " + vect[2]);

             Scene.BackgroundType = (int)swSceneBackgroundType_e.swBackgroundType_UseEnvironment;
             Debug.Print("Type of scene background as defined in swSceneBackgroundType_e: " + Scene.BackgroundType);
             Debug.Print("Scene background environment image file: " + Scene.BackgroundEnvImage);
             Debug.Print("Scene background image file: " + Scene.BackgroundImage);
             Debug.Print("Scene environment rotation: " + Scene.EnvironmentRotation);
             Scene.FitToSWWindow = true;
             Debug.Print("Stretch to fit in SOLIDWORKS Design window? " + Scene.FitToSWWindow);
             Debug.Print("Scale the scene floor uniformly? " + Scene.FixedAspectRatio);
             Debug.Print("Flip the scene floor direction? " + Scene.FloorDirection);
             Debug.Print("Automatically resize the scene floor based on the model bounding box? " + Scene.FloorAutoSize);
             Debug.Print("Distance between scene floor and model: " + Scene.FloorOffset);
             Debug.Print("Flip the scene floor offset direction? " + Scene.FloorOffsetDirection);
             Scene.FloorReflections = true;
             Debug.Print("Show model reflections on the scene floor? " + Scene.FloorReflections);
             Debug.Print("Scene floor rotation: " + Scene.FloorRotation);
             Debug.Print("Show model shadows on the scene floor? " + Scene.FloorShadows);
             Debug.Print("Keep the scene background when changing the scene? " + Scene.KeepBackground);
             Scene.FlattenFloor = true;
             Debug.Print("Flatten the scene floor of the spherical environment? " + Scene.FlattenFloor);
             Debug.Print("Horizon height: " + Scene.HorizonHeight);
             Debug.Print("Environment size: " + Scene.EnvironmentSize);

         }

         public SldWorks swApp;

     }
 }
```
