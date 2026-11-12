---
title: "Get Faces Affected by Scale Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Faces_Affected_by_Scale_Feature_Example_VB.htm"
---

# Get Faces Affected by Scale Feature Example (VBA)

This example shows how to get the faces affected by a scale feature in a multibody part.

**NOTE:** In SOLIDWORKS Design, a feature is a collection of faces. You can get these faces using IFeature::GetFaces. However, some features only affect existing faces and do not create any new faces. Examples of these types of features are draft and scale features. For these features, IFeature::GetFaces returns an empty array (i.e., no faces). To get the faces affected by a scale feature, first get the solid bodies to which the scale feature is applied. Each body is composed of a number of faces, which you can use to determine where these faces are located after the scale feature is applied to the body. An interesting issue is how to locate a face after a rebuild becausea face might not exist after a rebuild. To address this issue, SOLIDWORKS has safe entities, which are entities that survive a rebuild (i.e., are valid across a rebuild).

```
'--------------------------------------------------
' Preconditions:
' 1. Open a multibody part that has a scale feature.
' 2. Select the scale feature.
'
' Postconditions:
' 1. Deselects the scale feature.
' 2. Selects the faces affected by the scale feature.
' 3. Examine the graphics area.
'--------------------------------------------------
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
    Dim swScaleFeat As SldWorks.ScaleFeatureData
    Dim vBody As Variant
    Dim vBodyArr As Variant
    Dim swBody As SldWorks.Body2
    Dim swFace As SldWorks.Face2
    Dim swEnt As SldWorks.Entity
    Dim swSafeEnt As SldWorks.Entity
    Dim vSafeEnt As Variant
    Dim swSafeEntColl As New Collection
    Dim i As Long
    Dim bRet As Boolean
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
    Set swScaleFeat = swFeat.GetDefinition
```

```
    bRet = swScaleFeat.AccessSelections(swModel, Nothing)
    vBodyArr = swScaleFeat.Bodies
    For Each vBody In vBodyArr
        Set swBody = vBody
        Set swFace = swBody.GetFirstFace
        Do While Not swFace Is Nothing
            ' Face reference is only valid in rolled-back
            ' state, so get a more persistent face reference
            Set swEnt = swFace
            Set swSafeEnt = swEnt.GetSafeEntity
            swSafeEntColl.Add swSafeEnt
            Set swFace = swFace.GetNextFace
        Loop
    Next
```

```
     swScaleFeat.ReleaseSelectionAccess
```

```
     For Each vSafeEnt In swSafeEntColl
        Set swSafeEnt = vSafeEnt
        bRet = swSafeEnt.Select4(True, swSelData)
    Next
```

```
End Sub
```
