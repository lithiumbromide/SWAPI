---
title: "Manage Custom Coordinate Systems Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Manage_Default_and_Named_Custom_Coordinate_Systems_Example_VBA.htm"
---

# Manage Custom Coordinate Systems Example (VBA)

This example shows how to manage World, default, and named custom coordinate systems.

```vb
 '-----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Create a VBA macro in a software product in which VBA is
 '    embedded.
 ' 2. Copy and paste this example into the Visual Basic IDE.
 ' 3. Add a reference to the DraftSight type library,
 '    install_dir\bin\dsAutomation.dll.
 ' 5. Start DraftSight and open a new document.
 ' 6. Set a breakpoint in Main() and step through the macro.
 '
 ' Postconditions:
 ' 1. Inspect the Immediate Window.
 ' 2. A new named custom coordinate system is created, renamed, and removed.
 '---------------------------------------------------------------------------
Dim dsApp As DraftSight.Application
 Dim dsDoc As Document
 Option Explicit
     Sub Main()
         'Connect to DraftSight
         Set dsApp = GetObject(, "DraftSight.Application")
         'Abort any command currently running in DraftSight
         'to avoid nested commands
         dsApp.AbortRunningCommand
        'Get active document
         Set dsDoc = dsApp.GetActiveDocument()
         If dsDoc Is Nothing Then
             MsgBox ("There are no opened documents in DraftSight.")
             Return
         End If
        'Get custom coordinate system manager
         Dim dsCCSMgr As DraftSight.CustomCoordinateSystemManager
         Set dsCCSMgr = dsDoc.GetCustomCoordinateSystemManager()
        Call UsageOfDefaultCustomCoordinateSystems(dsCCSMgr)
        Call UsageOfNamedCustomCoordinateSystems(dsCCSMgr)
     End Sub
    Sub UsageOfDefaultCustomCoordinateSystems(dsCCSMgr As DraftSight.CustomCoordinateSystemManager)
         'Get World Coordinate System
         Dim dsWorldCCS As DraftSight.CustomCoordinateSystem
         Set dsWorldCCS = dsCCSMgr.GetWorldCustomCoordinateSystem()
        Debug.Print (" ")
         Debug.Print ("Get WCS.")
        Call PrintCoordinateSystemParameters(dsWorldCCS)
        'Get default Bottom custom coordinate system
         Dim dsBottomCCS As DraftSight.CustomCoordinateSystem
         Set dsBottomCCS = dsCCSMgr.GetDefaultCustomCoordinateSystem(dsDefaultCustomCoordinateSystem_e.dsDefaultCustomCoordinateSystem_Bottom)
        Debug.Print (" ")
         Debug.Print ("Get default bottom CCS.")
        Call PrintCoordinateSystemParameters(dsBottomCCS)
        'Activate default bottom custom coordinate system
         dsBottomCCS.Activate
        'Get previous CCS; it should be WCS.
         Dim dsPreviousCCS As DraftSight.CustomCoordinateSystem
         Set dsPreviousCCS = dsCCSMgr.GetPreviousCustomCoordinateSystem()
        Debug.Print (" ")
         Debug.Print ("Get previous CCS.")
        Call PrintCoordinateSystemParameters(dsPreviousCCS)
        'Get active CCS; it should be bottom CCS.
         Dim dsActiveCCS As DraftSight.CustomCoordinateSystem
         Set dsActiveCCS = dsCCSMgr.GetActiveCustomCoordinateSystem()
        Debug.Print (" ")
         Debug.Print ("Get active CCS.")
        Call PrintCoordinateSystemParameters(dsActiveCCS)
        'The active custom coordinate system can be modified
         'Change origin of active custom coordinate system
         Dim originX As Double
         originX = 2
         Dim originY As Double
         originY = 3
         Dim originZ As Double
         originZ = 1
         dsCCSMgr.SetActiveCustomCoordinateSystemOrigin originX, originY, originZ
        Debug.Print (" ")
         Debug.Print ("Origin of active CCS has been changed.")
        Call PrintCoordinateSystemParameters(dsActiveCCS)
        'Align custom coordinate system by entity
         Call AlignActiveCCSByEntity(dsCCSMgr)
        Debug.Print (" ")
         Debug.Print ("The active CCS has been aligned by line entity.")
        Call PrintCoordinateSystemParameters(dsActiveCCS)
     End Sub
    Sub AlignActiveCCSByEntity(dsCCSMgr As DraftSight.CustomCoordinateSystemManager)
         'Get model space
         Dim dsModel As DraftSight.Model
         Set dsModel = dsDoc.GetModel()
        'Get sketch manager
         Dim dsSketchMgr As DraftSight.SketchManager
         Set dsSketchMgr = dsModel.GetSketchManager()
        'Draw a line entity
         Dim startPoint(0 To 2) As Double
         startPoint(0) = 5
         startPoint(1) = 5
         startPoint(2) = 0
         Dim endPoint(0 To 2) As Double
         endPoint(0) = 12
         endPoint(1) = 15
         endPoint(2) = 0
         Dim dsLine As DraftSight.Line
         Set dsLine = dsSketchMgr.InsertLine(startPoint(0), startPoint(1), startPoint(2), endPoint(0), endPoint(1), endPoint(2))
        'Align active CCS by the created line entity
         dsCCSMgr.AlignActiveCustomCoordinateSystemByEntity dsLine, startPoint
     End Sub
    Sub UsageOfNamedCustomCoordinateSystems(dsCCSMgr As DraftSight.CustomCoordinateSystemManager)
         'Get view manager
         Dim dsViewManager As DraftSight.ViewManager
         Set dsViewManager = dsDoc.GetViewManager()
        'Set isometric view
         dsViewManager.SetPredefinedView (dsPredefinedView_e.dsPredefinedView_SWIsometric)
        'Zoom extents
         dsApp.Zoom dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing
        'Create a new named CCS by saving the active view as new CCS
         Dim name As String
         name = "newCCS"
         Dim dsNewCCS As DraftSight.CustomCoordinateSystem
         Dim saveViewResult As dsCreateObjectResult_e
         saveViewResult = dsCCSMgr.SaveActiveViewAs(name, dsNewCCS)

        Debug.Print (" ")
         Debug.Print ("New named CCS has been created by saving active view as new CCS.")
        Call PrintCoordinateSystemParameters(dsNewCCS)
        'Rename new CCS
         Dim newName As String
         newName = name & "_Changed"
         If RenameCCS(dsNewCCS, newName) Then
             Debug.Print (" ")
             Debug.Print ("The CCS has been renamed.")
            Call PrintCoordinateSystemParameters(dsNewCCS)
            'Print named CCS list
             Call PrintNamedCCSList(dsCCSMgr)
            'Remove the created CCS
             dsCCSMgr.RemoveCustomCoordinateSystem (newName)
            'Print named CCS list
             Call PrintNamedCCSList(dsCCSMgr)
         End If

    End Sub
    Sub PrintNamedCCSList(dsCCSMgr As DraftSight.CustomCoordinateSystemManager)
         Dim namedCCSObj As Variant
         namedCCSObj = dsCCSMgr.GetNamedCustomCoordinateSystemList
         Dim i As Long
         If IsEmpty(namedCCSObj) Then
             Debug.Print (" ")
             Debug.Print ("There are no named custom coordinate systems.")
         Else
             Debug.Print (" ")
             Debug.Print ("Named custom coordinate systems:")
             For i = 0 To UBound(namedCCSObj)
                 Debug.Print (namedCCSObj(i))
             Next
         End If
     End Sub
    Function RenameCCS(dsNewCCS As DraftSight.CustomCoordinateSystem, newName As String)
         Dim renameResult As dsCreateObjectResult_e
         renameResult = dsNewCCS.Rename(newName)
         If dsCreateObjectResult_Success <> renameResult Then
             MsgBox ("Failed to rename custom coordinate system. New name should be " + newName + " Renaming result: " + renameResult)
             RenameCCS = False
         End If
         RenameCCS = True
     End Function
    Sub PrintCoordinateSystemParameters(dsCustomCoordinateSystem As DraftSight.CustomCoordinateSystem)
         Debug.Print ("Custom Coordinate System Parameters:")
        Debug.Print ("Name = " & dsCustomCoordinateSystem.GetName())
        Dim isDefault As Boolean
         Dim defaultFlag As dsDefaultCustomCoordinateSystem_e
         dsCustomCoordinateSystem.GetDefaultCustomCoordinateSystemFlag isDefault, defaultFlag
         Debug.Print ("IsDefault = " & isDefault)
         Debug.Print ("DefaultCustomCoordinateSystemFlag = " & defaultFlag)
        Dim x As Double, y As Double, z As Double
         dsCustomCoordinateSystem.GetOrigin x, y, z
         Debug.Print ("Origin: " & x & ", " & y & ", " & z)
        dsCustomCoordinateSystem.GetXAxisDirection x, y, z
         Debug.Print ("X-Axis Direction: " & x & ", " & y & ", " & z)
        dsCustomCoordinateSystem.GetYAxisDirection x, y, z
         Debug.Print ("Y-Axis Direction: " & x & ", " & y & ", " & z)
        dsCustomCoordinateSystem.GetZAxisDirection x, y, z
         Debug.Print ("Z-Axis Direction: " & x & ", " & y & ", " & z)
     End Sub
```
