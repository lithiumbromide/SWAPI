---
title: "Get Broken-Out Section Feature Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Broken_Out_Section_Feature_Data_Example_VB.htm"
---

# Get Broken-Out Section Feature Data Example (VBA)

This example shows how to get broken-out section feature data from a drawing view.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Open a drawing that contains a view with a broken-out
 ' section feature.
 '
 ' Postconditions:
 ' 1. Inspect the Immediate window.
 ' 2. The radius of the broken-out section is increased.
 ' ---------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Dim swDoc As SldWorks.ModelDoc2
 Dim swDDoc As SldWorks.DrawingDoc
 Dim varSheet As Variant
 Dim varViews As Variant
 Dim I As Long
 Dim J As Long
 Dim K As Long
 Dim swFeat As SldWorks.Feature
 Dim swFeatData As SldWorks.BrokenOutSectionFeatureData
 Dim swDepthRef As SldWorks.Entity
 Dim varBS As Variant
 Dim doRelease As Boolean
 Dim varskSeg As Variant
 Dim segCtr As Long
 Dim segType As Long
Option Explicit
 Sub main()
    Set swApp = Application.SldWorks
     Set swDoc = swApp.ActiveDoc
     Set swDDoc = swDoc
     swDoc.ClearSelection2 True
     varSheet = swDDoc.GetViews
     For I = LBound(varSheet) To UBound(varSheet)
         varViews = varSheet(I)
         For J = 1 To UBound(varViews) ' skip the sheet view
             Dim swView As SldWorks.View
             Set swView = varViews(J)
             Debug.Print "View: " & swView.Name
             Debug.Print ("  Number of broken-out sections in this view: " & swView.GetBreakOutSectionCount)
             varBS = swView.GetBreakOutSections
             If (Not (IsEmpty(varBS))) Then
                 For K = LBound(varBS) To UBound(varBS)
                     Set swFeat = varBS(K)
                     Call EditFeature(swFeat)
                     Set swFeatData = swFeat.GetDefinition
                     swFeatData.AccessSelections swDoc, Nothing
                     Set swDepthRef = swFeatData.DepthReference ' depth reference is not set
                     If (swDepthRef Is Nothing) Then
                         Debug.Print ("              Depth of exposure in meters: " & swFeatData.Depth)
                     Else
                         swDepthRef.Select True
                     End If
                     swFeatData.ReleaseSelectionAccess
                     Set swFeatData = Nothing
                 Next K
             End If
         Next J
     Next I
 End Sub

 Sub GetExistingValue()
    swFeatData.EditSketch = True
     varskSeg = swFeatData.SketchSegment
     If (Not (IsEmpty(varskSeg))) Then
         Debug.Print ("              Number of sketch segments: " & swFeatData.GetSketchSegmentCount)
     End If
 End Sub

 Sub EditFeature(inFeat As SldWorks.Feature)
    Debug.Print ("      Iterating on broken-out section: " & inFeat.Name)

    Set swFeatData = inFeat.GetDefinition
     swFeatData.AccessSelections swDoc, Nothing

    GetExistingValue

    If (doRelease = False) Then
         If (Not (IsEmpty(varskSeg))) Then
             For segCtr = LBound(varskSeg) To UBound(varskSeg)
                 Dim swSeg As SldWorks.SketchSegment
                 Set swSeg = varskSeg(segCtr)
                 segType = swSeg.GetType
                 Select Case segType
                     Case swSketchLINE
                         Dim swSegLine As SldWorks.SketchLine
                         Set swSegLine = swSeg
                         Debug.Print ("                  Segment type: Line")
                         Set swSegLine = Nothing
                     Case swSketchARC
                         Dim swSegArc As SldWorks.SketchArc
                         Set swSegArc = swSeg
                         Debug.Print ("                  Segment type: Arc")
                         Debug.Print ("                      Old radius: " & swSegArc.GetRadius)
                         Dim newRad As Double
                         newRad = swSegArc.GetRadius + 0.005
                         Debug.Print ("                      New radius: " & newRad)
                         swSegArc.SetRadius (newRad)
                         Set swSegArc = Nothing
                     Case Else
                         Debug.Print ("                  Segment type: Unknown")
                 End Select
             Next segCtr
         End If
         inFeat.ModifyDefinition swFeatData, swDoc, Nothing
         swDoc.ClearSelection
     Else
         swFeatData.ReleaseSelectionAccess
     End If

    varskSeg = Empty
     Set swFeatData = Nothing

End Sub
```
