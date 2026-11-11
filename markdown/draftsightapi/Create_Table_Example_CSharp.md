---
title: "Create Table Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Table_Example_CSharp.htm"
---

# Create Table Example (C#)

This example shows how to change the transparency of the active Layer, create a TableStyle and Table, and change the background colors of the top row and a cell in the Table.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the C# IDE.
// 3. Add a reference to:
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
// 4. Open the Immediate window.
// 5. Add references to System and System.Windows.Forms.
// 6. Start DraftSight and open a new document.
// 7. Press F5.
//
//
// Postconditions:
// 1. Gets the transparency object for the active Layer and prints its
//    transparency percentage to the Immediate window.
// 2. Changes the transparency percentage of the active Layer and prints
//    its new percentage to the Immediate window.
// 3. Creates and activates a new TableStyle named Sample Table Style.
// 4. Inserts a Table and applies the Sample Table Style TableStyle.
// 5. Gets the transparency object for the Table.
// 6. Prints whether the transparency object for the Table is ByLayer.
// 7. If not, then changes and updates the transparency object
//    of the Table to ByLayer.
// 8. Changes the top row's background color.
// 9. Changes the background color of the cell in the second row
//    and second column to match the top row's background color.
//10. Prints the name of the TableStyle to the Immediate window.
//11. Examine the drawing and the Immediate window.
//----------------------------------------------------------------
```

```
using DraftSight.Interop.dsAutomation;
using System;
using System.Windows.Forms;
using System.Runtime.InteropServices;
using System.Diagnostics;

static class Module1{

    public static void Main()	{

		DraftSight.Interop.dsAutomation.Application dsApp;

		//Connect to DraftSight application
        		dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");

		//Abort any command currently running in DraftSight
		//to avoid nested commands
		dsApp.AbortRunningCommand();

		//Get active document
		Document dsDoc = default(Document);
		dsDoc = dsApp.GetActiveDocument();
		if (dsDoc == null) {
			MessageBox.Show("There are no open documents in DraftSight.");
			return;
		}
```

```
       		//Get how transparency is defined
        		LayerManager dsLayerManager = default(LayerManager);
        		Layer dsLayer = default(Layer);
        		dsLayerManager = dsDoc.GetLayerManager();
        		dsLayer = dsLayerManager.GetActiveLayer();
        		Debug.Print("Transparency percentage for active Layer: " + Convert.ToString(dsLayer.Transparency));
        		//Set new transparency percentage for the active Layer
        		dsLayer.Transparency = 50;
        		Debug.Print("New transparency percentage for active Layer: " + Convert.ToString(dsLayer.Transparency));

		//Get the TableStyle Manager
		TableStyleManager dsTableStyleManager = default(TableStyleManager);
		dsTableStyleManager = dsDoc.GetTableStyleManager();

		//Create the TableStyle
		TableStyle dsTableStyle = default(TableStyle);
		string sampleTableStyle = null;
		sampleTableStyle = "Sample Table Style";
        		dsCreateObjectResult_e result;
        		dsTableStyleManager.CreateTableStyle(sampleTableStyle, out dsTableStyle, out result);

		//Set the TableStyle styles
		//Create the Table in a downward direction
		dsTableStyle.HeaderOrientation = dsTableHeaderOrientation_e.dsTableHeaderOrientation_Down;

		//Set the Colors for the Table backgrounds
		Color dsColorHeader = default(Color);
		Color dsColorData = default(Color);
		Color dsColorTitle = default(Color);
```

```
        		dsColorHeader = dsTableStyle.GetBackgroundColor(dsTableCellType_e.dsTableCellType_Header);
        		dsColorHeader.SetNamedColor(dsNamedColor_e.dsNamedColor_Cyan);
        		dsTableStyle.SetBackgroundColor(dsTableCellType_e.dsTableCellType_Header, dsColorHeader);

        		dsColorData = dsTableStyle.GetBackgroundColor(dsTableCellType_e.dsTableCellType_Data);
		dsColorData.SetNamedColor(dsNamedColor_e.dsNamedColor_Green);
		dsTableStyle.SetBackgroundColor(dsTableCellType_e.dsTableCellType_Data, dsColorData);

		dsColorTitle = dsTableStyle.GetBackgroundColor(dsTableCellType_e.dsTableCellType_Title);
		dsColorTitle.SetNamedColor(dsNamedColor_e.dsNamedColor_White);
		dsTableStyle.SetBackgroundColor(dsTableCellType_e.dsTableCellType_Title, dsColorTitle);
```

```
		//Activate the TableStyle
		dsTableStyle.Activate();

		//Get the model document
		Model dsModel = default(Model);
		dsModel = dsDoc.GetModel();

		//Get the Sketch Manager
		SketchManager dsSketchManager = default(SketchManager);
		dsSketchManager = dsModel.GetSketchManager();

		//Insert the Table
		Table dsTable = default(Table);
		double x = 0;
		x = 6;
		double y = 0;
		y = 6;
		int row = 0;
		row = 4;
		int col = 0;
		col = 5;
		double rowHeight = 0;
		rowHeight = 2;
		double colWidth = 0;
		colWidth = 4;
		dsTable = dsSketchManager.InsertTable(x, y, row, col, rowHeight, colWidth, dsTableCellType_e.dsTableCellType_Title, dsTableCellType_e.dsTableCellType_Header, dsTableCellType_e.dsTableCellType_Data);
```

```
       		//Get transparency object for Table
        		Transparency dsTransparency = default(Transparency);
        		dsTransparency = dsTable.Transparency;
        		//Find out if Table's transparency is ByLayer
        		Debug.Print ("Transparency defined ByLayer: " + Convert.ToString(dsTransparency.IsByLayer()));
        		//If not, then change Table's transparency to ByLayer and
        		//update Table's transparency object
        		if (dsTransparency.IsByLayer() == false)
        		{
            		dsTransparency.SetByLayer();
            		Debug.Print("Transparency now ByLayer: " + Convert.ToString(dsTransparency.IsByLayer()));
            		//Update Table's transparency object
            		dsTable.Transparency = dsTransparency;
        		}

        		//Change Table's top row's background color
        		dsColorTitle.SetNamedColor(dsNamedColor_e.dsNamedColor_Yellow);
        		dsTable.SetBackgroundColor(dsTableCellType_e.dsTableCellType_Title, dsColorTitle);
        		//Change background color of cell in second row and
        		//second column to match the top row's background color
        		dsTable.SetCellBackgroundColor(1,1,dsColorTitle);

		//Get the name of the TableStyle for the just-inserted Table
		Debug.Print("TableStyle applied to this table: " + dsTableStyle.Name);
```

```
	        	//Zoom to fit
        		dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, null, null);

	}

}
```
