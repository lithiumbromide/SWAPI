---
title: "Get Detail Circle Information Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Detail_Circle_Information_Example_VB.htm"
---

# Get Detail Circle Information Example (VBA)

This example shows how to get information about detail circles.

```vb
'-----------------------------
'
' Preconditions:
'          (1) Drawing document is open.
'          (2) Drawing view to which you added at
'              least one detail circle is selected.
'
' Postconditions: None
'
'-----------------------------
Option Explicit
Sub main()
    Dim swApp                       As SldWorks.SldWorks
    Dim swModel                     As SldWorks.ModelDoc2
    Dim swDraw                      As SldWorks.DrawingDoc
    Dim swAssy                      As SldWorks.AssemblyDoc
    Dim swSelMgr                    As SldWorks.SelectionMgr
    Dim swView                      As SldWorks.View
    Dim vDetCirc                    As Variant
    Dim nSize                       As Long
    Dim nNumDetCirc                 As Long
    Dim i                           As Long
    Dim j                           As Long
    Dim index                       As Long
    Dim nNumArrow                   As Long
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDraw = swModel
    Set swSelMgr = swModel.SelectionManager
    Set swView = swSelMgr.GetSelectedObject5(1)

    'View::GetDetailCircleInfo2
    '   [ numDetailCircles,
    '       [ layer, centerPt[3], startPt[3], endPt[3], lineType, textPt[3], textHeight,
    '           numArrows,
    '               [ arrowTip[3], arrowComponent[3], arrowWidth, arrowHeight, arrowStyle ]
    '       ]
    '   ]
    vDetCirc = swView.GetDetailCircleInfo2
    nNumDetCirc = swView.GetDetailCircleCount2(nSize)
    Debug.Assert nNumDetCirc = vDetCirc(0)
    Debug.Assert nSize = UBound(vDetCirc) + 1
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  View = " & swView.Name

    index = 1   ' Set index to start of first detail circle
    For i = 0 To nNumDetCirc - 1
        Debug.Print "    Circle(" & i & ")"
        Debug.Print "      Layer        = " & vDetCirc(index + 0)
        Debug.Print "      Center pt    = (" & vDetCirc(index + 1) * 1000# & ", " & vDetCirc(index + 2) * 1000# & ", " & vDetCirc(index + 3) * 1000# & ") mm"
        Debug.Print "      Start  pt    = (" & vDetCirc(index + 4) * 1000# & ", " & vDetCirc(index + 5) * 1000# & ", " & vDetCirc(index + 6) * 1000# & ") mm"
        Debug.Print "      End    pt    = (" & vDetCirc(index + 7) * 1000# & ", " & vDetCirc(index + 8) * 1000# & ", " & vDetCirc(index + 9) * 1000# & ") mm"
        Debug.Print "      Line type    = " & vDetCirc(index + 10)
        Debug.Print "      Text   pt    = (" & vDetCirc(index + 11) * 1000# & ", " & vDetCirc(index + 12) * 1000# & ", " & vDetCirc(index + 13) * 1000# & ") mm"
        Debug.Print "      Text   ht    = " & vDetCirc(index + 14) * 1000# & " mm"

        nNumArrow = vDetCirc(index + 15)
        index = index + 16  ' Set index to start of first arrow
        For j = 0 To nNumArrow - 1
            Debug.Print "      Arrow(" & j & ")"
            Debug.Print "        Tip  pt      = (" & vDetCirc(index + 0) * 1000# & ", " & vDetCirc(index + 1) * 1000# & ", " & vDetCirc(index + 2) * 1000# & ") mm"
            Debug.Print "        Comp pt      = (" & vDetCirc(index + 3) * 1000# & ", " & vDetCirc(index + 4) * 1000# & ", " & vDetCirc(index + 5) * 1000# & ") mm"
            Debug.Print "        Width        = " & vDetCirc(index + 6) * 1000# & " mm"
            Debug.Print "        Height       = " & vDetCirc(index + 7) * 1000# & " mm"
            Debug.Print "        Style        = " & vDetCirc(index + 8)

            index = index + 9  ' Set index to start of next arrow
        Next j

        ' Index should now be at start of next detail circle
    Next i
End Sub
'-----------------------------
```
