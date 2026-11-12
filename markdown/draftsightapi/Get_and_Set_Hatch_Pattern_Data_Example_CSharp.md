---
title: "Get and Set Hatch Pattern Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_and_Set_Hatch_Pattern_Data_Example_CSharp.htm"
---

# Get and Set Hatch Pattern Data Example (C#)

This example shows how to get and set Hatch pattern data.

```vb
 //--------------------------------------------------------------
 // Preconditions:
 // 1.  Create a C# Windows console project.
 // 2.  Copy and paste this example into the C# IDE.
 // 3.  Add a reference to:
 //     install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
 // 4.  Add references to System and System.Windows.Forms.
 // 5.  Make sure that C:\ProgramData\Dassault Systemes\DraftSight\Examples
 //     exists.
 // 6.  Copy all .dxf and .dwg files in this folder to a backup folder.
 // 7.  Set all .dxf and .dwg files in
 //     C:\ProgramData\Dassault Systemes\DraftSight\Examples
 //     to read/write.
 // 8.  Start DraftSight.
 // 9.  Open the Immediate window.
 // 10. Start debugging the project.
 //
 // Postconditions:
 // 1. Each .dxf or .dwg file in
 //    C:\ProgramData\Dassault Systemes\DraftSight\Examples is
 //    filtered for Hatch patterns.
 // 2. Hatch patterns are changed in the .dxf and .dwg files
 //    that have them. Examine the Immediate window.
 // 3. Copy all .dxf and .dwg files from the backup folder to
 //     C:\ProgramData\Dassault Systemes\DraftSight\Examples.
 //----------------------------------------------------------------

 using System;
 using System.Collections.Generic;
 using System.Text;
 using System.Runtime.InteropServices;
 using System.Windows.Forms;
 using System.IO;
 using DraftSight.Interop.dsAutomation;
 using System.Diagnostics;

 namespace ChangeHatchPattern
 {
     class Program
     {
         static void Main(string[] args)
         {
             //Connect to DraftSight application
             DraftSight.Interop.dsAutomation.Application dsApp = ConnectToDraftSight();
             if (null == dsApp)
             {
                 return;
             }

             dsApp.AbortRunningCommand(); // abort any command currently running in DraftSight to avoid nested commands

             //Check if the specified folder exists
             string folderName = "C:\\ProgramData\\Dassault Systemes\\DraftSight\\Examples";

             if (false == Directory.Exists(folderName))
             {
                 Console.WriteLine("\"" + folderName + "\" does not exist.");
                 return;
             }

             //Get drawing files in the folder
             List<string> drawings = GetDrawings(folderName);
             if (0 == drawings.Count)
             {
                 MessageBox.Show ("There are no DWG/DXF files in \"" + folderName + "\" directory.");
                 return;
             }

             //Iterate through all drawings
             foreach (string docName in drawings)
             {
                 //Open document
                 Document dsDoc = dsApp.OpenDocument2(docName,  dsDocumentOpenOption_e.dsDocumentOpen_Default, dsEncoding_e.dsEncoding_Default);
                 if (null != dsDoc)
                 {

                     //Print name of document
                     Debug.Print ("Name of document: " + dsDoc.GetPathName());

                     //Change Hatch pattern for all Hatch entities in the drawing
                     ChangeHatchPattern(dsDoc);

                     //Save document
                     dsDoc.Save();

                     //Close document
                     dsApp.CloseDocument(docName, true);
                 }
                 else
                 {
                     MessageBox.Show("\"" + docName + "\" document could not be opened.");
                     return;
                 }
             }
         }

         private static void ChangeHatchPattern(Document dsDoc)
         {
             //Get model space
             Model dsModel = dsDoc.GetModel();

             //Get Sketch Manager
             SketchManager dsSketchMgr = dsModel.GetSketchManager();

             //GetSselection Manager
             SelectionManager dsSelectionMgr = dsDoc.GetSelectionManager();

             //Get selection filter
             SelectionFilter dsSelectionFilter = dsSelectionMgr.GetSelectionFilter();

             //Clear selection filter
             dsSelectionFilter.Clear();

             //Add Hatch entity to the selection filter
             dsSelectionFilter.AddEntityType(dsObjectType_e.dsHatchType);

             //Activate selection filter
             dsSelectionFilter.Active = true;

             //Get all Layer names
             string[] layerNames = GetLayers(dsDoc);

             object entityTypes;
             object entityObjects;

             //Get Hatch entities
             dsSketchMgr.GetEntities(dsSelectionFilter, layerNames, out entityTypes, out entityObjects);

             object[] dsEntities = (object[])entityObjects;
             if (entityObjects == null)
             {
                 Debug.Print("   Document does not have Hatch patterns.");
                 Debug.Print(" ");
             }
             else
             {
                 Debug.Print("   Document has Hatch patterns.");

                 //Iterate through Hatch entities
                 foreach (object entityItem in dsEntities)
                 {
                     //Cast to Hatch entity
                     Hatch dsHatch = entityItem as Hatch;

                     //Get Hatch pattern
                     string patternName = "";
                     double angle = 0.0;
                     double scale = 0.0;
                     dsHatchPatternType_e patternType = dsHatchPatternType_e.dsHatchPatternType_Predefined;
                     double spacing = 1.0;
                     HatchPattern dsHatchPattern = dsHatch.GetHatchPattern();

                     dsHatchPattern.GetHatchOrSolidData(out patternName, out angle, out scale, out patternType, out spacing);
                     Debug.Print ("   Pattern name, angle, scale, pattern types, spacing: " + patternName +  ", " + angle + ", " +  scale + ", " +  patternType + ", " + spacing);

                     //Update Hatch pattern
                     patternName =  "HOUND";
                     angle = 0.0;
                     scale = 1.0;
                     patternType =  dsHatchPatternType_e.dsHatchPatternType_Predefined;
                     spacing = 1.0;
                     dsHatchPattern.SetHatchOrSolidData(patternName, angle, scale, patternType, spacing);
                 }
                 Debug.Print(" ");
             }
         }

         private static string[] GetLayers(Document dsDoc)
         {
             //Get Layer Manager and Layer names
             LayerManager dsLayerManager = dsDoc.GetLayerManager();

             object[] dsLayers = (object[])dsLayerManager.GetLayers();

             string[] layerNames = new string[dsLayers.Length];

             for (int index = 0; index < dsLayers.Length; ++index)
             {
                 Layer dsLayer = dsLayers[index] as Layer;
                 layerNames[index] = dsLayer.Name;
             }

             return layerNames;
         }

         private static DraftSight.Interop.dsAutomation.Application ConnectToDraftSight()
         {
             DraftSight.Interop.dsAutomation.Application dsApp = null;

             try
             {
                 //Connect to DraftSight
                 dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");
             }
             catch (Exception ex)
             {
                 Console.WriteLine("Failed to connect to DraftSight. Cause: " + ex.Message);
                 dsApp = null;
             }

             return dsApp;
         }

         private static List<string> GetDrawings(string folderName)
         {
             List<string> drawings = new List<string>();
             //Get DWG files
             string[] files = Directory.GetFiles(folderName, "*.dwg");
             if (null != files)
             {
                 drawings.AddRange(files);
             }

             //Get DXF files
             files =  Directory.GetFiles(folderName, "*.dxf");
             if (null != files)
             {
                 drawings.AddRange(files);
             }

             return drawings;
         }
     }
 }
```
