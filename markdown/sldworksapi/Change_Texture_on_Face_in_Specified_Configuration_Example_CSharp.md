---
title: "Change Texture on Face in Specified Configuration Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Texture_on_Face_in_Specified_Configuration_Example_CSharp.htm"
---

# Change Texture on Face in Specified Configuration Example (C#)

This example shows how to change the texture on the selected face in the specified configuration.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Ensure the specified textures exist.
  // 2. Open a part or assembly with a Default configuration.
 // 3. Select a face.
 // 4. Open an Immediate window.
 //
 // Postconditions:
 // 1. Applies texture to the selected face.
 // 2. Inspect the Immediate window and the model.
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
 namespace ChangeTexture_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         SelectionMgr swSelMgr;
         ModelDocExtension swModelDocExt;
         Face2 face;
         Texture texture;
         bool boolstatus;
         string namStr;
         string configName;

         public void Main()
         {
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swModelDocExt = swModel.Extension;

             configName = "Default";

             face = (Face2)swSelMgr.GetSelectedObject6(1, -1);

             //Get existing texture on this face
             texture = face.GetTexture(configName);

             if ((texture != null))
             {
                 Debug.Print("Texture before:");
                 Debug.Print("Material: " + texture.MaterialName);
                 Debug.Print("Granularity: " + texture.ScaleFactor);
                 Debug.Print("Angle of rotation: " + texture.Angle);

                 //Change texture on this face
                 texture.Angle = 340;
                 texture.ScaleFactor = 25;
                 texture.MaterialName = "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\data\\Images\\textures\\plastic\\brushed\\bblue.jpg";
                 boolstatus = face.SetTexture(configName, texture);

                 Debug.Print("");
                 Debug.Print("Texture after:");
                 Debug.Print("Material: " + texture.MaterialName);
                 Debug.Print("Granularity: " + texture.ScaleFactor);
                 Debug.Print("Angle of rotation: " + texture.Angle);

             }
             else
             {
                 //If no texture exists on this face, then apply a texture to it
                 namStr = "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\data\\Images\\textures\\pattern\\checker2.jpg";
                 texture = swModelDocExt.CreateTexture(namStr, 5, 45, false);
                 boolstatus = face.SetTexture(configName, texture);

                 Debug.Print("New texture:");
                 Debug.Print("Material: " + texture.MaterialName);
                 Debug.Print("Granularity: " + texture.ScaleFactor);
                 Debug.Print("Angle of rotation: " + texture.Angle);

             }

             Debug.Print(texture.GetSystemTextureName(texture.MaterialName.ToString(), out boolstatus));

         }

         public SldWorks swApp;

     }
 }
```
