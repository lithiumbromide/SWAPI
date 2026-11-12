---
title: "Turn Cameras On and Off Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Turn_Cameras_On_and_Off_Example_CSharp.htm"
---

# Turn Cameras On and Off Example (C#)

This example shows how to turn cameras on and off.

```vb
 //----------------------------------------------------------------------------
 // Preconditions: Open a SOLIDWORKS Design model that contains at least one camera.
 //
 // Postconditions: The cameras are turned on and off.
 //----------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace CameraType_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         // Utility struct to combine the name and ID of a camera
         public struct Camera_t
         {
             public string Name;
             public int Id;
         }

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             ModelView swModelView = default(ModelView);
             Camera swCamera = default(Camera);
             int lNumCameras = 0;
             int lCameraId = 0;
             Feature swFeature = default(Feature);
             Camera_t[] aCameras = null;
             bool bValue = false;
             string sFeatureName = null;
             int lTypeOfCamera = 0;
             int lTypeOfCameraPosition = 0;

             // Get active document
             swModel = (ModelDoc2)swApp.ActiveDoc;

             // Get the active model view for the active document
             swModelView = (ModelView)swModel.ActiveView;

             // Check if a camera view is active
             swCamera = swModelView.Camera;

             Debug.Print("");

             if ((swCamera == null))
             {
                 Debug.Print("No active camera.");
             }
             else
             {
                 Debug.Print("Camera is active.");
                 Debug.Print("  Name = " + swCamera.ID);
             }

             // Turn off camera view
             swModelView.Camera = null;

             // Get the number of cameras
             lNumCameras = swModel.Extension.GetCameraCount();

             Debug.Print("");
             Debug.Print("Number of cameras = " + lNumCameras);

             aCameras = new Camera_t[lNumCameras];

             for (lCameraId = 0; lCameraId <= (lNumCameras - 1); lCameraId++)
             {
                 // Valid ID:
                 //  0 <= ID <= (ModelDocExtension::GetCameraCount - 1)
                 // IDs are reassigned if a camera is deleted
                 aCameras[lCameraId].Id = lCameraId;

                 // Get the camera
                 swCamera = swModel.Extension.GetCameraById(lCameraId);

                 // A camera is a feature
                 swFeature = (Feature)swCamera;

                 // Get the names of the feature and camera
                 sFeatureName = swFeature.Name;

                 aCameras[lCameraId].Name = sFeatureName;

                 Debug.Print("");
                 Debug.Print("Type of feature = " + swFeature.GetTypeName());
                 Debug.Print("Camera name = " + sFeatureName);

                 // Get the type of camera
                 lTypeOfCamera = swCamera.Type;

                 if ((lTypeOfCamera == 1))
                 {
                     Debug.Print("Type of camera = Aimed at target");
                 }
                 else
                 {
                     Debug.Print("Type of camera = Floating");
                 }

                 // Get the type of camera position
                 lTypeOfCameraPosition = swCamera.PositionType;

                 if ((lTypeOfCameraPosition == 1))
                 {
                     Debug.Print("Type of camera position = Cartesian");
                 }
                 else
                 {
                     Debug.Print("Type of camera position = Spherical");
                 }

             }

             // Now switch the view to each camera

             for (lCameraId = 0; lCameraId <= (lNumCameras - 1); lCameraId++)
             {
                 bValue = swModelView.SetCameraByName(aCameras[lCameraId].Name);

                 if ((bValue == false))
                 {
                     Debug.Print("Failed to set model view to use camera " + aCameras[lCameraId].Name);
                 }
                 else
                 {
                     Debug.Print("Model view set to use camera " + aCameras[lCameraId].Name);
                 }

                 swModelView.Camera =  null;

             }

         }

         public SldWorks swApp;

     }

 }
```
