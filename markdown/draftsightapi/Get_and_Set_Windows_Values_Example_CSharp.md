---
title: "Get and Set Windows Values Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_and_Set_Windows_Values_Example_CSharp.htm"
---

# Get and Set Windows Values Example (C#)

This example shows how to get and set various DraftSight application and document window values.

```
//--------------------------------------------------------------
// Preconditions:
//  1. Create a C# Windows console project.
//  2. Copy and paste this project into the C#.
//  3. Add a reference to
//     install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll
//  4. Add references to System and System.Windows.Forms.
//  5. Start DraftSight.
//  6. Open the Immediate window.
//  7. Press F5.
//
// Postconditions:
// 1. Document window is minimized.
// 2. Examine the Immediate window where
//    the application and document window handle values,
//    visibility values, window states, and frame and
//    geometry positions and sizes are printed.
// 3. Interactively maximize the document window in DraftSight.
//----------------------------------------------------------------

using System.IO;
using DraftSight.Interop.dsAutomation;
using System.Diagnostics;
using System.Windows.Forms;
using System.Runtime.InteropServices;

static class Module1
{

    static DraftSight.Interop.dsAutomation.Application dsApp;
    static Document dsDoc;
    static DraftSight.Interop.dsAutomation.DSWindow dsAppWindow;
    static DraftSight.Interop.dsAutomation.DSWindow dsDocWindow;

    public static void Main()
	{
		//Connect to DraftSight
        		dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");

		//Abort any command currently running in DraftSight to avoid nested commands
		dsApp.AbortRunningCommand();

		//Get application's window handle, visibility, and state
		Debug.Print("Application window using Application object:");
		Debug.Print("  Window handle: " + dsApp.GetHWND());
		Debug.Print("  Visible:       " + dsApp.Visible);
		Debug.Print("  State:         " + dsApp.WindowState);

		Debug.Print("");

		//Get active document
		dsDoc = dsApp.GetActiveDocument();
		if ((dsDoc != null)) {
			// Get application's window handle, visibility, and state
			Debug.Print("Application window using DSWindow object:");
			dsAppWindow = dsApp.GetMainWindow();
			int windowHandle = 0;
			dsAppWindow.GetHWND(out windowHandle);
			Debug.Print("  Window handle:     " + windowHandle);
			Debug.Print("  Visible            " + dsAppWindow.Visible);
			Debug.Print("  State:             " + dsAppWindow.WindowState);
			int x = 0;
			int y = 0;
			// Get application's frame and geometry positions and sizes
			dsAppWindow.GetFramePosition(out x, out y);
			Debug.Print("  Frame position:    " + x + ", " + y);
			dsAppWindow.GetFrameSize(out x, out y);
			Debug.Print("  Frame size:        " + x + ", " + y);
			dsAppWindow.GetGeometryPosition(out x, out y);
			Debug.Print("  Geometry position: " + x + ", " + y);
			dsAppWindow.GetGeometrySize(out x, out y);
			Debug.Print("  Geometry size:     " + x + ", " + y);

			Debug.Print(" ");

			// Get document's window handle, visibility, state,
			// frame and geometry positions and sizes
			Debug.Print("Document window using DSWindow object before minimizing window:");
			dsDocWindow = dsDoc.GetWindow();
			dsDocWindow.GetHWND(out windowHandle);
			Debug.Print("  Window handle:     " + windowHandle);
			Debug.Print("  Visible            " + dsDocWindow.Visible);
			Debug.Print("  State:             " + dsDocWindow.WindowState);
			dsDocWindow.GetFramePosition(out x, out y);
			Debug.Print("  Frame position:    " + x + ", " + y);
			dsDocWindow.GetFrameSize(out x, out y);
			Debug.Print("  Frame size:        " + x + ", " + y);
			dsDocWindow.GetGeometryPosition(out x, out y);
			Debug.Print("  Geometry position: " + x + ", " + y);
			dsDocWindow.GetGeometrySize(out x, out y);
			Debug.Print("  Geometry size:     " + x + ", " + y);

			//Minimize document window
			dsDocWindow.WindowState = 0;

			Debug.Print("");
			// Get document's window handle, visibility, state,
			// frame and geometry positions and sizes after minimizing
			// window
			Debug.Print("Document window using DSWindow object after minimizing the window:");
			dsDocWindow = dsDoc.GetWindow();
			dsDocWindow.GetHWND(out windowHandle);
			Debug.Print("  Window handle:     " + windowHandle);
			Debug.Print("  Visible            " + dsDocWindow.Visible);
			Debug.Print("  State:             " + dsDocWindow.WindowState);
			dsDocWindow.GetFramePosition(out x, out y);
			Debug.Print("  Frame position:    " + x + ", " + y);
			dsDocWindow.GetFrameSize(out x, out y);
			Debug.Print("  Frame size:        " + x + ", " + y);
			dsDocWindow.GetGeometryPosition(out x, out y);
			Debug.Print("  Geometry position: " + x + ", " + y);
			dsDocWindow.GetGeometrySize(out x, out y);
			Debug.Print("  Geometry size:     " + x + ", " + y);

		} else {
			MessageBox.Show("There are no open documents in DraftSight.");
		}

	}

}
```
