---
title: "Manage Custom Coordinate Systems Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Manage_Default_and_Named_Custom_Coordinate_Systems_Example_VBNET.htm"
---

# Manage Custom Coordinate Systems Example (VB.NET)

This example shows how to manage World, default, and named custom coordinate systems.

```vb
 '-----------------------------------------------------------------------------
 'Preconditions:
 ' 1. Create a VB.NET Windows console project.
 ' 2. Copy and paste this project into the VB.NET IDE.
 ' 3. Add a reference to:
 '    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.
 ' 4. Add references to System and System.Windows.Forms.
 ' 5. Start DraftSight.
 ' 6. Set a breakpoint in Main() and step through the macro.
 '
 'Postconditions:
 '1. Inspect the Immediate Window.
 '2. A new named custom coordinate system is created, renamed, and removed.
 '---------------------------------------------------------------------------
 Imports System.Collections.Generic
 Imports System.Text
 Imports DraftSight.Interop.dsAutomation
 Imports System.Windows.Forms
 Imports System.Runtime.InteropServices
 Imports System.Diagnostics

 Module Module1
     Dim dsApp As DraftSight.Interop.dsAutomation.Application
     Dim dsDoc As Document

     Sub Main(ByVal args As String())
         'Connect to DraftSight application
         dsApp = ConnectToDraftSight()
         If dsApp Is Nothing Then
             Return
         End If

         dsApp.AbortRunningCommand() ' abort any command currently running in DraftSight to avoid nested commands

         'Create new document
         dsDoc = dsApp.NewDocument("standard.dwt")
         If dsDoc Is Nothing Then
             MessageBox.Show("Failed to create a new document in DraftSight.")
             Return
         End If

         'Get custom coordinate system manager
         Dim dsCCSMgr As CustomCoordinateSystemManager = dsDoc.GetCustomCoordinateSystemManager()

         UsageOfDefaultCustomCoordinateSystems(dsCCSMgr)

         UsageOfNamedCustomCoordinateSystems(dsCCSMgr)
     End Sub

     Sub UsageOfDefaultCustomCoordinateSystems(ByVal dsCCSMgr As CustomCoordinateSystemManager)
         'Get World Coordinate System
         Dim dsWorldCCS As CustomCoordinateSystem = dsCCSMgr.GetWorldCustomCoordinateSystem()

         Debug.Print(Environment.NewLine   "Get World CCS.")

         PrintCoordinateSystemParameters(dsWorldCCS)

         'Get default bottom custom coordinate system
         Dim dsBottomCCS As CustomCoordinateSystem = dsCCSMgr.GetDefaultCustomCoordinateSystem(dsDefaultCustomCoordinateSystem_e.dsDefaultCustomCoordinateSystem_Bottom)

         Debug.Print(Environment.NewLine   "Get default Bottom CCS.")

         PrintCoordinateSystemParameters(dsBottomCCS)

         'Activate default bottom custom coordinate system
         dsBottomCCS.Activate()

         'Get previous CCS; it should be WCS.
         Dim dsPreviousCCS As CustomCoordinateSystem = dsCCSMgr.GetPreviousCustomCoordinateSystem()

         Debug.Print(Environment.NewLine   "Get previous CCS.")

         PrintCoordinateSystemParameters(dsPreviousCCS)

         'Get active CCS; it should be bottom CCS.
         Dim dsActiveCCS As CustomCoordinateSystem = dsCCSMgr.GetActiveCustomCoordinateSystem()

         Debug.Print(Environment.NewLine   "Get active CCS.")

         PrintCoordinateSystemParameters(dsActiveCCS)

         'The active custom coordinate system can be modified
         'Change origin of active custom coordinate system
         Dim originX As Double = 2
         Dim originY As Double = 3
         Dim originZ As Double = 1
         dsCCSMgr.SetActiveCustomCoordinateSystemOrigin(originX, originY, originZ)

         Debug.Print(Environment.NewLine   "Origin of active CCS has been changed.")

         PrintCoordinateSystemParameters(dsActiveCCS)

         'Align custom coordinate system by entity
         AlignActiveCCSByEntity(dsCCSMgr)

         Debug.Print(Environment.NewLine   "The active CCS has been aligned by line entity.")

         PrintCoordinateSystemParameters(dsActiveCCS)
     End Sub

     Sub AlignActiveCCSByEntity(ByVal dsCCSMgr As DraftSight.Interop.dsAutomation.CustomCoordinateSystemManager)
         'Get model space
         Dim dsModel As DraftSight.Interop.dsAutomation.Model = dsDoc.GetModel()

         'Get sketch manager
         Dim dsSketchMgr As DraftSight.Interop.dsAutomation.SketchManager = dsModel.GetSketchManager()

         'Draw a line entity
         Dim startPoint As Double() = {5, 5, 0}
         Dim endPoint As Double() = {12, 15, 0}
         Dim dsLine As DraftSight.Interop.dsAutomation.Line = dsSketchMgr.InsertLine(startPoint(0), startPoint(1), startPoint(2), endPoint(0), endPoint(1), endPoint(2))

         'Align active CCS by the created line entity
         dsCCSMgr.AlignActiveCustomCoordinateSystemByEntity(dsLine, startPoint)
     End Sub

     Sub UsageOfNamedCustomCoordinateSystems(ByVal dsCCSMgr As DraftSight.Interop.dsAutomation.CustomCoordinateSystemManager)
         'Get view manager
         Dim dsViewManager As DraftSight.Interop.dsAutomation.ViewManager = dsDoc.GetViewManager()

         'Set isometric view
         dsViewManager.SetPredefinedView(dsPredefinedView_e.dsPredefinedView_SWIsometric)

         'Zoom extents
         dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing)

         'Create a new named CCS by saving the active view as new CCS
         Dim name As String = "newCCS"
         Dim dsNewCCS As DraftSight.Interop.dsAutomation.CustomCoordinateSystem =  Nothing
         Dim saveViewResult As dsCreateObjectResult_e = dsCCSMgr.SaveActiveViewAs(name, dsNewCCS)
         If dsNewCCS IsNot Nothing AndAlso dsCreateObjectResult_e.dsCreateObjectResult_Success = saveViewResult  Then
             Debug.Print(Environment.NewLine & "New named CCS has been created by saving active view as new CCS.")

             PrintCoordinateSystemParameters(dsNewCCS)

             'Rename new CCS
             Dim newName As String = name & "_Changed"
             If RenameCCS(dsNewCCS, newName) Then
                 Debug.Print(Environment.NewLine & "The CCS has been renamed.")

                 PrintCoordinateSystemParameters(dsNewCCS)

                 'Print named CCS list
                 PrintNamedCCSList(dsCCSMgr)

                 'Remove the created CCS
                 dsCCSMgr.RemoveCustomCoordinateSystem(newName)

                 'Print named CCS list
                 PrintNamedCCSList(dsCCSMgr)
             End If
         Else
             MessageBox.Show(String.Format("Failed to save the active view as new ""{0}"" custom coordinate system.", name))
         End If
     End Sub

     Sub PrintNamedCCSList(ByVal dsCCSMgr As DraftSight.Interop.dsAutomation.CustomCoordinateSystemManager)
         Dim namedCCS As String() = DirectCast(dsCCSMgr.GetNamedCustomCoordinateSystemList(), String())
         If namedCCS Is Nothing Then
             Debug.Print(Environment.NewLine & "There are no named custom coordinate systems in the current document.")
         Else
             Debug.Print(Environment.NewLine & "Named custom coordinate systems:")

             For Each name As  String  In namedCCS
                 Debug.Print(name)
             Next
         End If
     End Sub

     Function RenameCCS(ByVal dsNewCCS As DraftSight.Interop.dsAutomation.CustomCoordinateSystem,  ByVal newName As  String)  As  Boolean
         Dim renameResult As dsCreateObjectResult_e = dsNewCCS.Rename(newName)
         If dsCreateObjectResult_e.dsCreateObjectResult_Success <> renameResult  Then
             MessageBox.Show(String.Format("Failed to rename custom coordinate system. New name should be {0}. Renaming result: {1}.", newName, renameResult.ToString()))

             Return False
         End If

         Return True
     End Function

     Sub PrintCoordinateSystemParameters(ByVal dsCustomCoordinateSystem As DraftSight.Interop.dsAutomation.CustomCoordinateSystem)
         Debug.Print(Environment.NewLine   "Custom Coordinate System Parameters:")

         Debug.Print("Name = " & dsCustomCoordinateSystem.GetName())

         Dim isDefault As Boolean
         Dim defaultFlag As dsDefaultCustomCoordinateSystem_e
         dsCustomCoordinateSystem.GetDefaultCustomCoordinateSystemFlag(isDefault, defaultFlag)
         Debug.Print("IsDefault = " & isDefault.ToString())
         Debug.Print("DefaultCustomCoordinateSystemFlag = " & defaultFlag.ToString())

         Dim x As  Double, y  As  Double, z  As  Double
         dsCustomCoordinateSystem.GetOrigin(x, y, z)
         Debug.Print(String.Format("Origin ({0},{1},{2})", x, y, z))

         dsCustomCoordinateSystem.GetXAxisDirection(x, y, z)
         Debug.Print(String.Format("XAxisDirection ({0},{1},{2})", x, y, z))

         dsCustomCoordinateSystem.GetYAxisDirection(x, y, z)
         Debug.Print(String.Format("YAxisDirection ({0},{1},{2})", x, y, z))

         dsCustomCoordinateSystem.GetZAxisDirection(x, y, z)
         Debug.Print(String.Format("ZAxisDirection ({0},{1},{2})", x, y, z))
     End Sub

     Function ConnectToDraftSight() As DraftSight.Interop.dsAutomation.Application
         Dim dsApp As DraftSight.Interop.dsAutomation.Application =  Nothing

         Try
             'Connect to DraftSight
             dsApp =  DirectCast(Marshal.GetActiveObject("DraftSight.Application"), DraftSight.Interop.dsAutomation.Application)
         Catch ex As Exception
             MessageBox.Show("Failed to connect to DraftSight. Cause: " & ex.Message)
             dsApp = Nothing
         End Try

         Return dsApp
     End Function
 End Module
```
