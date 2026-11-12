---
title: "Get Part for Corresponding Component Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Part_for_Corresponding_Component_Example_VB.htm"
---

# Get Part for Corresponding Component Example (VBA)

This example shows how to get the names of the part entity and the corresponding assembly component entity.

```vb
'-----------------------------------------------
'
' Preconditions:
'        (1) Assembly document is open.
'        (2) Select the feature whose part's and component's name you want.
'
' Postconditions: None
'
'-----------------------------------------------
Option Explicit
Sub main()
    Dim swApp                   As SldWorks.SldWorks
    Dim swModel                 As SldWorks.ModelDoc2
    Dim swModelDocComp          As SldWorks.ModelDoc2
    Dim swModelDocExt           As SldWorks.ModelDocExtension
    Dim swSelMgr                As SldWorks.SelectionMgr
    Dim swAssyFeat              As SldWorks.feature
    Dim swPartFeat              As SldWorks.feature
    Dim swComp                  As SldWorks.Component2
    Dim vFaceArr                As Variant
    Dim swAssyFace              As SldWorks.face2
    Dim swPartFace              As SldWorks.face2
    Dim swAssyEnt               As SldWorks.entity
    Dim swPartEnt               As SldWorks.entity
    Dim bRet                    As Boolean

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager

    Set swAssyFeat = swSelMgr.GetSelectedObject5(1)
    Set swComp = swSelMgr.GetSelectedObjectsComponent2(1)
    Set swModelDocComp = swComp.GetModelDoc
    Set swModelDocExt = swModelDocComp.Extension

    vFaceArr = swAssyFeat.GetFaces: Debug.Assert Not IsEmpty(vFaceArr)

    Set swAssyFace = vFaceArr(0)
    Set swAssyEnt = swAssyFace
    Set swPartEnt = swModelDocExt.GetCorrespondingEntity(swAssyEnt): Debug.Assert Not swPartEnt Is Nothing
    Set swPartFace = swPartEnt
    Set swPartFeat = swPartFace.GetFeature: Debug.Assert Not swPartFeat Is Nothing

    Debug.Print "Comp       = " + swComp.Name2 + " [" + swComp.GetPathName + "]"
    Debug.Print "  AssyFeat   = " + swAssyFeat.Name
    Debug.Print "  PartFeat   = " + swPartFeat.Name
End Sub
'---------------------------------------------------
```
