---
title: "Modify Heal Edges Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Modify_Heal_Edges_Feature_Example_VB.htm"
---

# Modify Heal Edges Feature Example (VBA)

This example shows how to modify an existing heal edges feature.

```
'---------------------------------------------------
' Preconditions:
' 1. Open a part document that contains
'    an imported part with the edges of four faces
'    merged in a heal edges feature.
' 2. Edit the heal edges feature to verify that
'    four faces are listed in Faces in the Heal
'    Edges PropertyManager page.
' 3. Close the PropertyManager page.
'
' Postconditions:
' 1. At stop, press the Ctrl key while selecting
'    two faces, then press F5.
' 2. Modifies the heal edges feature
'    so that the edges of the two selected
'    faces are merged.
' 3. Edit the heal edges feature to verify
'    that only two faces are listed in Faces
'    in the Heal Edges PropertyManager page and
'    examine the graphics area.
'----------------------------------------------------
Option Explicit
```

```vb
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim swModelDocExt As SldWorks.ModelDocExtension
 Dim swHealEdgesFeature As SldWorks.HealEdgesFeatureData
 Dim swFeature As SldWorks.Feature
 Dim pFaceArr(1) As Object
 Dim vNewFaces As Variant
 Dim boolstatus As Boolean
 Dim nBefore As Long, nAfter As Long

 Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager
     Set swModelDocExt = swModel.Extension
     boolstatus = swModelDocExt.SelectByID2("HealEdge1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
     Set swFeature = swSelMgr.GetSelectedObject6(1, 0)
     swModel.ClearSelection2 True
     Set swHealEdgesFeature = swFeature.GetDefinition

    swHealEdgesFeature.AccessSelections swModel, Nothing
      Stop
     'Select two faces (press the Crtl key while selecting the faces)
     'Press F5

    Set pFaceArr(0) = swSelMgr.GetSelectedObject6(1, 0)
     Set pFaceArr(1) = swSelMgr.GetSelectedObject6(2, 0)
     swModel.ClearSelection2 True
    vNewFaces = pFaceArr
     swHealEdgesFeature.Faces = (vNewFaces)
     swHealEdgesFeature.HealEdges
     swHealEdgesFeature.GetEdgeInformation nBefore, nAfter
     swModel.ClearSelection2 True
    swFeature.ModifyDefinition swHealEdgesFeature, swModel, Nothing

End Sub
```
