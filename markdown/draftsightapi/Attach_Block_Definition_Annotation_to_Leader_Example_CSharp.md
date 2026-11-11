---
title: "Attach Block Definition Annotation to Leader Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Attach_Block_Definition_Annotation_to_Leader_Example_CSharp.htm"
---

# Attach Block Definition Annotation to Leader Example (C#)

This example shows how to attach a Block definition annotation to a Leader.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the C# IDE.
// 3. Add a reference to:
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
// 4. Add a reference to System.Windows.Forms.
// 5. Start DraftSight and open a document.
// 6. Click Start Debugging.
//
// Postconditions:
// 1. A message box pops up when the Block definition,
//    named MyBlockAnnotation, is created.
// 2. Click OK to close the message box.
// 3. A Leader is created and MyBlockAnnotation is
//    is attached to the Leader.
// 4. The drawing zooms to fit.
// 5. Examine the drawing.
//----------------------------------------------------------------
using DraftSight.Interop.dsAutomation;
using System;
using System.Runtime.InteropServices;
using System.Windows.Forms;

static class Module1
{
    static void Main(string[] args)
        {
            DraftSight.Interop.dsAutomation.Application dsApp;
            Document dsDoc = default(Document);
            Model dsModel = default(Model);
            SketchManager dsSketchManager = default(SketchManager);

            //Connect to DraftSight
            dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");
            //Get active document
            dsDoc = dsApp.GetActiveDocument();
            if ((dsDoc != null))
            {
                //Get model space
                dsModel = dsDoc.GetModel();

                //Get Sketch Manager
                dsSketchManager = dsModel.GetSketchManager();

                //First Line's parameters
                double startX = 1.0;
                double startY = 1.0;
                double startZ = 0.0;
                double endX = 6.0;
                double endY = 1.0;
                double endZ = 0.0;

                //Construct a Line
                Line dsLine = (dsSketchManager.InsertLine(startX, startY, startZ, endX, endY, endZ));

                //Second Line's parameters
                double start2X = 2.0;
                double start2Y = 2.0;
                double start2Z = 0.0;
                double end2X = 2.0;
                double end2Y = 20.0;
                double end2Z = 0.0;

                //Construct another Line
                Line dsLine2 = (dsSketchManager.InsertLine(start2X, start2Y, start2Z, end2X, end2Y, end2Z));

                int[] typesArray = new int[] {21, 21};
                Line[] linesArray = new Line[] {dsLine, dsLine2};

                BlockDefinition dsBlockDef = dsDoc.CreateBlockDefinition ("MyBlockAnnotation", "Block annotation to attach to Leader", 0, 0, 0, typesArray, linesArray, dsBlockDefinitionEntities_e.dsBlockDefinitionEntities_ConvertToBlock);
                MessageBox.Show("Name of Block definition: " + dsBlockDef.GetName());

                //Add Leader
                double[] leaderCoordinates = new double[] { 6.5, 7.2, 0, 7.7, 8.6, 0 };
                double noteWidth = 1.0;
                string noteText = "L1 ";
                Leader dsLeader = dsSketchManager.InsertLeader(leaderCoordinates, noteWidth, noteText);

                //Attach Block definition to Leader,
                //which creates a Block instance
                MathUtility dsMathUtility = dsApp.GetMathUtility();
                MathPoint dsMathPoint = dsMathUtility.CreatePoint(20,20,25);
                dsLeader.SetBlockAnnotation("MyBlockAnnotation", dsMathPoint);

                dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, null, null);

        }
    }
}
```
