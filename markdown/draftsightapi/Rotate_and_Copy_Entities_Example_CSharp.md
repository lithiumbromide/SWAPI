---
title: "Rotate and Copy Entities Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Rotate_and_Copy_Entities_Example_CSharp.htm"
---

# Rotate and Copy Entities Example (C#)

This example shows how to rotate and copy selected entities.

```vb
 //--------------------------------------------------------------
 // Preconditions:
 // 1. Create a C# Windows console project.
 // 2. Copy and paste this example into the C# IDE.
 // 3. Add a reference to:
 //    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
 // 4. Add references to System and System.Windows.Forms.
 // 5. Start DraftSight and open a new document.
 // 6. Construct multiple entities (e.g., circle, rectangle, 2D PolyLine,
 //    etc.).
 // 7. Start debugging the project.
 //
 // Postconditions:
 // 1. When the prompt appears in the DraftSight command window,
 //    select the entities to rotate and press the Enter key. The
 //    selected entities are rotated.
 // 2. Execution stops so that you can examine the drawing to
 //    verify that the selected entities were rotated. Click the
 //    Continue button in the IDE to continue.
 // 3. The selected entities are copied.
 //----------------------------------------------------------------

 using System;
 using System.Collections.Generic;
 using System.Text;
 using DraftSight.Interop.dsAutomation;
 using System.Runtime.InteropServices;
 using System.Windows.Forms;
 using System.Diagnostics;

 namespace RotateSelectedEntities
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

             //Get active document
             Document dsDoc = dsApp.GetActiveDocument();
             if (null == dsDoc)
             {
                 MessageBox.Show("There are no open documents in DraftSight.");
                 return;
             }

             //Get model space
             Model dsModel = dsDoc.GetModel();

             //Get Sketch Manager
             SketchManager dsSketchMgr = dsModel.GetSketchManager();

             //Get selection manager
             SelectionManager dsSelectionMgr = dsDoc.GetSelectionManager();

             //Get selection filter
             SelectionFilter dsSelectionFilter = dsSelectionMgr.GetSelectionFilter();

             //Clear selection filter
             dsSelectionFilter.Clear();

             //Add all entities to the selection filter
             foreach (dsObjectType_e entityType in Enum.GetValues(typeof(dsObjectType_e)))
             {
                 dsSelectionFilter.AddEntityType(entityType);
             }

             //Activate selection filter
             dsSelectionFilter.Active = true;

             //Get command message object
             CommandMessage dsCommandMessage = dsApp.GetCommandMessage();

             //Clear previous selection
             dsSelectionMgr.ClearSelections(dsSelectionSetType_e.dsSelectionSetType_Previous);

             //Run prompt to select entities
             bool singleSelection = false;
             string prompt = "Select entities";
             string errorMessage = "Unknown entity";
             if (dsCommandMessage.PromptForSelection(singleSelection, prompt, errorMessage))
             {
                 //Get number of selected objects
                 int count = dsSelectionMgr.GetSelectedObjectCount(dsSelectionSetType_e.dsSelectionSetType_Previous);

                 DispatchWrapper[] dsEntities = new DispatchWrapper[count];
                 int[] dsEntityTypes = new int[count];

                 //Get selected entities
                 for (int index = 0; index < count; ++index)
                 {
                     dsObjectType_e entityType;
                     object selectedEntity = dsSelectionMgr.GetSelectedObject(dsSelectionSetType_e.dsSelectionSetType_Previous, index, out entityType);
                     dsEntities[index] = new DispatchWrapper(selectedEntity);

                     dsEntityTypes[index] = (int)entityType;
                 }

                 //Rotation parameters
                 double pivotPointX = 0.0;
                 double pivotPointY = 0.0;
                 double rotateAngle = Math.PI / 4; //In radians

                 //Rotate entities
                 dsSketchMgr.RotateEntities(pivotPointX, pivotPointY, rotateAngle, dsEntityTypes, dsEntities);

                 //Stop execution
                 //Examine the document
                 System.Diagnostics.Debugger.Break();

                 //Click the Continue button in the IDE

                 //Copy parameters
                 double displacementX = 2.0;
                 double displacementY = 2.0;
                 double displacementZ = 0.0;

                 //Copy entities
                 object[] dsEntityCopies = dsSketchMgr.CopyEntities2(displacementX, displacementY, displacementZ, dsEntityTypes, dsEntities);

             }
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
                 MessageBox.Show("Failed to connect to DraftSight. Cause: " + ex.Message);
                 dsApp = null;
             }

             return dsApp;
         }
     }
 }
```
