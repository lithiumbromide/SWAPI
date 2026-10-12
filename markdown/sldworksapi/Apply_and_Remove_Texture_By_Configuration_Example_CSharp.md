---
title: "Apply and Remove Texture Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Apply_and_Remove_Texture_By_Configuration_Example_CSharp.htm"
---

# Apply and Remove Texture Example (C#)

This example shows how to apply a texture to a face by display state and remove it by configuration.

```vb
 //---------------------------------------------------------------------------
 // Preconditions: Verify that the specified part to open exists.
 //
 // Postconditions:
 // 1. Opens the part and applies the texture to the selected face.
 // 2. Press F5 to continue running the macro.
 // 3. Examine the part to verify that the texture
 //    was removed from the Default configuration.
 //----------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 namespace RemoveTexture2_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         SelectionMgr swSelMgr;
         ModelDocExtension swModelDocExt;
         Face2 face;
         Texture texture;
         ModelView modelview;
         bool status;
         string displayState;
         int errors;
         int warnings;
         string namStr;

         int[] atIndex = new int[2];

         public void Main()
         {
             // Open the document and select a face
             swModel = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\SOLIDWORKS 2018\\samples\\tutorial\\api\\pplate.sldprt", (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
             swModelDocExt = swModel.Extension;

             status = swModelDocExt.SelectByID2("", "FACE", -0.02341747645642, 0.03900188771217, -0.008053400767039,  false, 0,  null, 0);

             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             face = (Face2)swSelMgr.GetSelectedObject6(1, -1);

             // Set the texture on the selected face in the specified display state
             displayState =  "<Default>_Display State 1";
             namStr = "<SystemTexture>\\images\\textures\\pattern\\checker2.jpg";
             texture = swModelDocExt.CreateTexture(namStr, 5, 45, false);
             status = face.SetTextureByDisplayState(displayState, texture);

             // Redraw the window view
             modelview = (ModelView)swModel.ActiveView;
             modelview.GraphicsRedraw(null);

             // Examine the selected face to verify that the specified texture was set
             // Press F5 to continue running macro

             System.Diagnostics.Debugger.Break();

             // Remove the texture from the face by the specified configuration
             status = swModelDocExt.SelectByID2("", "FACE", -0.02341747645642, 0.03900188771217, -0.008053400767039,  false, 0,  null, 0);
             face = (Face2)swSelMgr.GetSelectedObject6(1, -1);
             status = face.RemoveTexture2("Default");

             // Deselect the face to verify that the texture was removed
             atIndex[1] = 1;
             errors = swSelMgr.DeSelect2(atIndex, -1);

         }

         public SldWorks swApp;

     }
 }
```
