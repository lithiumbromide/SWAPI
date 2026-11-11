---
title: "Insert Notes with Background Mask Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Notes_with_Background_Mask_Example_CSharp.htm"
---

# Insert Notes with Background Mask Example (C#)

This example shows how to insert Notes with a background Mask in a drawing document.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the C# IDE.
// 3. Add a reference to:
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
// 4. Add a reference to System.Windows.Forms.
// 5. Start DraftSight.
// 6. Press F5.
//
// Postconditions:
// 1. Inserts two Notes with a blue background Mask in the drawing.
// 2. Zooms to fit the two Notes in the drawing.
// 3. Examine the drawing.
//----------------------------------------------------------------

using DraftSight.Interop.dsAutomation;
using System;
using System.Runtime.InteropServices;
using System.Windows.Forms;

static class Module1
{
    public static void Main()
	{
		DraftSight.Interop.dsAutomation.Application dsApp;

		Document dsDoc = default(Document);
		Model dsModel = default(Model);
		SketchManager dsSketchManager = default(SketchManager);
		Note dsNote = default(Note);
        		Color dsColor = default(Color);
		double x1 = 0;
		double y1 = 0;
		double z1 = 0;
		double x2 = 0;
		double y2 = 0;
		double z2 = 0;
		string[] strArray = new string[2];

		//Connect to DraftSight
        		dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");

		//Get active document
		dsDoc = dsApp.GetActiveDocument();

		if ((dsDoc != null)) {
			//Get model space
			dsModel = dsDoc.GetModel();
			//Get Sketch Manager
			dsSketchManager = dsModel.GetSketchManager();
			//Note parameters
			x1 = 10.0;
			y1 = 10.0;
			z1 = 0.0;
			x2 = 60.0;
			y2 = 20.0;
			z2 = 0.0;
			strArray[0] = "First Note's text line.";
			strArray[1] = "Second Note's text line.";
			//Add a note
			dsNote = dsSketchManager.InsertNote(x1, y1, z1, x2, y2, z2, strArray);

            		//Change height of Note text
            		dsNote.TextHeight = 2;

            		//Change Note to use blue background Mask
            		dsNote.UseDrawingBackgroundColor = false;
            		dsNote.BackgroundMask = true;
            		dsNote.BackgroundBorderOffsetFactor = 4;

            		dsColor = dsNote.Color;
            		dsColor.SetNamedColor(dsNamedColor_e.dsNamedColor_Blue);
            		dsNote.BackgroundFillColor = dsColor;

            		//Zoom to fit the Note
            		dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, null, null);
		}

        		else{
			MessageBox.Show("There are no open documents in DraftSight.");
		}
	}
}
```
