---
title: "Transform Circle to Region Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Transform_Circle_to_Region_Example_VBA.htm"
---

# Transform Circle to Region Example (VBA)

This example shows how to transform a Circle to a Region.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Start DraftSight.
' 5  Open the Immediate window.
' 6. Run the macro.
'
' Postconditions:
' 1. A Circle is constructed in the drawing document.
' 2. The Circle is transformed to a Region.
' 3. Whether the Region is visible and its perimeter value are printed
'    to the Immediate window.
'----------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim dsApp As DraftSight.Application
    Dim dsDoc As DraftSight.Document
    Dim dsModel As DraftSight.Model
    Dim dsSketchManager As DraftSight.SketchManager
    Dim dsCircle As DraftSight.Circle
    Dim dsSelectionManager As DraftSight.SelectionManager
    Dim dsRegion As DraftSight.Region
    Dim centerX, centerY, centerZ, radius As Double
    Dim status As Boolean
    Dim perimeter As Double
```

```
    ' Connect to DraftSight
    Set dsApp = GetObject(, "DraftSight.Application")
```

```
    ' Abort any command currently running in DraftSight to
    ' avoid nested commands
    dsApp.AbortRunningCommand
```

```
    ' Get active document
    Set dsDoc = dsApp.GetActiveDocument()
    If dsDoc Is Nothing Then
            MsgBox "There are no open documents in DraftSight."
            Exit Sub
    End If
```

```
        ' Get model space
        Set dsModel = dsDoc.GetModel()
```

```
        ' Get Sketch Manager
        Set dsSketchManager = dsModel.GetSketchManager()
```

```
        ' Circle parameters
        centerX = 1#
        centerY = 2#
        centerZ = 0#
        radius = 5#
```

```
        ' Construct Circle
        Set dsCircle = dsSketchManager.InsertCircle(centerX, centerY, centerZ, radius)
```

```
        ' Select Circle
        status = dsCircle.Select(True)
```

```
        If status Then
```

```
            ' Get selected Circle
            Set dsSelectionManager = dsDoc.GetSelectionManager()
            Dim dsObj(0) As Object
            Dim dsType As Long
            Set dsObj(0) = dsSelectionManager.GetSelectedObject(dsSelectionSetType_Current, 0, dsType)
```

```
            ' Make sure that the Circle object was retrieved
            If Not dsObj(0) Is Nothing Then
```

```
                 ' Transform Circle to Region
                 Dim regionObjs As Variant
                 Dim regionObj As Variant
                 dsSketchManager.InsertRegion dsObj, regionObjs
                 Set regionObj = regionObjs(0)
```

```
                 ' Cast to Region
                 Set dsRegion = regionObj
```

```
                 ' Is Region visible?
                 status = dsRegion.Visible
                 Debug.Print ("Is Region visible? " & status)
```

```
                 ' Get perimeter of Region
                 dsRegion.GetPerimeter perimeter
                 Debug.Print ("Perimeter of Region: " & perimeter)

            Else
```

```
                 Debug.Print ("Circle object was not retrieved.")
                 Debug.Print (" ")
```

```
            End If
```

```
        End If
```

```
End Sub
```
