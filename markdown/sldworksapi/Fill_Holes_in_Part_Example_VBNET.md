---
title: "Fill Holes in Part Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fill_Holes_in_Part_Example_VBNET.htm"
---

# Fill Holes in Part Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System.Diagnostics
Imports System

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swPart As PartDoc
        Dim swBody As Body2
        Dim swFace As Face2
        Dim swLoop As Loop2
        Dim vEdgeArr As Object
        Dim swCurve() As Curve
        Dim vCurveArr As Object
        Dim swEdge As Edge
        Dim swTempBody As Body2
        Dim swSurf As Surface
        Dim swSurfCopy As Surface
        Dim sPartTemplateName As String
        Dim swNewModel As ModelDoc2
        Dim swNewPart As PartDoc
        Dim swFeat() As Feature
        Dim swKnitFeat As Feature
        Dim swThickFeat As Feature
        Dim swNewFeatMgr As FeatureManager
        Dim i As Integer
        Dim bRet As Boolean
        Dim vBodies As Object

        swModel = swApp.ActiveDoc
        swPart = swModel

        vBodies = swPart.GetBodies2(swBodyType_e.swSolidBody, False)
        swBody = vBodies(0)

        ' Create new part
        sPartTemplateName = swApp.GetUserPreferenceStringValue(swUserPreferenceStringValue_e.swDefaultTemplatePart)
        swNewModel = swApp.NewDocument(sPartTemplateName, swDwgPaperSizes_e.swDwgPaperAsize, 0.0#, 0.0#)
        swNewFeatMgr = swNewModel.FeatureManager
        swNewPart = swNewModel

        ReDim swFeat(0)

        swFace = swBody.GetFirstFace
        Do While Not swFace Is Nothing
            swLoop = swFace.GetFirstLoop
            Do While Not swLoop Is Nothing
                If swLoop.IsOuter Then
                    vEdgeArr = swLoop.GetEdges
                    If UBound(vEdgeArr) >= 0 Then
                        ReDim swCurve(UBound(vEdgeArr))
                        For i = 0 To UBound(vEdgeArr)
                            swEdge = vEdgeArr(i)
                            swCurve(i) = swEdge.GetCurve
                        Next i
                        vCurveArr = swCurve
                        swSurf = swFace.GetSurface
                        swSurfCopy = swSurf.Copy
                        swTempBody = swSurfCopy.CreateTrimmedSheet4(vCurveArr, False)

                        ' Typically nothing is returned if the loop is
                        ' perpendicular to the surface, as in the
                        ' end loops of a cylinder
                        If Not swTempBody Is Nothing Then
                            ' Sheet body only has one face
                            'Debug.Assert(1 = swTempBody.GetFaceCount)
                            'Debug.Assert(swBodyType_e.swSheetBody = swTempBody.GetType)
                            swFeat(UBound(swFeat)) = swNewPart.CreateFeatureFromBody3(swTempBody, False, swCreateFeatureBodyOpts_e.swCreateFeatureBodyCheck)
                            ' Debug.Assert(Not swFeat(UBound(swFeat)) Is Nothing)
                            ReDim Preserve swFeat(UBound(swFeat) + 1)
                        End If
                    End If
                End If
                swLoop = swLoop.GetNext
            Loop
            swFace = swFace.GetNextFace
        Loop

        ' Remove last empty feature
        ReDim Preserve swFeat(UBound(swFeat) - 1)

        swNewModel.ClearSelection2(True)
        For i = 0 To UBound(swFeat)
            bRet = swFeat(i).Select2(True, 1)
        Next i

        swNewFeatMgr.InsertSewRefSurface(True, False, False, 0.00003001639406912, 0.0001)

        ' Make sure surfaces are successfully sewn together
        swKnitFeat = swNewModel.FeatureByPositionReverse(0)
        bRet = swKnitFeat.Select2(False, 1)
        swThickFeat = swNewFeatMgr.FeatureBossThicken(0.00254, 0, 7471215, False, True, True, True)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
