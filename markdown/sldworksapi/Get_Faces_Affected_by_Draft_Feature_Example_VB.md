---
title: "Get Faces Affected by Draft Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Faces_Affected_by_Draft_Feature_Example_VB.htm"
---

# Get Faces Affected by Draft Feature Example (VBA)

This example shows how to get the faces affected by a draft feature.

**NOTE:** In SOLIDWORKS Design, a feature is comprised of faces. The faces created by a feature can be retrieved using IFeature::GetFaces. However, certain types of features only affect existing faces and do not create any new faces. Examples of these types of features are draft and scale features. For these features, IFeature::GetFaces returns an empty array (no faces). This sample code shows how to use IDraftFeatureData2::GetDraftedEntities to get the faces affected by a draft feature.

```
'---------------------------------------------------------------------------
' Preconditions:
' 1. Open a part or assembly with a draft feature.
' 2. If you opened an assembly, then fully resolve the assembly if necessary.
' 3. Select a draft feature.
'
' Postconditions:
' 1. Deselects the draft feature.
' 2. Selects the faces affected by the draft feature.
' 3. Gets the type of draft feature as defined in swDraftType_e.
' 4. Examine the Immediate window and graphics area.
'----------------------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swSelData As SldWorks.SelectData
    Dim swFeat As SldWorks.Feature
    Dim swDraftFeat As SldWorks.DraftFeatureData2
    Dim vEnt As Variant
    Dim vEntArr As Variant
    Dim swEnt As SldWorks.Entity
    Dim bRet As Boolean
```

```vb
    Set swApp = CreateObject("SldWorks.Application")
     Set swModel = swApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager
     Set swSelData = swSelMgr.CreateSelectData
     Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
     Set swDraftFeat = swFeat.GetDefinition

    ' Type as defined in swDraftType_e
     Debug.Print swDraftFeat.Type
    swModel.ClearSelection2 True

    ' No need to roll back to get affected faces
     vEntArr = swDraftFeat.GetDraftedEntities
     For Each vEnt In vEntArr
         Set swEnt = vEnt
         bRet = swEnt.Select4(True, swSelData)
     Next
 End Sub
```
