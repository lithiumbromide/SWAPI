---
title: "Get Temporary Axes in Each Drawing View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Temporary_Axes_in_Each_Drawing_View_Example_VB.htm"
---

# Get Temporary Axes in Each Drawing View Example (VBA)

This example shows how to get the temporary axes in each drawing view and convert them to lines.

```
'----------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\block.sldprt.
' 2. Click File > Make Drawing from Part and
'    add one or more views to the drawing.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Converts all temporary axes to lines.
' 2. Examine the Immediate window and graphics area.
'----------------------------------------------------
Option Explicit
```

```vb
Dim swApp As SldWorks.SldWorks
Dim swDrawDoc As SldWorks.DrawingDoc
Dim swSelMgr As SldWorks.SelectionMgr
Dim swView As SldWorks.View
Dim pline As SldWorks.SketchSegment
Dim itr As Long

Sub main()

    Set swApp = Application.SldWorks
    Set swDrawDoc = swApp.ActiveDoc
    Set swSelMgr = swDrawDoc.SelectionManager
    ' Iterate through the views
    Set swView = swDrawDoc.GetFirstView

    While Not swView Is Nothing

        If Not swView.Type = swDrawingSheet Then

            Debug.Print swView.GetName2
            swDrawDoc.ActivateView swView.GetName2

            Dim nCount As Long, vTempAxesPoints As Variant, nJump As Long
            ' Get number of temporary axes
            nCount = swView.GetTemporaryAxesCount
            Debug.Print " Number of temporary axes = " & nCount

            nJump = 6
  ' Get temporary axes
            vTempAxesPoints = swView.GetTemporaryAxes

            For itr = 0 To nCount - 1

                Dim startPt(2) As Double
                Dim endPt(2) As Double

                startPt(0) = vTempAxesPoints(nJump * itr)
                startPt(1) = vTempAxesPoints(nJump * itr + 1)
                startPt(2) = vTempAxesPoints(nJump * itr + 2)

                endPt(0) = vTempAxesPoints(nJump * itr + 3)
                endPt(1) = vTempAxesPoints(nJump * itr + 4)
                endPt(2) = vTempAxesPoints(nJump * itr + 5)

                Debug.Print "   Temporary axis " & itr; " data :"
                Debug.Print "     start : x = " & startPt(0)
                Debug.Print "             y = " & startPt(1)
                Debug.Print "             z = " & startPt(2)
                Debug.Print "     end   : x = " & endPt(0)
                Debug.Print "             y = " & endPt(1)
                Debug.Print "             z = " & endPt(2)

' Convert temporary axes to line
                Set pline = swDrawDoc.CreateLine2(startPt(0), startPt(1), startPt(2), endPt(0), endPt(1), endPt(2))

                If Not pline Is Nothing Then

                    ' Color
                    Dim clr As Long
                    clr = swApp.GetUserPreferenceIntegerValue(swSystemColorsConstructionGeometry)
                    pline.Color = clr
                    ' Width
                    pline.Width = swLW_NORMAL
                    ' Style ( only an approximation )
                    pline.Style = swLineCHAIN

                End If
            Next itr

        End If
        ' Get next view
        Set swView = swView.GetNextView
    Wend

    swDrawDoc.ClearSelection2 True

End Sub
```
