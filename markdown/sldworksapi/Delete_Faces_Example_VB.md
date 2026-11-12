---
title: "Delete Faces Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Delete_Faces_Example_VB.htm"
---

# Delete Faces Example (VBA)

This example shows how to delete faces.

NOTE: You can only delete faces from a temporary body.

```
'------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\block.sldprt.
' 2. Select a cylindrical face.
'
' Postconditions:
' 1. Creates a new part, which contains the same body as
'    the original part but with the selected face removed.
' 2. Examine the graphics area.
'
' NOTE: It might not be possible to remove the
' selected face. If this is the case, then
' the new body is the same as the original
' body.
'-------------------------------------------------
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
    ' Search for faces on temporary body based on copied attributes
    ReDim swFaceArr(0)
    Set swFace = swBody.GetFirstFace
    Do While Not Nothing Is swFace
        Set swEnt = swFace
        Set swAttCopy = Nothing
        ' Only one instance of attribute on a face should exist
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
    '   1 = invisible
    '   0 = visible
    Const CreateVisible As Long = 0
```

```
    Const sAttDefName As String = "TDE_temp_attrib"
    Const sAttRootName As String = "TDE"
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swAttDef As SldWorks.AttributeDef
    Dim swModel As SldWorks.ModelDoc2
    Dim swPart As SldWorks.PartDoc
    Dim swBody As SldWorks.Body2
    Dim swCopyBody As SldWorks.Body2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim nSelCount As Long
    Dim swFace As SldWorks.Face2
    Dim swEnt As SldWorks.Entity
    Dim swAtt() As SldWorks.Attribute
    Dim vFaceArr As Variant
    Dim swNewPart As SldWorks.PartDoc
    Dim swNewModel As SldWorks.ModelDoc2
    Dim swFeat As SldWorks.Feature
    Dim vBodies As Variant
    Dim i As Long
    Dim bLocChk As Boolean
    Dim nRetval As Long
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
    vBodies = swPart.GetBodies2(swAllBodies, True)
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
```

```
    ' Can only delete faces from a temporary body
    Debug.Assert swCopyBody.IsTemporaryBody
```

```
    ' Should not assert because it may fail to delete
    ' faces or fail local check or both
    bRet = swCopyBody.DeleteFaces3(vFaceArr, 2, False, bLocChk)
```

```
    ' Should not assert because body may be a surface body
    nRetval = swCopyBody.Check2
```

```
    Set swNewPart = swApp.NewPart
    Set swNewModel = swNewPart
    Set swFeat = swNewPart.CreateFeatureFromBody3(swCopyBody, False, swCreateFeatureBodyCheck)
```

```
End Sub
```
