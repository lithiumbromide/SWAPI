---
title: "Fill Holes in Part Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fill_Holes_in_Part_Example_VB.htm"
---

# Fill Holes in Part Example (VBA)

In CAM drilling operations, it might be useful to deduce the appearance of an item before machining begins. This is slightly different than calculating the minimum amount of raw material required, i.e., the stock size. This example shows how to use some of the geometry- and topology-related methods and properties to fill all holes in a part.

```
'--------------------------------------------------------------------------
' Preconditions: Open public_documents\samples\tutorial\api\cover_datum.sldrpt.
'
' Postconditions:
' 1. Creates a new part.
' 2. Fills the holes in the new part.
' 3. Click the surface-imported and thicken features, which were created
'    by filling the holes, in the FeatureManager design tree and examine
'    the part after each click.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'-----------------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swPart As SldWorks.PartDoc
    Dim swBody As SldWorks.Body2
    Dim swFace As SldWorks.Face2
    Dim swLoop As SldWorks.Loop2
    Dim vEdgeArr As Variant
    Dim swCurve() As SldWorks.Curve
    Dim vCurveArr As Variant
    Dim swEdge As SldWorks.Edge
    Dim swTempBody As SldWorks.Body2
    Dim swSurf As SldWorks.Surface
    Dim swSurfCopy As SldWorks.Surface
    Dim sPartTemplateName As String
    Dim swNewModel As SldWorks.ModelDoc2
    Dim swNewPart  As SldWorks.PartDoc
    Dim swFeat() As SldWorks.Feature
    Dim swKnitFeat As SldWorks.Feature
    Dim swThickFeat As SldWorks.Feature
    Dim swNewFeatMgr As SldWorks.FeatureManager
    Dim i As Long
    Dim bRet As Boolean
    Dim vBodies As Variant
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swPart = swModel
```

```
    vBodies = swPart.GetBodies2(swSolidBody, False)
    Set swBody = vBodies(0)
```

```
    ' Create new part
    sPartTemplateName = swApp.GetUserPreferenceStringValue(swDefaultTemplatePart)
    Set swNewModel = swApp.NewDocument(sPartTemplateName, swDwgPaperAsize, 0#, 0#)
    Set swNewFeatMgr = swNewModel.FeatureManager
    Set swNewPart = swNewModel
```

```
    ReDim swFeat(0)
```

```
    Set swFace = swBody.GetFirstFace
    Do While Not swFace Is Nothing
        Set swLoop = swFace.GetFirstLoop
        Do While Not swLoop Is Nothing
            If swLoop.IsOuter Then
                vEdgeArr = swLoop.GetEdges
                If UBound(vEdgeArr) >= 0 Then
                    ReDim swCurve(UBound(vEdgeArr))
                    For i = 0 To UBound(vEdgeArr)
                        Set swEdge = vEdgeArr(i)
                        Set swCurve(i) = swEdge.GetCurve
                    Next i
                    vCurveArr = swCurve
                    Set swSurf = swFace.GetSurface
                    Set swSurfCopy = swSurf.Copy
                    Set swTempBody = swSurfCopy.CreateTrimmedSheet4(vCurveArr, False)
                    ' Typically nothing is returned if the loop is
                    ' perpendicular to the surface, as in the
                    ' end loops of a cylinder
                    If Not swTempBody Is Nothing Then
                        ' Sheet body only has one face
                        Debug.Assert 1 = swTempBody.GetFaceCount
                        Debug.Assert swSheetBody = swTempBody.GetType
                        Set swFeat(UBound(swFeat)) = swNewPart.CreateFeatureFromBody3(swTempBody, False, swCreateFeatureBodyCheck)
                        Debug.Assert Not swFeat(UBound(swFeat)) Is Nothing
                        ReDim Preserve swFeat(UBound(swFeat) + 1)
                    End If
                End If
            End If
            Set swLoop = swLoop.GetNext
        Loop
        Set swFace = swFace.GetNextFace
    Loop
    ' Remove last empty feature
    ReDim Preserve swFeat(UBound(swFeat) - 1)
    swNewModel.ClearSelection2 True
    For i = 0 To UBound(swFeat)
        bRet = swFeat(i).Select2(True, 1)
    Next i
    swNewFeatMgr.InsertSewRefSurface True, False, False, 3.001639406912E-05, 0.0001
    ' Make sure surfaces are successfully sewn together
    Set swKnitFeat = swNewModel.FeatureByPositionReverse(0)
    bRet = swKnitFeat.Select2(False, 1)
    Set swThickFeat = swNewFeatMgr.FeatureBossThicken(0.00254, 0, 7471215, False, True, True, True)
```

```
End Sub
```
