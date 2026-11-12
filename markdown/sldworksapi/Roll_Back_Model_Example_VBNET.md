---
title: "Roll Back Model Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Roll_Back_Model_Example_VBNET.htm"
---

# Roll Back Model Example (VB.NET)

This example shows how to step through the FeatureManager design tree of a model by rolling back to each feature in reverse sequence. Running an example like this can provide insight into the design intent of the user.

```
'-----------------------------------
' Preconditions:
' 1. Open a part or assembly document.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Observe the FeatureManager design tree
'    while the macro executes.
' 2. Examine the Immediate window to see the
'    names of the features rolled back and forward.
'
' NOTE: The delay between steps is set to 1 second.
'-----------------------------------
```

```
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics
Imports System.Windows.Forms.Application

Partial Class SolidWorksMacro

    Public Sub Main()

        ' Delay in seconds
        Const DELAY As Single = 1.0#
        Dim swModel As ModelDoc2
        Dim swModelView As ModelView
        Dim swPart As PartDoc
        Dim swAssy As AssemblyDoc
        Dim swFeatMgr As FeatureManager
        Dim swFeat As Feature
        Dim featFace As Object
        Dim swFace As Face2
        Dim rect As Object
        Dim featName() As String
        Dim timeNow As Single
        Dim docType As Integer
        Dim i As Integer
        Dim j As Integer
        Dim status As Boolean

        swModel = swApp.ActiveDoc
        swModelView = swModel.ActiveView
        rect = Nothing
        swFeatMgr = swModel.FeatureManager

        swFeat = swModel.FirstFeature
        docType = swModel.GetType
        Select Case docType
            Case swDocumentTypes_e.swDocPART
                swPart = swModel
            Case swDocumentTypes_e.swDocASSEMBLY
                swAssy = swModel
            Case Else
                Debug.Print("Open a part or assembly document, then rerun this macro.")
                Exit Sub
        End Select

        ReDim featName(0)

        Do While Not swFeat Is Nothing
            featName(UBound(featName)) = swFeat.Name
            ReDim Preserve featName(UBound(featName) + 1)
            swFeat = swFeat.GetNextFeature
        Loop

        ' Loop over-allocates array by 1, so remove last (empty) entry
        ReDim Preserve featName(UBound(featName) - 1)

        ' Playback each feature in the FeatureManager design tree
        For i = 0 To UBound(featName)
            Debug.Print(featName(i))
            status = swFeatMgr.EditRollback(swMoveRollbackBarTo_e.swMoveRollbackBarToAfterFeature, featName(i))
            ' Do not assert because you may be trying to roll back or roll forward
            ' to a feature that cannot be rolled back or forward to; for example,
            ' the Lighting or Annotations folder
            'Debug.Assert status

            ' Remove any previous highlights
            swModelView.GraphicsRedraw(rect)
            ' Highlight feature if it has any geometry
            Select Case docType
                Case swDocumentTypes_e.swDocPART
                    swPart = swModel
                    swFeat = swPart.FeatureByName(featName(i))
                Case swDocumentTypes_e.swDocASSEMBLY
                    swAssy = swModel
                    swFeat = swAssy.FeatureByName(featName(i))
            End Select

            featFace = swFeat.GetFaces
            If (IsArray(featFace)) Then
                For j = 0 To (UBound(featFace) + 1)
                    swFace = featFace(j)
                    swFace.Highlight(True)
                Next j
            End If

            ' Only pause if rollback is successful
            If status Then
                timeNow = Timer
                While timeNow + DELAY > Timer
                    ' Allow SOLIDWORKS Design to refresh screen
                    DoEvents()
                End While
            End If
        Next i
        ' Remove highlight from last feature
        swModelView.GraphicsRedraw(rect)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
