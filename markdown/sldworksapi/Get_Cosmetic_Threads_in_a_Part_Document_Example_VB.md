---
title: "Get Cosmetic Threads Features in a Part Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Cosmetic_Threads_in_a_Part_Document_Example_VB.htm"
---

# Get Cosmetic Threads Features in a Part Example (VBA)

This example shows how to create and get mirrored and patterned cosmetic thread feature data in a part document.

```
'-------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\holecube.sldprt.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Mirrors and patterns the cosmetic thread feature.
' 2. Examine the Immediate window.
'
' NOTE: Because this part is used elsewhere, do not save changes.
'-------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swMathUtility As SldWorks.MathUtility
Dim boolstatus As Boolean
```

```
Sub main()
```

```
    Dim myModel As SldWorks.ModelDoc2
    Dim thisFeature As SldWorks.Feature
    Dim thisSubFeature As SldWorks.Feature
```

```
    Set swApp = Application.SldWorks
    Set swMathUtility = swApp.GetMathUtility()
    Set myModel = swApp.ActiveDoc
```

```
    'Mirror and pattern the cosmetic thread subfeature
    boolstatus = myModel.Extension.SelectByID2("", "EDGE", -8.02489357837999E-04, -2.46888176810671E-02, 6.00726028778809E-05, True, 0, Nothing, 0)
    Set thisFeature = myModel.FeatureManager.InsertCosmeticThread3(swStandardType_StandardHelicoilMetric, "Helicoil threads", "M33x2.0", 0.033, swEndConditionBlind2Dia, 0.025, "M33x2.0 Helicoil Threads")
    boolstatus = myModel.Extension.SelectByID2("Cut-Extrude1", "BODYFEATURE", 0, 0, 0, False, 4, Nothing, 0)
    boolstatus = myModel.Extension.SelectByID2("", "FACE", -5.25693542039818E-02, -7.07674502874625E-02, 0, True, 128, Nothing, 0)
    boolstatus = myModel.Extension.SelectByID2("Boss-Extrude1", "BODYFEATURE", 0, 0, 0, True, 4, Nothing, 0)
    boolstatus = myModel.Extension.SelectByID2("", "EDGE", -7.36957308265147E-02, -4.66691871832836E-02, 1.25295787199775E-04, True, 1, Nothing, 0)
    myModel.FeatureManager.FeatureCircularPattern4 3, 1.25663706143592, True, "NULL", False, False, False
```

```
    ' Traverse features and subfeatures of this model and look for cosmetic threads
    Set thisFeature = myModel.FirstFeature
    While Not thisFeature Is Nothing
        Set thisSubFeature = thisFeature.GetFirstSubFeature()
        While Not thisSubFeature Is Nothing
            If (thisSubFeature.GetTypeName() = "CosmeticThread") Then
                Debug.Print "Processing " & thisSubFeature.Name
                Call processCosmeticThread(myModel, thisSubFeature)
            End If
            Set thisSubFeature = thisSubFeature.GetNextSubFeature()
        Wend
        Set thisFeature = thisFeature.GetNextFeature()
    Wend
End Sub
```

```
Private Sub processCosmeticThread(myModel As SldWorks.ModelDoc2, aFeature As SldWorks.Feature)
```

```
    Dim thisCThread As SldWorks.CosmeticThreadFeatureData
    Dim patternedCount As Long
    Dim holeEdge As SldWorks.Edge
    Dim holeCurve As SldWorks.Curve
    Dim vCurveParams As Variant
    Dim basePt(0 To 2) As Double
    Dim vBasePt As Variant
    Dim mBasePt As SldWorks.MathPoint
    Dim edgeEntity As SldWorks.Entity
    Dim selData As SldWorks.SelectData
    Dim vPatternedXform As Variant
    Dim i As Integer
    Dim transform As SldWorks.MathTransform
    Dim mTransPt As SldWorks.MathPoint
    Dim vTransPt As Variant
    Dim transPtX As Double, transPtY As Double, transPtZ As Double
    Dim append As Boolean, myCallout As SldWorks.Callout
```

```
    Set thisCThread = aFeature.GetDefinition()
```

```
    If Not thisCThread Is Nothing Then
    ' Retrieve the information about the edge associated with the cosmetic thread
        boolstatus = thisCThread.AccessSelections(myModel, Nothing)
        Set holeEdge = thisCThread.Edge()
        If Not holeEdge Is Nothing Then
            Set holeCurve = holeEdge.GetCurve()
            If Not holeCurve Is Nothing Then
                vCurveParams = holeEdge.GetCurveParams2()
                basePt(0) = vCurveParams(0)
                basePt(1) = vCurveParams(1)
                basePt(2) = vCurveParams(2)
                Debug.Print "    0 (" & Format(basePt(0), "###0.0#####") & ", " & Format(basePt(1), "###0.0#####") & ", " & Format(basePt(2), "###0.0#####") & ")"
            End If
        End If
```

```
        thisCThread.ReleaseSelectionAccess
        vBasePt = basePt
        Set mBasePt = swMathUtility.CreatePoint((vBasePt))
```

```
        ' Select the edge used for the cosmetic thread
        Set edgeEntity = holeEdge
        append = True
        boolstatus = edgeEntity.Select4(append, selData)
```

```
        ' Retrieve information about any patterns made from this cosmetic thread
        patternedCount = thisCThread.GetPatternedTransformsCount()
        Debug.Print "         Pattern count = " & patternedCount
        vPatternedXform = thisCThread.PatternedTransforms()
        If Not IsEmpty(vPatternedXform) Then
            For i = LBound(vPatternedXform) To UBound(vPatternedXform)
                Set transform = vPatternedXform(i)
                Set mTransPt = mBasePt.MultiplyTransform(transform)
                vTransPt = mTransPt.ArrayData()
                transPtX = vTransPt(0)
                transPtY = vTransPt(1)
                transPtZ = vTransPt(2)
                Debug.Print "             Pattern " & Str(i + 1) & " (" & Format(transPtX, "###0.0#####") & ", " & Format(transPtY, "###0.0#####") & ", " & Format(transPtZ, "###0.0#####") & ")"
                ' The transform information should be sufficient
                ' for getting the necessary geometry
                ' information for this cosmetic thread and
                ' its patterned cosmetic threads
                ' The next step  attempts to select the edge used for
                ' patterned cosmetic threads to help verify that the
                ' transform information is accurate and that
                ' an edge could be obtained, if necessary
                ' Selections depend on whether the edge is
                ' actually visible in this orientation and this display state
                append = True
                boolstatus = myModel.Extension.SelectByID2("", "EDGE", transPtX, transPtY, transPtZ, append, 0, myCallout, 0)
                If (boolstatus = 0) Then
                    Debug.Print "                 Selection failed?"
               End If
            Next i
        End If
    End If
```

```
End Sub
```
