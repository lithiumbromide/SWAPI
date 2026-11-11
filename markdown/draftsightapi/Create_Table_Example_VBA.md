---
title: "Create Table Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Table_Example_VBA.htm"
---

# Create Table Example (VBA)

This example shows how to change the transparency of the active Layer, create a TableStyle and Table, and change the background colors of the top row and a cell in the Table.

```
'-------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Open the Immediate window.
' 5. Start DraftSight and open a new document.
' 6. Run the macro.
'
' Postconditions:
' 1. Gets the transparency object for the active Layer and prints its
'    transparency percentage to the Immediate window.
' 2. Changes the transparency percentage of the active Layer and prints
'    its new percentage to the Immediate window.
' 3. Creates and activates a new TableStyle named Sample Table Style.
' 4. Inserts a Table and applies the Sample Table Style TableStyle.
' 5. Gets the transparency object for the Table.
' 6. Prints whether the transparency object for the Table is ByLayer.
' 7. If not, then changes and updates the transparency object
'    of the Table to ByLayer.
' 8. Changes the top row's background color.
' 9. Changes the background color of the cell in the second row
'    and second column to match the top row's background color.
'10. Prints the name of the TableStyle to the Immediate window.
'11. Examine the drawing and the Immediate window.
'----------------------------------------------------------------
```

```
Option Explicit
```

```
    Sub main()
```

```
        Dim dsApp As DraftSight.Application
```

```
        'Connect to DraftSight application
        Set dsApp = GetObject(, "DraftSight.Application")
```

```
        'Abort any command currently running in DraftSight
        'to avoid nested commands
        dsApp.AbortRunningCommand
```

```
        'Get active document
        Dim dsDoc As DraftSight.Document
        Set dsDoc = dsApp.GetActiveDocument()
        If dsDoc Is Nothing Then
            MsgBox ("There are no open documents in DraftSight.")
            Return
        End If
```

```
        'Get how transparency is defined
        Dim dsLayerManager As DraftSight.LayerManager
        Dim dsLayer As DraftSight.Layer
        Set dsLayerManager = dsDoc.GetLayerManager
        Set dsLayer = dsLayerManager.GetActiveLayer
        Debug.Print "Transparency percentage for active Layer: " & dsLayer.Transparency
        'Set new transparency percentage for the active Layer
        dsLayer.Transparency = 50
        Debug.Print "New transparency percentage for active Layer: " & dsLayer.Transparency
```

```
        'Get the TableStyle Manager
        Dim dsTableStyleManager As DraftSight.TableStyleManager
        Set dsTableStyleManager = dsDoc.GetTableStyleManager
```

```
        'Create the TableStyle
        Dim dsTableStyle As DraftSight.TableStyle
        Dim sampleTableStyle As String
        Dim status As Long
        sampleTableStyle = "Sample Table Style"
        dsTableStyleManager.CreateTableStyle sampleTableStyle, dsTableStyle, status
```

```
        'Set the TableStyle styles
        'Create the Table in a downward direction
        dsTableStyle.HeaderOrientation = dsTableHeaderOrientation_Down
```

```
        'Set the Colors for the Table backgrounds
        Dim dsColorHeader As DraftSight.Color
        Dim dsColorData As DraftSight.Color
        Dim dsColorTitle As DraftSight.Color
```

```
        Set dsColorHeader = dsTableStyle.GetBackgroundColor(dsTableCellType_Header)
        dsColorHeader.SetNamedColor dsNamedColor_e.dsNamedColor_Cyan
        dsTableStyle.SetBackgroundColor dsTableCellType_Header, dsColorHeader
```

```
        Set dsColorData = dsTableStyle.GetBackgroundColor(dsTableCellType_Data)
        dsColorData.SetNamedColor dsNamedColor_e.dsNamedColor_Green
        dsTableStyle.SetBackgroundColor dsTableCellType_Data, dsColorData
```

```
        Set dsColorTitle = dsTableStyle.GetBackgroundColor(dsTableCellType_Title)
        dsColorTitle.SetNamedColor dsNamedColor_e.dsNamedColor_White
        dsTableStyle.SetBackgroundColor dsTableCellType_Title, dsColorTitle
```

```
        'Activate the TableStyle
        dsTableStyle.Activate
```

```
        'Get the model document
        Dim dsModel As DraftSight.Model
        Set dsModel = dsDoc.GetModel
```

```
        'Get the Sketch Manager
        Dim dsSketchManager As DraftSight.SketchManager
        Set dsSketchManager = dsModel.GetSketchManager
```

```
        'Insert the Table
        Dim dsTable As DraftSight.Table
        Dim x As Double
        x = 6
        Dim y As Double
        y = 6
        Dim row As Long
        row = 4
        Dim col As Long
        col = 5
        Dim rowHeight As Double
        rowHeight = 2
        Dim colWidth As Double
        colWidth = 4
 	Set dsTable = dsSketchManager.InsertTable(x, y, row, col, rowHeight, colWidth, dsTableCellType_Title, dsTableCellType_Header, dsTableCellType_Data)
```

```
        'Get transparency object for Table
        Dim dsTransparency As DraftSight.Transparency
        Set dsTransparency = dsTable.Transparency
        'Find out if Table's transparency is ByLayer
        Debug.Print "Transparency defined ByLayer: " & dsTransparency.IsByLayer
        'If not, then change Table's transparency to ByLayer and
        'update Table's transparency object
        If Not dsTransparency.IsByLayer Then
            dsTransparency.SetByLayer
            Debug.Print "Transparency now ByLayer: " & dsTransparency.IsByLayer
            'Update Table's transparency object
	    dsTable.Transparency = dsTransparency
        End If
```

```
        'Change Table's top row's background color
        dsColorTitle.SetNamedColor (dsNamedColor_Yellow)
        dsTable.SetBackgroundColor dsTableCellType_Title, dsColorTitle
        'Change background color of cell in second row and
        'second column to match the top row's background color
        dsTable.SetCellBackgroundColor 1, 1, dsColorTitle

        'Get the name of the TableStyle for the just-inserted Table
        Debug.Print ("TableStyle applied to this table: " & dsTableStyle.Name)

        dsApp.Zoom dsZoomRange_Fit, Nothing, Nothing

End Sub
```
