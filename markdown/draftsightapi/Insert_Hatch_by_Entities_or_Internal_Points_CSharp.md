---
title: "Insert Hatch by Entities or Internal Points (C#)"
project: ""
interface: ""
member: ""
kind: "topic"
source: "draftsightapi/Insert_Hatch_by_Entities_or_Internal_Points_CSharp.htm"
---

# Insert Hatch by Entities or Internal Points (C#)

## Insert Hatch by Entities or Internal Points Example (C#)

This example shows how to insert a Hatch either by selecting sketch entities that form the Hatch boundary or by selecting internal points of enclosed areas of a drawing.

```vb
 //--------------------------------------------------------------
 // Preconditions:
 // 1. Create a C# Windows console project.
 // 2. Copy and paste this example into the C# IDE.
 // 3. Add a reference to:
 //    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
 // 4. Add references to System and System.Windows.Forms.
 // 5. Start DraftSight and open a drawing document with sketch entities.
 // 6. Start debugging the project.
 //
 // In the DraftSight command window, choose how the Hatch should be inserted:
 //    1. Type Entities.
 //    2. Select the sketch entities that form the boundary of the area to be hatched.
 //    3. Press Enter when finished.
 //    - or -
 //    1. Type InternalPoints.
 //    2. Select three points that are in enclosed areas of the drawing.
 //
 // Postconditions: A Hatch is inserted, and the drawing document
 // is zoomed to fit.
 //----------------------------------------------------------------
 using System;
 using System.Collections.Generic;
 using System.Text;
 using DraftSight;
 using System.Runtime.InteropServices;
 using System.Windows.Forms;
 using System.Diagnostics;

 namespace AddHatch
 {
     class Program
     {
         private static DraftSight.Application dsApp;
         private static DraftSight.Document dsDoc;

         static void Main(string[] args)
         {
             //Connect to DraftSight application
             dsApp = ConnectToDraftSight();
             if (null == dsApp)
             {
                 return;
             }

             dsApp.AbortRunningCommand(); // abort any command currently running in DraftSight to avoid nested commands

             //Get active document
             dsDoc = dsApp.GetActiveDocument();
             if (null == dsDoc)
             {
                 MessageBox.Show("There are no open documents in DraftSight.");
                 return;
             }

             //Get model space
             Model dsModel = dsDoc.GetModel();

             //Get sketch manager
             SketchManager dsSketchMgr = dsModel.GetSketchManager();

             //Get command message object
             CommandMessage dsCommandMessage = dsApp.GetCommandMessage();

             //Display a prompt at the command line to create Hatch by entities or by internal points
             string[] keywords = { "Entities", "InternalPoints" };
             string selectedKeyword;
             bool promptResult = dsCommandMessage.PromptForKeyword("Insert Hatch by:", keywords, keywords[0],  out selectedKeyword);
             if (promptResult)
             {
                 //The user selected "By Entities" option
                 if (selectedKeyword.ToUpper() == "_" + keywords[0].ToUpper() ||
                     selectedKeyword.ToUpper() == keywords[0].ToUpper())
                 {
                     DispatchWrapper[] selectedEntities = SelectEntities(dsCommandMessage);

                     InsertHatchByEntities(dsSketchMgr, selectedEntities);
                 }

                 //The user selected "By Internal Points" option
                 if (selectedKeyword.ToUpper() == "_" + keywords[1].ToUpper())
                 {
                     //Select three internal points
                     int pointsCount = 3;

                     dsCommandMessage.PrintLine("Select three internal points for a hatch");

                     double[] internalPoints = SelectPoints(dsCommandMessage, pointsCount);

                     InsertHatchByInternalPoints(dsSketchMgr, internalPoints);
                 }
             }
         }

         private static void InsertHatchByInternalPoints(SketchManager dsSketchMgr, double[] internalPoints)
         {
             //Hatch parameters
             string patternName = "ANSI31";
             double patternScale = 1;
             double patternAngle = 0;

             //Insert Hatch
             Hatch dsHatch = dsSketchMgr.InsertHatchByInternalPoints(internalPoints, patternName, patternScale, patternAngle);
             if (null != dsHatch)
             {
                 //Change color of Hatch
                 Color dsColor = dsHatch.Color;
                 dsColor.SetNamedColor(dsNamedColor_e.dsNamedColor_Green);
                 dsHatch.Color = dsColor;

                 //Zoom to fit
                 dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, null, null);
             }
             else
             {
                 MessageBox.Show("Hatch entity was not added to the current drawing.");
             }
         }

         private static double[] SelectPoints(CommandMessage dsCommandMessage, int internalPointsCount)
         {
             List<double> internalPoints = new List<double>();

             //Display prompt for point
             double x, y, z;
             int count = 0;
             while (count < internalPointsCount)
             {
                 if (dsCommandMessage.PromptForPoint("Specify internal point",  out x,  out y,  out z))
                 {
                     internalPoints.Add(x);
                     internalPoints.Add(y);
                 }

                 count++;
             }

             return internalPoints.ToArray();
         }

         private static void InsertHatchByEntities(SketchManager dsSketchMgr, DispatchWrapper[] dsEntities)
         {
             //Hatch parameters
             string patternName = "GRASS";
             double patternScale = 1;
             double patternAngle = 0;

             //Insert Hatch
             Hatch dsHatch = dsSketchMgr.InsertHatchByEntities(dsEntities, patternName, patternScale, patternAngle);
             if (null != dsHatch)
             {
                 //Change color of Hatch
                 Color dsColor = dsHatch.Color;
                 dsColor.SetNamedColor(dsNamedColor_e.dsNamedColor_Blue);
                 dsHatch.Color = dsColor;

                 //Zoom to fit
                 dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, null, null);
             }
             else
             {
                 MessageBox.Show("Hatch entity was not added to the current drawing.");
             }
         }

         private static DispatchWrapper[] SelectEntities(CommandMessage dsCommandMessage)
         {
             DispatchWrapper[] selectedEntities = null;

             //Prompt for multiple selection of entities
             if (dsCommandMessage.PromptForSelection(false, "Specify entities", "It is not an entity"))
             {
                 //Get selection manager
                 SelectionManager dsSelectionMgr = dsDoc.GetSelectionManager();

                 //Get count of selected entities
                 dsSelectionSetType_e selectionType = dsSelectionSetType_e.dsSelectionSetType_Previous;
                 int count = dsSelectionMgr.GetSelectedObjectCount(selectionType);
                 if (count > 0)
                 {
                     selectedEntities = new DispatchWrapper[count];
                     for (int index = 0; index < count; ++index)
                     {
                         dsObjectType_e entityType;
                         selectedEntities[index] =  new  DispatchWrapper(dsSelectionMgr.GetSelectedObject(selectionType, index, out entityType));
                     }
                 }
             }

             return selectedEntities;
         }

         private static DraftSight.Application ConnectToDraftSight()
         {
             DraftSight.Application dsApp = null;

             try
             {
                 //Connect to DraftSight
                 dsApp = (DraftSight.Application)Marshal.GetActiveObject("DraftSight.Application");
             }
             catch (Exception ex)
             {
                 MessageBox.Show("Failed to connect to DraftSight. Cause: " + ex.Message);
                 dsApp = null;
             }

             return dsApp;
         }
     }
 }
```
