---
title: "Get Differences Between Parts Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Differences_Between_Parts_Example_VB.htm"
---

# Get Differences Between Parts Example (VBA)

This examples shows how to get the differences between two parts.

**NOTE**: When a part is designed for injection molding, many small design details must be added for the injection molding process. Typically, these are draft angles, thickening of walls, additional ribs, and so on. Quite often, without specialized knowledge and experience, these are added to the model, by mold maker, after the part has been designed by a designer. It is often desirable to find out what changes have been made to the original model. This is usually done to determine the change in the amount of material for the revised part. This example uses several geometry- and topology-related methods to find the differences and reverse difference between two parts.

```
'--------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\box.sldprt and holecube.sldprt.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Creates two new parts showing the differences between the parts.
' 2. Examine the Immediate window.
' 3. Examine the graphics area, then click Window and open the other
'    just-created part.
'
' NOTES:
' * This example is not intended to be a replacement for SOLIDWORKS
'   Utilities comparison utility.
' * New parts can contain one or more solid bodies.
' * This code is intended to run on parts that are similar.
' * Because the parts are used elsewhere, do not save changes.
'--------------------------------------------------------------------
Option Explicit
```

```
Sub CreateDiffPart(swApp As SldWorks.SldWorks, vBodyResArr As Variant)
    Dim vBodyRes As Variant
    Dim swBodyRes As SldWorks.Body2
    Dim swPartRes As SldWorks.PartDoc
    Dim swFeatRes As SldWorks.Feature
```

```
    If IsEmpty(vBodyResArr) Then Exit Sub
```

```
    Set swPartRes = swApp.NewPart
    For Each vBodyRes In vBodyResArr
        Set swBodyRes = vBodyRes
        Set swFeatRes = swPartRes.CreateFeatureFromBody3(swBodyRes, False, swCreateFeatureBodyCheck + swCreateFeatureBodySimplify): Debug.Assert Not swFeatRes Is Nothing
    Next
```

```
 End Sub
```

```
Sub main()
```

```
    Const sPartName1 As String = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\box.sldprt"
    Const sPartName2 As String = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\holecube.sldprt"
    Dim swApp As SldWorks.SldWorks
    Dim swModel1 As SldWorks.ModelDoc2
    Dim swPart1 As SldWorks.PartDoc
    Dim swBody1 As SldWorks.Body2
    Dim swBody1Copy As SldWorks.Body2
    Dim swBody1Copy2 As SldWorks.Body2
    Dim swModel2 As SldWorks.ModelDoc2
    Dim swPart2 As SldWorks.PartDoc
    Dim swBody2 As SldWorks.Body2
    Dim swBody2Copy As SldWorks.Body2
    Dim swBody2Copy2 As SldWorks.Body2
    Dim vswBody1 As Variant
    Dim vswBody2 As Variant
    Dim vBodyResArr1 As Variant
    Dim vBodyResArr2 As Variant
    Dim nRetval As Long
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel1 = swApp.GetOpenDocumentByName(sPartName1)
    Set swModel2 = swApp.GetOpenDocumentByName(sPartName2)
    Set swPart1 = swModel1
    Set swPart2 = swModel2
```

```
    ' Get all of the visible bodies in each part
    vswBody1 = swPart1.GetBodies2(swSolidBody, True)
    vswBody2 = swPart2.GetBodies2(swSolidBody, True)
    Set swBody1 = vswBody1(0)
    Set swBody2 = vswBody2(0)
    Set swBody1Copy = swBody1.Copy
    Set swBody2Copy = swBody2.Copy
    Set swBody1Copy2 = swBody1.Copy
    Set swBody2Copy2 = swBody2.Copy
```

```
    vBodyResArr1 = swBody1Copy2.Operations2(SWBODYCUT, swBody2Copy2, nRetval): Debug.Assert swBodyOperationNoError = nRetval
    vBodyResArr2 = swBody2Copy.Operations2(SWBODYCUT, swBody1Copy, nRetval): Debug.Assert swBodyOperationNoError = nRetval
```

```
    If IsEmpty(vBodyResArr1) And IsEmpty(vBodyResArr2) Then Exit Sub
```

```
    Debug.Print "Part1          = " & swModel1.GetPathName
    Debug.Print "Part2          = " & swModel2.GetPathName
```

```
    If Not IsEmpty(vBodyResArr1) Then
        Debug.Print "  Diffs(1-2)   = " & UBound(vBodyResArr1) + 1
    End If
```

```
    If Not IsEmpty(vBodyResArr2) Then
        Debug.Print "  Diffs(2-1)   = " & UBound(vBodyResArr2) + 1
    End If
```

```
    CreateDiffPart swApp, vBodyResArr1
    CreateDiffPart swApp, vBodyResArr2
```

```
End Sub
```
