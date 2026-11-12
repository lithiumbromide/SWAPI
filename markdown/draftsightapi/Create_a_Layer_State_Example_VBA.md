---
title: "Create a Layer State Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_a_Layer_State_Example_VBA.htm"
---

# Create a Layer State Example (VBA)

This example shows how to create a Layer state and get one of its stored Layer's properties.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Open the Immediate window.
' 5. Start DraftSight.
' 6. Ensure the specified document to open exists.
' 7. Press F5.
'
' Postconditions:
' 1. Specified document is opened.
' 2. A layer state is created.
' 3. Properties of the stored Layer, Object, are printed out.
'---------------------------------------------------------------------------
Option Explicit
Sub main()
```

```vb
        Dim dsApp As DraftSight.Application
         'Connect to DraftSight application
         Set dsApp = GetObject(, "DraftSight.Application")
         'Abort any command currently running in DraftSight
         'to avoid nested commands
         dsApp.AbortRunningCommand
         'Open document
         Dim dsDoc As DraftSight.Document
         Dim docName As String
         docName = "c:\ProgramData\Dassault Systemes\DraftSight\Examples\B-44563.DWG"
         Set dsDoc = dsApp.OpenDocument2(docName, dsDocumentOpenOption_e.dsDocumentOpen_Default, dsEncoding_e.dsEncoding_Default)
         If dsDoc Is Nothing Then
             MsgBox ("Specified document did not open. Check path and file name.")
             Return
         End If

        'Create a Layer state and get one of its Layer's properties
         Dim dsLayerStateMgr As DraftSight.LayerStateManager
         Dim dsLayerState As DraftSight.LayerState
         Dim dsLayerStateProperties As DraftSight.LayerProperties

         Dim iStatus As Long
         Set dsLayerStateMgr = dsDoc.GetLayerStateManager
         iStatus = dsLayerStateMgr.CreateLayerState("LSName", dsLayerStateSpaceType_Model, dsLayerState)

        dsLayerState.Activate

        Debug.Print "Layer state: " & dsLayerState.Name
         Debug.Print "Description: " & dsLayerState.Description
         Debug.Print "Space as defined in dsLayerStateSpaceType_e: " & dsLayerState.Space
         Debug.Print "Save Visibility in active Viewport? " & dsLayerState.ActiveViewPortVisibility
         Debug.Print "Save Freeze/Thaw property? " & dsLayerState.FrozenThawed
         Debug.Print "Save LineColor property? " & dsLayerState.LineColor
         Debug.Print "Save LineStyle property? " & dsLayerState.LineStyle
         Debug.Print "Save LineWeight property? " & dsLayerState.LineWeight
         Debug.Print "Save Lock/Unlock property? " & dsLayerState.LockedUnlocked
         Debug.Print "Save Freeze/Thaw in new Viewport property? " & dsLayerState.NewViewPortFrozenThawed
         Debug.Print "Save Print/No print property? " & dsLayerState.PrintNoPrint
         Debug.Print "Save PrintStyle property? " & dsLayerState.PrintStyle
         Debug.Print "Save On/Off property? " & dsLayerState.ShowHide
         Debug.Print "Save Transparency property? " & dsLayerState.Transparency

        Dim layerObj As Variant
         layerObj = dsLayerState.GetLayers

        Set dsLayerStateProperties = dsLayerState.GetLayerProperties("Object")
        Debug.Print "Layer: " & dsLayerStateProperties.Layername
         Debug.Print "Name: " & dsLayerStateProperties.Name
         Debug.Print "Active: " & dsLayerStateProperties.status
         Debug.Print "Frozen: " & dsLayerStateProperties.Frozen
         Debug.Print "LineStyle: " & dsLayerStateProperties.LineStyle
         Debug.Print "LineWeight as defined in dsLineWeight_e: " & dsLayerStateProperties.LineWeight
         Debug.Print "Locked: " & dsLayerStateProperties.Locked
         Debug.Print "Frozen in new Viewport: " & dsLayerStateProperties.FrozenInNewViewport
         Debug.Print "Can be printed: " & dsLayerStateProperties.Print
         Debug.Print "PrintStyle: " & dsLayerStateProperties.PrintStyle
         Debug.Print "On: " & dsLayerStateProperties.Show
         Debug.Print "Transparency (%): " & dsLayerStateProperties.Transparency

 End Sub
```
