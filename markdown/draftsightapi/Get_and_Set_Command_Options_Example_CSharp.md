---
title: "Get and Set Command Options Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_and_Set_Command_Options_Example_CSharp.htm"
---

# Get and Set Command Options Example (C#)

This example shows how to get and set command options.

```
//------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the C# IDE.
// 3. Add a reference to:
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
// 4. Add a reference to System.
// 5. Open the Immediate window.
// 6. Start DraftSight and open a document.
// 7. Run the macro.
//
// Postconditions: Specified command option values are returned, set, and
// printed to the Immediate window. Results of setting specified command
// option values are also printed to the Immediate window.
//----------------------------------------------------------------
using DraftSight.Interop.dsAutomation;
using System;
using System.Runtime.InteropServices;
using System.Diagnostics;
```

```
static class Module1
{
    public static void Main()
	{
		DraftSight.Interop.dsAutomation.Application dsApp;
		Document dsDoc = default(Document);
```

```
		//Connect to DraftSight
        	dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");
		dsApp.AbortRunningCommand(); // abort any command currently running in DraftSight to avoid nested commands
```

```
		//Get active document
		dsDoc = dsApp.GetActiveDocument();
```

```
		if ((dsDoc != null)) {
			bool boolCommand = false;
			double doubleCommand = 0;
			int int16Command = 0;
			Int32 int32Command = 0;
			int int8Command = 0;
			double xint2DCommand = 0;
			double yint2DCommand = 0;
            		double xint3DCommand = 0;
            		double yint3DCommand = 0;
            		double zint3DCommand = 0;
			string valueStringCommand = "";
            		dsGetCommandOptionResult_e getResult = default(dsGetCommandOptionResult_e);
			dsSetCommandOptionResult_e setResult = default(dsSetCommandOptionResult_e);
```

```
			//Boolean
			//Get and set whether to enable drawing boundary
			//Tools > Options > Drawing Settings > Behavior > Drawing Boundary > Enable drawing boundary
            		dsDoc.GetCommandOptionBool(dsCommandOptionBool_e.dsCommandOptionBool_EnblDlDm, out boolCommand, out getResult);
			Debug.Print("Get drawing boundary value: " + boolCommand);
			boolCommand = true;
            		dsDoc.SetCommandOptionBool(dsCommandOptionBool_e.dsCommandOptionBool_EnblDlDm, boolCommand, out setResult);
			Debug.Print("Set drawing boundary value: " + boolCommand);
			Debug.Print("Set result: " + setResult);
			Debug.Print(" ");
```

```
			//Double
			//Get and set dimension tolerance precision
			//Tools > Options > Drafting Styles > Dimension > Tolerance > Tolerance settings > Precision
            		dsDoc.GetCommandOptionDouble(dsCommandOptionDouble_e.dsCommandOptionDouble_SetTDmMin, out doubleCommand, out getResult);
			Debug.Print("Get dimension tolerance precision: " + doubleCommand);
			doubleCommand = 2.0;
            		dsDoc.SetCommandOptionDouble(dsCommandOptionDouble_e.dsCommandOptionDouble_SetTDmMin, doubleCommand, out setResult);
			Debug.Print("Set dimension tolerance precision: " + doubleCommand);
			Debug.Print("Set result: " + setResult);
			Debug.Print(" ");
```

```
			//Int16
			//Get and set units for inserting entities
			//Tools > Options > System Options > Drawing File Defaults > Block insertion units > Units for inserting entities
            		dsDoc.GetCommandOptionInt16(dsCommandOptionInt16_e.dsCommandOptionInt16_SetActBlkInsUnt, out int16Command, out getResult);
			Debug.Print("Get units for inserting entities: " + int16Command);
			int16Command = 4;
            		dsDoc.SetCommandOptionInt16(dsCommandOptionInt16_e.dsCommandOptionInt16_SetActBlkInsUnt, int16Command, out setResult);
			Debug.Print("Set units for inserting entities: " + int16Command);
			Debug.Print("Set result: " + setResult);
			Debug.Print(" ");
```

```
			//Int32
			//Get and set the elapsed time between saving and backing up documents
			//Tools > Options > System Options > Auto-save & Backup > Auto-save/backups > Save document every nn minutes
            		dsDoc.GetCommandOptionInt32(dsCommandOptionInt32_e.dsCommandOptionInt32_SetSvTm, out int32Command, out getResult);
			Debug.Print("Get elapsed time between saving and backing up documents: " + int32Command);
			int32Command = 15;
            		dsDoc.SetCommandOptionInt32(dsCommandOptionInt32_e.dsCommandOptionInt32_SetSvTm, int32Command, out setResult);
			Debug.Print("Set elapsed time between saving and backing up documents: " + int32Command);
			Debug.Print("Set result: " + setResult);
			Debug.Print(" ");
```

```
			//Int8
			//Get and set whether dual dimensions display leading zeros, trailing zeros, 0', and 0"
			//Tools > Options > Drafting Styles > Dimension > Dual Dimension > Zeroes display
            		dsDoc.GetCommandOptionInt8(dsCommandOptionInt8_e.dsCommandOptionInt8_SetDlDmZroDsp, out int8Command, out getResult);
			Debug.Print("Get whether dual dimensions display leading zeros, trailing zeros, 0 feet, and 0 inches: " + int8Command);
			int8Command = 0;
            		dsDoc.SetCommandOptionInt8(dsCommandOptionInt8_e.dsCommandOptionInt8_SetDlDmZroDsp, int8Command, out setResult);
			Debug.Print("Set whether dual dimensions display leading zeros, trailing zeros, 0 feet, and 0 inches: " + int8Command);
			Debug.Print("Set result: " + setResult);
			Debug.Print(" ");
```

```
			//2D Point
			//Get and set horizontal and vertical snap spacing for the pointer device
			//Tools > Options > User Preferences > Drafting Options > Pointer Control > Snap Settings > Spacing > Horizontal Snap spacing and Vertical Snap spacing
            		dsDoc.GetCommandOptionPoint2D(dsCommandOptionPoint2d_e.dsCommandOptionPoint2d_SetSnpSpc, out xint2DCommand, out yint2DCommand, out  getResult);
			Debug.Print("Get pointer's horizontal and vertical snap values: " + xint2DCommand + ", " + yint2DCommand);
			xint2DCommand = 15.0;
			yint2DCommand = 15.0;
            		dsDoc.SetCommandOptionPoint2D(dsCommandOptionPoint2d_e.dsCommandOptionPoint2d_SetSnpSpc, xint2DCommand, yint2DCommand, out setResult);
			Debug.Print("Set pointer's horizontal and vertical snap values: " + xint2DCommand + ", " + yint2DCommand);
			Debug.Print("Set result: " + setResult);
			Debug.Print(" ");
```

```
			//3D Point
			//Get and set the base point for inserting a drawing
            		dsDoc.GetCommandOptionPoint3D(dsCommandOptionPoint3d_e.dsCommandOptionPoint3d_SetBase, out xint3DCommand, out yint3DCommand, out zint3DCommand, out getResult);
			Debug.Print("Get base point for inserting a drawing: " + xint3DCommand + ", " + yint3DCommand + ", " + zint3DCommand);
			xint3DCommand = 1.0;
			yint3DCommand = 0.0;
			zint3DCommand = 0.0;
            		dsDoc.SetCommandOptionPoint3D(dsCommandOptionPoint3d_e.dsCommandOptionPoint3d_SetBase, xint3DCommand, yint3DCommand, zint3DCommand, out setResult);
			Debug.Print("Set base point for inserting a drawing: " + xint3DCommand + ", " + yint3DCommand + ", " + zint3DCommand);
			Debug.Print("Set result: " + setResult);
			Debug.Print(" ");
```

```
			//String
			//Get and set name of project
            		dsDoc.GetCommandOptionString(dsCommandOptionString_e.dsCommandOptionString_LgcyPROJECTNAME, out valueStringCommand, out getResult);
			Debug.Print("Get project name: " + valueStringCommand);
			valueStringCommand = "New project name";
            		dsDoc.SetCommandOptionString(dsCommandOptionString_e.dsCommandOptionString_LgcyPROJECTNAME, valueStringCommand, out setResult);
			Debug.Print("Set project name: " + valueStringCommand);
			Debug.Print("Set result: " + setResult);
			Debug.Print(" ");
		}
		else
		{
			Debug.Print ("There are no open documents in DraftSight.");
		}
	}
}
```
