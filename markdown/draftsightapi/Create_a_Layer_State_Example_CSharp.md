---
title: "Create a Layer State Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_a_Layer_State_Example_CSharp.htm"
---

# Create a Layer State Example (C#)

This example shows how to create a Layer state and get one of its stored Layer's properties.

```vb
  //-------------------------------------------------------------
 // Preconditions:
 // 1. Create a C# Windows console project.
 // 2. Copy and paste this project into the C# IDE.
 // 3. Add a reference to:
 //    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
 // 4. Open the Immediate window.
 // 5. Start DraftSight.
 // 6. Ensure the specified document to open exists.
 // 7. Click Start.
 //
 // Postconditions:
 // 1. Specified document is opened.
 // 2. A layer state is created.
 // 3. Properties of the stored Layer, Object, are printed out.
  //------------------------------------------------------------

 using System.IO;
 using DraftSight.Interop.dsAutomation;
 using System.Diagnostics;
 using System.Runtime.InteropServices;

 namespace CreateLayerState_CSharp
 {
     static class Program
     {

         public static void Main()
         {
             DraftSight.Interop.dsAutomation.Application dsApp;
             //Connect to DraftSight application
             dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");
             //Abort any command currently running in DraftSight
             //to avoid nested commands
             dsApp.AbortRunningCommand();

             //Open document
             Document dsDoc = default(Document);
             string docName = null;
             docName = "C:\\ProgramData\\Dassault Systemes\\DraftSight\\Examples\\B-44563.DWG";
             dsDoc = dsApp.OpenDocument2(docName, dsDocumentOpenOption_e.dsDocumentOpen_Default, dsEncoding_e.dsEncoding_Default);
             if (dsDoc == null)
             {
                 Debug.Print("Specified document did not open. Check path and file name.");
                 return;
             }

             //Create a Layer state and get one of its Layer's properties
             LayerStateManager dsLayerStateMgr = default(LayerStateManager);
             LayerState dsLayerState = default(LayerState);
             LayerProperties dsLayerStateProperties = default(LayerProperties);

             int iStatus = 0;
             dsLayerStateMgr = dsDoc.GetLayerStateManager();
             iStatus = dsLayerStateMgr.CreateLayerState("LSName", (int)dsLayerStateSpaceType_e.dsLayerStateSpaceType_Model, out dsLayerState);

             dsLayerState.Activate();

             Debug.Print("Layer state: " + dsLayerState.Name);
             Debug.Print("Description: " + dsLayerState.Description);
             Debug.Print("Space as defined in dsLayerStateSpaceType_e: " + dsLayerState.Space);
             Debug.Print("Save Visibility in active Viewport? " + dsLayerState.ActiveViewPortVisibility);
             Debug.Print("Save Freeze/Thaw property? " + dsLayerState.FrozenThawed);
             Debug.Print("Save LineColor property? " + dsLayerState.LineColor);
             Debug.Print("Save LineStyle property? " + dsLayerState.LineStyle);
             Debug.Print("Save LineWeight property? " + dsLayerState.LineWeight);
             Debug.Print("Save Lock/Unlock property? " + dsLayerState.LockedUnlocked);
             Debug.Print("Save Freeze/Thaw in new Viewport property? " + dsLayerState.NewViewPortFrozenThawed);
             Debug.Print("Save Print/No print property? " + dsLayerState.PrintNoPrint);
             Debug.Print("Save PrintStyle property? " + dsLayerState.PrintStyle);
             Debug.Print("Save On/Off property? " + dsLayerState.ShowHide);
             Debug.Print("Save Transparency property? " + dsLayerState.Transparency);

             object layerObj = null;
             layerObj = dsLayerState.GetLayers();

             dsLayerStateProperties = dsLayerState.GetLayerProperties("Object");

             Debug.Print("Layer: " + dsLayerStateProperties.LayerName);
             Debug.Print("Name: " + dsLayerStateProperties.Name);
             Debug.Print("Active: " + dsLayerStateProperties.Status);
             Debug.Print("Frozen: " + dsLayerStateProperties.Frozen);
             Debug.Print("LineStyle: " + dsLayerStateProperties.LineStyle);
             Debug.Print("LineWeight as defined in dsLineWeight_e: " + dsLayerStateProperties.LineWeight);
             Debug.Print("Locked: " + dsLayerStateProperties.Locked);
             Debug.Print("Frozen in new Viewport: " + dsLayerStateProperties.FrozenInNewViewport);
             Debug.Print("Can be printed: " + dsLayerStateProperties.Print);
             Debug.Print("PrintStyle: " + dsLayerStateProperties.PrintStyle);
             Debug.Print("On: " + dsLayerStateProperties.Show);
             Debug.Print("Transparency (%): " + dsLayerStateProperties.Transparency);
         }

     }
 }
```
