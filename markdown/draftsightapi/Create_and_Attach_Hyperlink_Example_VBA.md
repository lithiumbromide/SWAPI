---
title: "Create and Attach HyperLink Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_and_Attach_Hyperlink_Example_VBA.htm"
---

# Create and Attach HyperLink Example (VBA)

This example shows how to create and attach a HyperLink to a Circle.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Start DraftSight and open a drawing document.
' 5. Run the macro.
'
' Postconditions:
' 1. A Circle is constructed in the drawing document.
' 2. A HyperLink is created and attached to the Circle.
' 3. In DraftSight, put the cursor on the Circle to see the
'    the hyperlink and Ctrl+click to open DraftSight's website.
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
    Dim centerX, centerY, centerZ, radius As Double
```

```
    'Connect to DraftSight
    Set dsApp = GetObject(, "DraftSight.Application")
    'Abort any command currently running in DraftSight
    'to avoid nested commands
    dsApp.AbortRunningCommand
```

```
    'Get active document
    Set dsDoc = dsApp.GetActiveDocument()
    If Not dsDoc Is Nothing Then
```

```
        'Get model space
        Set dsModel = dsDoc.GetModel()
```

```
        'Get Sketch Manager
        Set dsSketchManager = dsModel.GetSketchManager()
```

```
        'Circle parameters
        centerX = 1#
        centerY = 2#
        centerZ = 0#
        radius = 5#
```

```
        'Construct a Circle
        Set dsCircle = dsSketchManager.InsertCircle(centerX, centerY, centerZ, radius)
```

```
        'Create and attach HyperLink to Circle
        Dim startCornerX As Double
        startCornerX = 0#
        Dim startCornerY As Double
        startCornerY = 0#
        Dim startCornerZ As Double
        startCornerZ = 0#
        Dim oppositeCornerX As Double
        startCornerX = 0#
        Dim oppositeCornerY As Double
        startCornerY = 0#
        Dim oppositeCornerZ As Double
        startCornerZ = 0#
        Dim hyperLinkAddress As String
        hyperLinkAddress = "http://www.3ds.com/products/draftsight/free-cad-software/"
        Dim description As String
        description = "DraftSight's website"
        Dim ds3DPolyLine As DraftSight.PolyLine3D
        Dim dsHyperLink As DraftSight.HyperLink
```

```
        Set dsHyperLink = dsSketchManager.AttachLinkToArea(startCornerX, startCornerY, startCornerZ, oppositeCornerX, oppositeCornerY, oppositeCornerZ, hyperLinkAddress, description, ds3DPolyLine)
        dsCircle.SetHyperLink dsHyperLink
```

```
    Else
```

```
        MsgBox "There are no open documents in DraftSight."
```

```
    End If
End Sub
```
