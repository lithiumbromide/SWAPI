---
title: "Attach Note and Tolerance Annotations to Leaders Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Attach_Note_and_Tolerance_Annotations_to_Leaders_Example_CSharp.htm"
---

# Attach Note and Tolerance Annotations to Leaders Example (C#)

This example shows how to attach Note and Tolerance annotations to Leaders.

```
//-------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the C# IDE.
// 3. Add a reference to:
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll
// 4. Add a reference to System.Windows.Forms.
// 5. Start DraftSight and open a document.
// 6. Click Start Debugging.
//
// Postconditions:
// 1. A Leader is constructed with a Note.
// 2. Click within the drawing to specify the point
//    where to attach a geometric Tolerance annotation
//    to the Leader.
// 3. The geometric Tolerance annotation is attached to
//    the Leader.
// 4. A second leader is constructed with a Note.
// 5. Click within the drawing to specify the
//    point where to attach the New Note annotation to
//    the Leader.
// 6. The New Note annotation is attached to the Leader.
// 7. The drawing is zoomed to fit.
//------------------------------------------------------------
using System.IO;
using DraftSight.Interop.dsAutomation;
using System.Windows.Forms;
using System.Runtime.InteropServices;

namespace CreateNoteToleranceLeadersCSharp
{
    static class Module1
    {
        static DraftSight.Interop.dsAutomation.Application dsApp = default(DraftSight.Interop.dsAutomation.Application);

	    public static void Main()
	    {
		    //Connect to DraftSight application
		    dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");

                      // Abort any command currently running in DraftSight to avoid nested commands
		    dsApp.AbortRunningCommand();

		    //Get active document
		    Document dsDoc = dsApp.GetActiveDocument();
		    if (dsDoc == null) {
			    MessageBox.Show("There are no open documents in DraftSight.");
			    return;
		    }

		    //Get model space
		    Model dsModel = dsDoc.GetModel();

		    //Get the Sketch Manager
		    SketchManager dsSketchMgr = dsModel.GetSketchManager();

		    //Add first Leader
		    double[] leaderCoordinates = new double[] {
			    6.5,
			    7.2,
			    0,
			    7.7,
			    8.6,
			    0
		    };
		    double noteWidth = 1.0;
		    string noteText = "L1 ";
		    Leader dsLeader = dsSketchMgr.InsertLeader(leaderCoordinates, noteWidth, noteText);

		    //Get command message
		    CommandMessage dsCommandMessage = dsApp.GetCommandMessage();

                      //Get math utility
		    MathUtility dsMathUtility = dsApp.GetMathUtility();

		    //Prompt to select the point where to insert the
		    //Tolerance annotation to the Leader
		    double firstX = 0;
		    double firstY = 0;
		    double firstZ = 0;
		    MathPlane dsMathPlane = default(MathPlane);
		    dsMathUtility = dsApp.GetMathUtility();
		    dsMathPlane = dsMathUtility.CreateXYPlane();
		    bool status = false;
                      status = dsCommandMessage.PromptForPoint2("Click within the drawing to insert the geometric Tolerance", true, 0, 0, 0, out firstX, out firstY, out firstZ, dsMathPlane);

		    //Create the first math point
		    MathPoint dsFirstMathPoint = dsMathUtility.CreatePoint(firstX, firstY, firstZ);

                      //Attach the Tolerance annotaion
		    dsLeader.SetToleranceAnnotation("{\\Fgdt;j}%%v{\\Fgdt;n}0.7{\\Fgdt;m}", dsFirstMathPoint);

		    //Add second Leader
		    double[] leaderCoordinates2 = new double[] {
			    18,
			    29,
			    0,
			    30,
			    26,
			    0
		    };
		    double noteWidth2 = 1.0;
		    string noteText2 = "L2 ";
		    Leader dsLeader2 = dsSketchMgr.InsertLeader(leaderCoordinates2, noteWidth2, noteText2);

		    //Prompt to select the point where to insert a
		    //Note annotation to the Leader
                      double secondX = 0;
		    double secondY = 0;
		    double secondZ = 0;
		    MathPlane dsMathPlane2 = default(MathPlane);
		    MathUtility dsMathUtility2 = dsApp.GetMathUtility();
		    dsMathPlane2 = dsMathUtility2.CreateXYPlane();
                       bool status2 = false;
		    status2 = dsCommandMessage.PromptForPoint2("Click within the drawing to specify where to insert the Note", true, 0, 0, 0, out secondX, out secondY, out secondZ, dsMathPlane2);

		    //Create the second math point
		    MathPoint dsSecondMathPoint = dsMathUtility.CreatePoint(secondX, secondY, secondZ);
```

```
                      //Attach the New Note annotation
		    dsLeader2.SetNoteAnnotation("New Note", dsSecondMathPoint);

		    dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, null, null);

	    }

    }
}
```
