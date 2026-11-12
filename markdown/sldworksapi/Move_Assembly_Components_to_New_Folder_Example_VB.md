---
title: "Move Assembly Components to New Folder Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Move_Assembly_Components_to_New_Folder_Example_VB.htm"
---

# Move Assembly Components to New Folder Example (VBA)

This example shows how to move selected assembly components to a newly created folder in the FeatureManager design tree.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified assembly to open exists.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the specified assembly document.
 ' 2. Selects the valve<1> and valve_guide<1> components.
 ' 3. Creates a folder named Folder1 in the FeatureManager design tree.
 ' 4. Moves the valve<1> and valve_guide<1> components to  Folder1,
 '    which you can verify by expanding Folder1.
 ' 5. Examine the Immediate window.
 '
 ' NOTE: Because the assembly document is used by elsewhere,
 ' do not save any changes.
 '---------------------------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim modelDoc2 As SldWorks.modelDoc2
 Dim assemblyDoc As SldWorks.assemblyDoc
 Dim featureMgr As SldWorks.FeatureManager
 Dim modelDocExt As SldWorks.ModelDocExtension
 Dim selectionMgr As SldWorks.selectionMgr
 Dim feature As SldWorks.feature
 Dim selObj As Object
 Dim feat As SldWorks.feature
 Dim folderFeat As SldWorks.feature
 Dim errors As Long
 Dim warnings As Long
 Dim status As Long
 Dim count As Long
 Dim componentToMove As SldWorks.Component2
 Dim componentsToMove() As Object
 Dim i As Long
 Dim retVal As Boolean
 Sub Main()

    Set swApp = Application.SldWorks
    'Open assembly document
     swApp.OpenDoc6 "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\motionstudies\valve_cam.sldasm", swDocASSEMBLY, swOpenDocOptions_Silent, "", errors, warnings
     Set modelDoc2 = swApp.ActiveDoc
     Set assemblyDoc = modelDoc2
    'Select and get the two valve-related components to move to the new folder
     Set modelDocExt = modelDoc2.Extension
     Set selectionMgr = modelDoc2.SelectionManager
     status = modelDocExt.SelectByID2("valve-1@valve_cam", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
     Set selObj = selectionMgr.GetSelectedObject6(1, -1)
     status = modelDocExt.SelectByID2("valve_guide-1@valve_cam", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
     Set selObj = selectionMgr.GetSelectedObject6(2, -1)
     count = selectionMgr.GetSelectedObjectCount2(0)
     ReDim componentsToMove(count - 1)
     For i = 0 To count - 1
         Set componentToMove = selectionMgr.GetSelectedObjectsComponent4(i + 1, 0)
         Set componentsToMove(i) = componentToMove
     Next
    'Create the folder where to move the selected components
     Set featureMgr = modelDoc2.FeatureManager
     Set feature = featureMgr.InsertFeatureTreeFolder2(swFeatureTreeFolder_EmptyBefore)
     Set feature = assemblyDoc.FeatureByName("Folder1")
    'Move the selected components to the new folder
     retVal = assemblyDoc.ReorderComponents(componentsToMove, feature, swReorderComponents_LastInFolder)
    status = modelDocExt.SelectByID2("valve-1@valve_cam", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
     Set feat = selectionMgr.GetSelectedObject6(1, -1)
    Set featureMgr = modelDoc2.FeatureManager
     Set folderFeat = featureMgr.FeatureFolderLocation(feat)

    Debug.Print "Component valve-1@valve_cam folder feature: " & folderFeat.Name
End Sub
```
