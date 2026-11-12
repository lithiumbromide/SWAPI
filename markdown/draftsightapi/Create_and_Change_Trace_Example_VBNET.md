---
title: "Create and Change Trace Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_and_Change_Trace_Example_VBNET.htm"
---

# Create and Change Trace Example (VB.NET)

This example shows how to create a Trace and change its vertex coordinates and thickness.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this code into the VB.NET project.
' 3. Add a reference to
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
' 4. Add a reference to System.Windows.Forms.
' 5. Start DraftSight.
' 6. Press F5.
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
'----------------------------------------------------------------

Imports System
Imports DraftSight.Interop.dsAutomation
Imports System.Runtime.InteropServices
Imports System.Windows.Forms

Module Module1

    Sub Main()
        Dim dsApp As DraftSight.Interop.dsAutomation.Application

        'Connects to DraftSight application
        dsApp = GetObject(, "DraftSight.Application")

        If dsApp Is Nothing Then
            Return
        End If

        'Aborts any command currently running in DraftSight
        'to avoid nested commands
        dsApp.AbortRunningCommand()

        'Gets active document
        Dim dsDoc As Document = dsApp.GetActiveDocument()
        If dsDoc Is Nothing Then
            MessageBox.Show("There are no open documents in DraftSight.")
            Return
        End If

        'Gets Sketch Manager
        Dim dsSketchMgr As SketchManager = dsDoc.GetModel().GetSketchManager()

        'Creates array for Trace vertex coordinates
        Dim CoordinatesArray As Double() = {0, 0, 0, 5, 5, 0, _
         -1, 10, 0, 4, 8, 0}

        'Creates Trace
        Dim dsTrace As Trace = dsSketchMgr.InsertTrace(CoordinatesArray)

        'Sets the Trace vertex coordinates
        dsTrace.SetVertex1Coordinate(1.2, 2.0, 0.0)
        dsTrace.SetVertex2Coordinate(1.1, 2.3, 0.0)
        dsTrace.SetVertex3Coordinate(2.2, 1.0, 0.0)
        dsTrace.SetVertex4Coordinate(2.2, 3.0, 0.0)

        'Sets Trace thickness
        dsTrace.Thickness = 2.0

        'Gets Trace vertex coordinates
        Dim X As Double, Y As Double, Z As Double
        dsTrace.GetVertex1Coordinate(X, Y, Z)
        MessageBox.Show("GetVertex1Coordinate: (" + CType(X, String) + ", " + CType(Y, String) + ", " + CType(Z, String) + ")")

        dsTrace.GetVertex2Coordinate(X, Y, Z)
        MessageBox.Show("GetVertex2Coordinate: (" + CType(X, String) + ", " + CType(Y, String) + ", " + CType(Z, String) + ")")

        dsTrace.GetVertex3Coordinate(X, Y, Z)
        MessageBox.Show("GetVertex3Coordinate: (" + CType(X, String) + ", " + CType(Y, String) + ", " + CType(Z, String) + ")")

        dsTrace.GetVertex3Coordinate(X, Y, Z)
        MessageBox.Show("GetVertex4Coordinate: (" + CType(X, String) + ", " + CType(Y, String) + ", " + CType(Z, String) + ")")

        'Gets Trace thickness
        Dim traceThickness As Double = 0
        traceThickness = dsTrace.Thickness
        MessageBox.Show("Thickness: " + CType(traceThickness, String))

    End Sub

End Module
```
