---
title: "Move Assembly Components to New Folder Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Move_Assembly_Components_to_New_Folder_Example_VBNET.htm"
---

# Move Assembly Components to New Folder Example (VB.NET)

This example shows how to move selected assembly components to a newly created folder in the FeatureManager design tree.

```
'---------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly to open exists.
' 2. Open an Immediate window.
'
' Postconditions:
' 1. Opens the specified assembly document.
' 2. Selects the valve<1> and valve_guide<1> components.
' 3. Creates a folder named Folder1 in the FeatureManager design tree.
' 4. Moves the valve<1> and valve_guide<1> components to Folder1,
'    which you can verify by expanding Folder1.
' 5. Examine the Immediate window.
'
' NOTE: Because the assembly document is used by elsewhere,
' do not save any changes.
'---------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks

	Imports SolidWorks.Interop.swconst

	Imports System.Runtime.InteropServices

	Imports System

	Imports System.Diagnostics

	Partial Class SolidWorksMacro

	    Dim modelDoc2 As ModelDoc2

	    Dim assemblyDoc As AssemblyDoc

	    Dim featureMgr As FeatureManager

	    Dim modelDocExt As ModelDocExtension

	    Dim selectionMgr As SelectionMgr

	    Dim feature As Feature

	    Dim selObj As Object

	    Dim feat As Feature

	    Dim folderFeat As Feature

	    Dim errors As Integer

	    Dim warnings As Integer

	    Dim status As Integer

	    Dim count As Integer

	    Dim componentToMove As Component2

	    Dim componentsToMove() As Object

	    Dim i As Integer

	    Dim retVal As Boolean

	    Sub Main()

	        'Open assembly document

	        swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\motionstudies\valve_cam.sldasm", swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "",
	errors, warnings)

	        modelDoc2 = swApp.ActiveDoc

	        assemblyDoc = modelDoc2

	        'Select and get the two
	valve-related components to move to the new folder

	        modelDocExt = modelDoc2.Extension

	        selectionMgr = modelDoc2.SelectionManager

	        status = modelDocExt.SelectByID2("valve-1@valve_cam", "COMPONENT",
	0, 0, 0, True,
	0, Nothing,
	0)

	        selObj = selectionMgr.GetSelectedObject6(1, -1)

	        status = modelDocExt.SelectByID2("valve_guide-1@valve_cam", "COMPONENT",
	0, 0, 0, True,
	0, Nothing,
	0)

	        selObj = selectionMgr.GetSelectedObject6(2, -1)

	        count = selectionMgr.GetSelectedObjectCount2(0)

	        ReDim componentsToMove(count - 1)

	        For i = 0 To count - 1

	            componentToMove = selectionMgr.GetSelectedObjectsComponent4(i
	+ 1, 0)

	            componentsToMove(i) = componentToMove

	        Next

	        'Create
	the folder where to move the selected components

	        featureMgr = modelDoc2.FeatureManager

	        feature = featureMgr.InsertFeatureTreeFolder2(swFeatureTreeFolderType_e.swFeatureTreeFolder_EmptyBefore)

	        feature = assemblyDoc.FeatureByName("Folder1")

	        'Move the selected components to
	the new folder

	        retVal = assemblyDoc.ReorderComponents(componentsToMove,
	feature, swReorderComponentsWhere_e.swReorderComponents_LastInFolder)

	        status = modelDocExt.SelectByID2("valve-1@valve_cam", "COMPONENT",
	0, 0, 0, True,
	0, Nothing,
	0)

	        feat = selectionMgr.GetSelectedObject6(1, -1)

	        featureMgr = modelDoc2.FeatureManager

	        folderFeat = featureMgr.FeatureFolderLocation(feat)

	        Debug.Print("Component valve-1@valve_cam folder feature: " & folderFeat.Name)

	    End Sub

	    Public swApp As SldWorks

	End Class
```
