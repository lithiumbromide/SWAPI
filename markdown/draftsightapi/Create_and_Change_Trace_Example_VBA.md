---
title: "Create and Change Trace Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_and_Change_Trace_Example_VBA.htm"
---

# Create and Change Trace Example (VBA)

This example shows how to create a Trace and change its vertex coordinates and thickness.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this code into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Start DraftSight.
' 5. Press F5.
'
' Postconditions:
' 1. Connects to DraftSight.
' 2. Gets the active document.
' 3. Creates a Trace.
' 4. Sets the vertex coordinates of the Trace.
' 5. Sets the thickness of the Trace.
' 6. Gets the vertex coordinates of the Trace.
'    Click OK to close each message box.
' 7. Gets the thickness of the Trace.
'    Click OK to close the message box.
'--------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim dsApp As DraftSight.Application
```

```
    'Connects to DraftSight
    Set dsApp = GetObject(, "DraftSight.Application")
    If dsApp Is Nothing Then
        Return
    End If
```

```
    'Aborts any command currently running in DraftSight
    'to avoid nested commands
    dsApp.AbortRunningCommand
```

```
    'Gets active document
    Dim dsDoc As DraftSight.Document
    Set dsDoc = dsApp.GetActiveDocument
    If dsDoc Is Nothing Then
        MsgBox "There are no open documents in DraftSight."
        Return
    End If
```

```
    'Gets Sketch Manager
    Dim dsSketchMgr As DraftSight.SketchManager
    Set dsSketchMgr = dsDoc.GetModel.GetSketchManager
```

```
    'Creates array of Trace vertex coordinates
    Dim CoordinatesArray(11) As Double
    CoordinatesArray(0) = 0
    CoordinatesArray(1) = 0
    CoordinatesArray(2) = 0
    CoordinatesArray(3) = 5
    CoordinatesArray(4) = 5
    CoordinatesArray(5) = 0
    CoordinatesArray(6) = -1
    CoordinatesArray(7) = 10
    CoordinatesArray(8) = 0
    CoordinatesArray(9) = 4
    CoordinatesArray(10) = 8
    CoordinatesArray(11) = 0
```

```
    'Creates Trace
    Dim dsTrace As DraftSight.Trace
    Set dsTrace = dsSketchMgr.InsertTrace(CoordinatesArray)
```

```
    'Sets Trace vertex coordinates
    dsTrace.SetVertex1Coordinate 1.2, 2#, 0#
    dsTrace.SetVertex2Coordinate 1.1, 2.3, 0#
    dsTrace.SetVertex3Coordinate 2.2, 1#, 0#
    dsTrace.SetVertex4Coordinate 2.2, 3#, 0#
```

```
    'Sets Trace thickness
    dsTrace.Thickness = 2#
```

```
    'Gets Trace vertex coordinates
    Dim X As Double
    Dim Y As Double
    Dim Z As Double
    dsTrace.GetVertex1Coordinate X, Y, Z
    MsgBox "GetVertex1Coordinate: (" & X & ", " & Y & ", " & Z & ")"
```

```
    dsTrace.GetVertex2Coordinate X, Y, Z
    MsgBox "GetVertex2Coordinate: (" & X & ", " & Y & ", " & Z & ")"
```

```
    dsTrace.GetVertex3Coordinate X, Y, Z
    MsgBox "GetVertex3Coordinate: (" & X & ", " & Y & ", " & Z & ")"
```

```
    dsTrace.GetVertex4Coordinate X, Y, Z
    MsgBox "GetVertex4Coordinate: (" & X & ", " & Y & ", " & Z & ")"
```

```
    'Gets Trace thickness
    MsgBox "Thickness: " & dsTrace.Thickness
```

```
End Sub
```
