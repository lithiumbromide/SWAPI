---
title: "Get Multi-jog Leader Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Multi-jog_Leader_Data_Example_VBNET.htm"
---

# Get Multi-jog Leader Data Example (VB.NET)

This example shows how to get data for a multi-jog leader.

```
'-----------------------------------------------------------------------
' Preconditions:
' 1. Open a drawing document with at least one multi-jog leader.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Selects a multi-jog leader.
' 2. Gets data for the multi-jog leader.
' 3. Examine the Immediate window.
'-----------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swDrawingDoc As DrawingDoc
        Dim swSheet As Sheet
        Dim swView As View
        Dim obj As Object
        Dim swAnnotation As Annotation
        Dim swMultiJogLeader As MultiJogLeader
        Dim nbrLines As Integer
        Dim lineData As Object
        Dim lineType As Integer
        Dim startPointX As Double
        Dim startPointY As Double
        Dim startPointZ As Double
        Dim endPointX As Double
        Dim endPointY As Double
        Dim endPointZ As Double
        Dim i As Integer

        'Get multi-jog leader
        swModel = swApp.ActiveDoc
        swDrawingDoc = swModel
        swSheet = swDrawingDoc.GetCurrentSheet
        Debug.Print("Sheet name: " & swSheet.GetName)
        'First view is Sheet, so get next view
        swView = swDrawingDoc.GetFirstView
        swView = swView.GetNextView
        Debug.Print("View name: " & swView.GetName2)
        obj = swView.GetFirstMultiJogLeader2
        swMultiJogLeader = obj

        'Get multi-jog leader data
        swAnnotation = swMultiJogLeader.GetAnnotation
        Debug.Print("Annotation name: " & swAnnotation.GetName)
        Debug.Print("Type of annotation (11 = multi-jog leader): " & swAnnotation.GetType)
        nbrLines = swMultiJogLeader.GetLineCount
        Debug.Print("Number of lines in multi-jog leader: " & nbrLines)
        lineData = swMultiJogLeader.GetLineAtIndex(1)
        For i = 0 To nbrLines - 1
            If Not lineData Is Nothing Then
                Debug.Print(" Line " & i + 1 & ":")
                lineType = lineData(0)
                startPointX = lineData(1)
                startPointY = lineData(2)
                startPointZ = lineData(3)
                endPointX = lineData(4)
                endPointY = lineData(5)
                endPointZ = lineData(6)
                Debug.Print("  Line type as defined by swLineTypes_e: " & lineType)
                Debug.Print("  Line x, y, and z start points: " & startPointX & ", " & startPointY & ", and " & startPointZ)
                Debug.Print("  Line x, y, and z end points: " & endPointX & ", " & endPointY & ", and " & endPointZ)
            End If
        Next i
        Debug.Print("Number of arrow heads in multi-jog leader: " & swMultiJogLeader.GetArrowHeadCount)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
