---
title: "Get Broken-Out Section Feature Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Broken_Out_Section_Feature_Data_Example_VBNET.htm"
---

# Get Broken-Out Section Feature Data Example (VB.NET)

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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swDoc As ModelDoc2
     Dim swDDoc As DrawingDoc
     Dim swView As View
     Dim varSheet As Object
     Dim varViews As Object
     Dim I As Long
     Dim J As Long
     Dim K As Long
     Dim swFeat As Feature
     Dim swFeatData As BrokenOutSectionFeatureData
     Dim swDepthRef As Entity
     Dim varBS As Object
     Dim doRelease As Boolean
     Dim varskSeg As Object
     Dim segCtr As Long
     Dim segType As Long

     Sub main()
         swDoc = swApp.ActiveDoc
         swDDoc = swDoc
         swDoc.ClearSelection2(True)
         varSheet = swDDoc.GetViews
         For I = LBound(varSheet) To UBound(varSheet)
             varViews = varSheet(I)
             For J = 1 To UBound(varViews) ' skip the sheet view
                 Dim swView As View
                 swView = varViews(J)
                 Debug.Print("View: " & swView.Name)
                 Debug.Print("  Number of broken-out sections in this view: " & swView.GetBreakOutSectionCount)
                 varBS = swView.GetBreakOutSections
                 If (Not (IsNothing(varBS))) Then
                     For K = LBound(varBS) To UBound(varBS)
                         swFeat = varBS(K)
                         Call EditFeature(swFeat)
                         swFeatData = swFeat.GetDefinition
                         swFeatData.AccessSelections(swDoc, Nothing)
                         swDepthRef = swFeatData.DepthReference ' get and select depth reference, if set
                         If (swDepthRef Is Nothing) Then
                             Debug.Print("              Depth of exposure in meters: " & swFeatData.Depth)
                         Else
                             swDepthRef.Select(True)
                         End If
                         swFeatData.ReleaseSelectionAccess()
                         swFeatData =  Nothing
                     Next K
                 End If
             Next J
         Next I
     End Sub

     Sub GetExistingValue()
         swFeatData.EditSketch =  True
         varskSeg = swFeatData.SketchSegment
         If (Not (IsNothing(varskSeg))) Then
             Debug.Print("              Number of sketch segments: " & swFeatData.GetSketchSegmentCount)
         End If
     End Sub

     Sub EditFeature(ByVal inFeat As Feature)
         Debug.Print("      Iterating on broken-out section: " & inFeat.Name)

         swFeatData = inFeat.GetDefinition
         swFeatData.AccessSelections(swDoc,  Nothing)

         GetExistingValue()

         If (doRelease = False) Then
             If (Not (IsNothing(varskSeg))) Then
                 For segCtr = LBound(varskSeg) To UBound(varskSeg)
                     Dim swSeg As SketchSegment
                     swSeg = varskSeg(segCtr)
                     segType = swSeg.GetType
                     Select Case segType
                         Case swSketchSegments_e.swSketchLINE
                             Dim swSegLine As SketchLine
                             swSegLine = swSeg
                             Debug.Print("                  Segment type: Line")
                             swSegLine =  Nothing
                         Case swSketchSegments_e.swSketchARC
                             Dim swSegArc As SketchArc
                             swSegArc = swSeg
                             Debug.Print("                  Segment type: Arc")
                             Debug.Print("                      Old radius: " & swSegArc.GetRadius)
                             Dim newRad As Double
                             newRad = swSegArc.GetRadius + 0.005
                             Debug.Print("                      New radius: " & newRad)
                             swSegArc.SetRadius(newRad)
                             swSegArc =  Nothing
                         Case Else
                             Debug.Print("                  Segment type: Unknown")
                     End Select
                 Next segCtr
             End If
             inFeat.ModifyDefinition(swFeatData, swDoc, Nothing)
             swDoc.ClearSelection()
         Else
             swFeatData.ReleaseSelectionAccess()
         End If
         varskSeg =  Nothing
         swFeatData =  Nothing
     End Sub

     Public swApp As SldWorks

 End Class
```
