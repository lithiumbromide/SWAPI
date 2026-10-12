---
title: "Delete Blended Faces Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Delete_Blended_Faces_Example_VB.htm"
---

# Delete Blended Faces Example (VBA)

This example shows how to delete blended faces.

NOTE: You can only delete blended faces from a temporary body.

```
'--------------------------------------------------
' Preconditions:
' 1. Open a part that contains one solid body
'    and at least one blended (fillet) face.
' 2. Select a blended face.
'
' Postconditions:
' 1. Creates a new part, which has the same body as
'    the original part, but the selected blended
'    face is removed.
' 2. Examine the graphics area.
'
' NOTE: It might not be possible to remove the
' selected blended face. If it's not removed, then
' the new body is the same as the original
' body.
'--------------------------------------------------
Option Explicit
```

```
Function GetFacesWithAttribute(swApp As SldWorks.SldWorks, swBody As SldWorks.Body2, swAttDef As SldWorks.AttributeDef) As Variant
    Dim swFace As SldWorks.Face2
    Dim swEnt As SldWorks.Entity
    Dim swAttCopy As SldWorks.Attribute
    Dim swFaceArr() As SldWorks.Face2
```

```
    ' Search for faces on temporary body based
    ' on copied attributes
    ReDim swFaceArr(0)
    Set swFace = swBody.GetFirstFace
    Do While Not Nothing Is swFace
        Set swEnt = swFace
        Set swAttCopy = Nothing
        ' Only one instance of attribute should exist
        Set swAttCopy = swEnt.FindAttribute(swAttDef, 0)
        If Not swAttCopy Is Nothing Then
            Set swFaceArr(UBound(swFaceArr)) = swFace
            ReDim Preserve swFaceArr(UBound(swFaceArr) + 1)
        End If
        Set swFace = swFace.GetNextFace
    Loop
    ReDim Preserve swFaceArr(UBound(swFaceArr) - 1)
    GetFacesWithAttribute = swFaceArr
End Function
```

```
Sub main()
```

```
    '1 = Invisible
    '0 = Visible
    Const CreateVisible         As Long = 0
```

```
    Const sAttDefName As String = "temp_attrib"
    Const sAttRootName As String = "temp"
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swAttDef As SldWorks.AttributeDef
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swPart As SldWorks.PartDoc
    Dim nSelCount As Long
    Dim swFace As SldWorks.Face2
    Dim swEnt As SldWorks.Entity
    Dim swAtt() As SldWorks.Attribute
    Dim vFaceArr As Variant
    Dim swFeat As SldWorks.Feature
    Dim vBodies As Variant
    Dim swBody As SldWorks.Body2
    Dim swCopyBody As SldWorks.Body2
    Dim swNewPart As SldWorks.PartDoc
    Dim i As Long
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swAttDef = swApp.DefineAttribute(sAttDefName)
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swPart = swModel
```

```
    bRet = swAttDef.Register
```

```
    ' Add attribute to selected faces
    nSelCount = swSelMgr.GetSelectedObjectCount
    ReDim swAtt(nSelCount)
    For i = 1 To nSelCount
        Set swFace = swSelMgr.GetSelectedObject6(i, -1)
        Set swEnt = swFace
        Set swAtt(i - 1) = swAttDef.CreateInstance5(swModel, swEnt, sAttRootName & i, CreateVisible, swAllConfiguration)
    Next i
```

```
    vBodies = swPart.GetBodies2(swAllBodies, False)
    Set swBody = vBodies(0)
    Set swCopyBody = swBody.Copy
```

```
    ' Remove attribute from faces
    For i = 1 To nSelCount
       bRet = swAtt(i - 1).Delete(True)
    Next i
```

```
    vFaceArr = GetFacesWithAttribute(swApp, swCopyBody, swAttDef)

    ' Can only delete blends from a temporary body
    Debug.Assert swCopyBody.IsTemporaryBody
```

```
    bRet = swCopyBody.DeleteBlends3(vFaceArr, True, True)
```

```
    Set swNewPart = swApp.NewPart
    Set swFeat = swNewPart.CreateFeatureFromBody3(swCopyBody, False, swCreateFeatureBodyCheck)
```

```
End Sub
```
