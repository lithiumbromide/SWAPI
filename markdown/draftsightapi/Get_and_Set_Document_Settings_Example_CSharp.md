---
title: "Get and Set Document Settings Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_and_Set_Document_Settings_Example_CSharp.htm"
---

# Get and Set Document Settings Example (C#)

This example shows how to get and set document settings.

```
//--------------------------------------------------------------
//Preconditions:
// 1. Create a Visual C# Console App (.NET Framework) in Visual Studio.
// 2. Copy and paste this code into the program file.
// 3. Add a reference to:
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
// 4. Start DraftSight and open a drawing.
// 5. Add references to System and System.Windows.Forms.
// 6. Start debugging the project.
//
//Postconditions: Message boxes pop up verifying that
//document properties are reset. Read the text in each
//message box before clicking OK to close it.
//----------------------------------------------------------------
```

```
using System;
using DraftSight.Interop.dsAutomation;
using System.Windows.Forms;
using System.Runtime.InteropServices;
```

```
static class Module1
{
```

```
    static DraftSight.Interop.dsAutomation.Application dsApp;
    static Document dsDoc;
```

```
    static string dsDocName;
    public static void Main()
    {
		//Connect to DraftSight
        	dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");
		dsApp.AbortRunningCommand(); // abort any command currently running in DraftSight to avoid nested commands
```

```
		//Get active document
		dsDoc = dsApp.GetActiveDocument();
```

```
		if (dsDoc != null)
                {
			//Get and set document settings
			GetSetDocSettings(dsDoc);
```

```
		}
                else
                {
			MessageBox.Show("There are no open documents in DraftSight.");
		}
```

```
    }
```

```
    public static void GetSetDocSettings(Document dsDoc)
    {
        //Set and get dimension scale property of document
        TestDimensionScale(dsDoc);
```

```
        //Set and get angle unit expression for document
        TestAngleUnitExpression(dsDoc);
```

```
        //Set and get base angle for document
        TestBaseAngle(dsDoc);
```

```
        //Set and get length unit expression for document
        TestLengthUnitExpression(dsDoc);
```

```
        //Set and get scale unit of the document
        TestScaleUnit(dsDoc);
```

```
        //Check whether document is active
        if (dsDoc.IsActive())
        {
            MessageBox.Show(dsDoc.GetPathName() + " document is currently active in DraftSight.");
        }
        else
        {
            MessageBox.Show(dsDoc.GetPathName() + " document is not currently active in DraftSight.");
        }
```

```
        //Check whether document is dirty
        if (dsDoc.IsDirty())
        {
            MessageBox.Show(dsDoc.GetPathName() + " document was modified since opened.");
        }
        else
        {
            MessageBox.Show(dsDoc.GetPathName() + " document was not modified since opened.");
        }
	//Set document dirty
	dsDoc.SetDirty();

	if (dsDoc.IsDirty())
	{
		MessageBox.Show(dsDoc.GetPathName() + " document was successfully set dirty.");
	}
	else
	{
		MessageBox.Show(dsDoc.GetPathName() + " document was not set dirty.");
	}
```

```
    }
    public static void TestDimensionScale(Document dsDoc)
    {
        double dimScale = 0;
        double precision = 0;
```

```
        precision = 1E-09;
```

```
        //Set IDocument.DimensionScale property
        dimScale = 0.1;
        dsDoc.DimensionScale = dimScale;
```

```
        if (Math.Abs(dimScale - dsDoc.DimensionScale) > precision)
        {
            MessageBox.Show("Failed to set dimension scale property of document to " + dimScale);
        }
    }
```

```
    public static void TestAngleUnitExpression(Document dsDoc)
    {
        dsAngleType_e newAngType = default(dsAngleType_e);
        dsAngleType_e getAngType = default(dsAngleType_e);
        dsUnitPrecision_e newUnitPrecision = default(dsUnitPrecision_e);
        dsUnitPrecision_e getUnitPrecision = default(dsUnitPrecision_e);
```

```
        //Set IDocument.SetAngleUnitExpression for document
        newAngType = dsAngleType_e.dsAngleType_Radians;
        newUnitPrecision = dsUnitPrecision_e.dsUnitPrecision_8;
```

```
        dsDoc.SetAngleUnitExpression(newAngType, newUnitPrecision);
```

```
        //Get IDocument.GetAngleUnitExpression for document
        dsDoc.GetAngleUnitExpression(out getAngType, out getUnitPrecision);
```

```
        if (getAngType == newAngType)
        {
            MessageBox.Show("Set angle type property of document to " + newAngType + ".");
        }
```

```
        if (getUnitPrecision == newUnitPrecision)
        {
            MessageBox.Show("Set unit precision property of document to " + newUnitPrecision + ".");
        }
```

```
    }
    public static void TestBaseAngle(Document dsDoc)
    {
        double newBaseAngle = 0;
        bool newClockwise = false;
        double baseAngle = 0;
        bool clockwise = false;
        double precision = 0;
```

```
        precision = 1E-09;
```

```
        //Set IDocument.SetBaseAngle property for document
        newBaseAngle = 0.0;
        newClockwise = true;
```

```
        dsDoc.SetBaseAngle(newBaseAngle, newClockwise);
```

```
        //Get IDocument.GetBaseAngle for document
        dsDoc.GetBaseAngle(out baseAngle, out clockwise);
```

```
        if (Math.Abs(newBaseAngle - baseAngle) < precision)
        {
            MessageBox.Show("Set base angle property of document to " + newBaseAngle + ".");
        }
```

```
        if (newClockwise == clockwise)
        {
            MessageBox.Show("Set clockwise property of document.");
        }
```

```
    }
    public static void TestLengthUnitExpression(Document dsDoc)
    {
        dsLengthType_e newLengthType = default(dsLengthType_e);
        dsUnitPrecision_e newUnitPrecision = default(dsUnitPrecision_e);
        dsLengthType_e lengthType = default(dsLengthType_e);
        dsUnitPrecision_e unitPrecision = default(dsUnitPrecision_e);
```

```
        //Set IDocument.SetLengthUnitExpression for document
        newLengthType = dsLengthType_e.dsLengthType_Engineering;
        newUnitPrecision = dsUnitPrecision_e.dsUnitPrecision_5;
        dsDoc.SetLengthUnitExpression(newLengthType, newUnitPrecision);
```

```
        //Get IDocument.GetLengthUnitExpression for document and
        //verify if a value is correct
        dsDoc.GetLengthUnitExpression(out lengthType, out unitPrecision);
```

```
        if (newLengthType == lengthType)
        {
            MessageBox.Show("Set length type property of document to " + newLengthType + ".");
        }
```

```
        if (newUnitPrecision == unitPrecision)
        {
            MessageBox.Show("Set unit precision property of document to " + newUnitPrecision + ".");
        }
    }
```

```
    public static void TestScaleUnit(Document dsDoc)
    {
        dsScaleUnit_e newScaleUnit = default(dsScaleUnit_e);
        dsScaleUnit_e scaleUnit = default(dsScaleUnit_e);
```

```
        //Set IDocument.ScaleUnit property for document
        newScaleUnit = dsScaleUnit_e.dsScaleUnit_Yards;
        dsDoc.ScaleUnit = newScaleUnit;
```

```
        //Get IDocument.ScaleUnit property for document and verify if a value is correct
        scaleUnit = dsDoc.ScaleUnit;
```

```
        if (scaleUnit == newScaleUnit)
        {
            MessageBox.Show("Set scale unit property of document to " + newScaleUnit + ".");
        }
    }
```

```
}
```
