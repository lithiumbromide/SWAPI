---
title: "Insert Notes with Parameters Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Notes_with_Parameters_Example_CSharp.htm"
---

# Insert Notes with Parameters Example (C#)

This example shows how to insert Notes with parameters in a drawing document.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the C# IDE.
// 3. Add a reference to:
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
// 4. Add references to System and System.Windows.Forms.
// 5. Start DraftSight and open a document.
// 6. Start debugging the project.
//
// Postconditions: A message box pops up when Notes with parameters
// are inserted in the drawing document.
//----------------------------------------------------------------
```

```
using DraftSight.Interop.dsAutomation;
using System;
using System.Runtime.InteropServices;
using System.Windows.Forms;
```

```
static class Module1
{
    public static void Main()
	{
		DraftSight.Interop.dsAutomation.Application dsApp;
```

```
		Document dsDoc = default(Document);
		Model dsModel = default(Model);
		SketchManager dsSketchManager = default(SketchManager);
		Note dsNote = default(Note);
		double x1 = 0;
		double y1 = 0;
		double z1 = 0;
		double x2 = 0;
		double y2 = 0;
		double z2 = 0;
        	double angle = 0;
        	double height = 0;
        	double lineSpaceDistance = 0;
        	double width = 0;
		string[] strArray = new string[2];
        	string textStyle;
        	dsNoteJustification_e justify;
        	dsNoteLineSpacingStyle_e lineSpacingStyle;
```

```
		//Connect to DraftSight
                dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");
		dsApp.AbortRunningCommand(); // abort any command currently running in DraftSight to avoid nested commands

		//Get active document
		dsDoc = dsApp.GetActiveDocument();
		if (dsDoc != null)
                {
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
                        angle = 0.0;
                        height = 1.0;
                        justify = dsNoteJustification_e.dsNoteJustification_BottomCenter;
                        lineSpacingStyle = dsNoteLineSpacingStyle_e.dsNoteLineSpacingStyle_AtLeast;
                        lineSpaceDistance = 1.5;
                        textStyle = "Standard";
                        width = 25.0;
```

```
			//Add notes
			dsNote = dsSketchManager.InsertNoteWithParameters(x1, y1, z1, x2, y2, z2, strArray, angle, height, justify, lineSpacingStyle, lineSpaceDistance, textStyle, width);
			if (dsNote != null)
                        {
				MessageBox.Show("Notes with parameters were inserted in the drawing.");
			}
		}
                else
                {
			MessageBox.Show("There are no open documents in DraftSight.");
		}
	}
```

```
}
```
