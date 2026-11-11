---
title: "Create Rectangular Viewport Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Rectangular_Viewport_Example_CSharp.htm"
---

# Create Rectangular Viewport Example (C#)

This example shows how to create a rectangular Viewport.

//--------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the C# IDE.
// 3. Add a reference to:
// `install_dir`\**APISDK\tlb\DraftSight.Interop.dsAutomation.dll**
// 4. Add a reference to **System**.
// 5. Start DraftSight.
// 6. Open the Immediate window.
// 7. Press F5 to debug the project.
//
// Postconditions:
// 1. A Viewport is created on Sheet2.
// 2. Examine the drawing and output printed
// to the Immediate window.
//----------------------------------------------------------------

```
using System;
using System.Diagnostics;
using System.Runtime.InteropServices;
using DraftSight.Interop.dsAutomation;

static class Module1
{

    public static void Main()
	{
		DraftSight.Interop.dsAutomation.Application dsApp;
		Document dsDoc = default(Document);
		string SheetName = null;
		object[] dsSheets = null;
		Sheet dsSheet = default(Sheet);
		int index = 0;
		Viewport dsViewport = default(Viewport);
		MathUtility dsMathUtility = default(MathUtility);
		MathPoint startCorner = default(MathPoint);
		MathPoint oppositeCorner = default(MathPoint);
		bool isClipped = false;

		//Connect to DraftSight
        dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");

		//Abort any command currently running in DraftSight
		//to avoid nested commands
		dsApp.AbortRunningCommand();

		//Get active document
		dsDoc = dsApp.GetActiveDocument();

		if ((dsDoc != null)) {
			//Switch to Sheet space and activate Sheet2
			dsSheets = (object[])dsDoc.GetSheets();
			if (dsSheets is System.Array) {
				for (index = 0; index < dsSheets.Length; index++) {
					dsSheet = (Sheet)dsSheets[index];
					//Get sheet name
					SheetName = dsSheet.Name;
					//Change sheet name, if it is not a model
					if (SheetName != "Model") {
						//Activate sheet
						dsSheet.Activate();
					}
				}
			}

			// Set the corners for the Viewport
			dsMathUtility = dsApp.GetMathUtility();
			startCorner = dsMathUtility.CreatePoint(0, 0, 0);
			oppositeCorner = dsMathUtility.CreatePoint(3, 3, 0);

			//Create a rectangular Viewport
			dsViewport = dsSheet.InsertRectangularViewport(dsStandardViewports_e.dsStandardViewports_1, false, startCorner, oppositeCorner);

			// Activate and access the rectangular Viewport
			dsViewport.Active = true;
			Debug.Print(SheetName + ":");
			Debug.Print("  Viewport:");
			dsViewport.GetIsClipped(out isClipped);
			Debug.Print("    Clipped by an entity?       " + isClipped);
			Debug.Print("    Height:                     " + dsViewport.Height);
			Debug.Print("    Width:                      " + dsViewport.Width);
			Debug.Print("    Locked in model workspace?  " + dsViewport.DisplayLocked);
			Debug.Print("    Displayed in graphics area? " + dsViewport.IsOn);
			Debug.Print("    Visible?                    " + dsViewport.Visible);
		} else {
			Debug.Print("There are no open documents in DraftSight.");
		}
	}

}
```
