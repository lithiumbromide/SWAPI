---
title: "Transform Circle to Region Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Transform_Circle_to_Region_Example_VBNET.htm"
---

# Transform Circle to Region Example (VB.NET)

This example shows how to transform a Circle to a Region.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this example into the VB.NET IDE.
' 3. Add a reference to:
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll
' 4. Add references to System and System.Windows.Forms.
' 5. Start DraftSight.
' 6. Open the Immediate window.
' 7. Press F5 to debug the project.
'
' Postconditions:
' 1. A Circle is constructed in the drawing document.
' 2. The Circle is transformed to a Region.
' 3. Whether the Region is visible and its perimeter value are
'    printed to the Immediate window.
'----------------------------------------------------------------
Imports DraftSight.Interop.dsAutomation
Imports System.Windows.Forms
Imports System.Runtime.InteropServices

Module Module1

    Sub Main()

        Dim dsApp As DraftSight.Interop.dsAutomation.Application
        Dim dsDoc As Document
        Dim dsModel As Model
        Dim dsSketchManager As SketchManager
        Dim dsSelectionManager As SelectionManager
        Dim dsCircle As Circle
        Dim dsRegions As Object() = Nothing
        Dim centerX, centerY, centerZ, radius, perimeter As Double
        Dim status As Boolean
        Dim objType As Integer

        ' Connect to DraftSight
        dsApp = GetObject(, "DraftSight.Application")

        ' Abort any command currently running in DraftSight to
        ' avoid nested commands
        dsApp.AbortRunningCommand()

        ' Get active document
        dsDoc = dsApp.GetActiveDocument()

        ' Make sure there is an open document
        If dsDoc Is Nothing Then
            MessageBox.Show("There are no open documents in DraftSight.")
            Return
        End If

        ' Get model space
        dsModel = dsDoc.GetModel()

        ' Get Sketch Manager
        dsSketchManager = dsModel.GetSketchManager()

        ' Circle parameters
        centerX = 1.0#
        centerY = 2.0#
        centerZ = 0.0#
        radius = 5.0#

        ' Construct a Circle
        dsCircle = dsSketchManager.InsertCircle(centerX, centerY, centerZ, radius)

        ' Select the Circle
        status = dsCircle.Select(True)

        If status Then

            ' Get selected Circle
            dsSelectionManager = dsDoc.GetSelectionManager
            Dim dsObj As Object = dsSelectionManager.GetSelectedObject(dsSelectionSetType_e.dsSelectionSetType_Current, 0, objType)
            Dim dsSelObj As DispatchWrapper() = New DispatchWrapper(0) {}
            dsSelObj(0) = New DispatchWrapper(dsObj)

            ' Transform Circle to Region
            dsSketchManager.InsertRegion(dsSelObj, dsRegions)
            Dim dsRegion As Region = dsRegions(0)

            ' Is Region visible?
            status = dsRegion.Visible
            Debug.Print("Is Region visible? " & status)

            ' Get perimeter of Region
            dsRegion.GetPerimeter(perimeter)
            Debug.Print("Perimeter of Region: " & perimeter)

        End If

    End Sub

End Module
```
