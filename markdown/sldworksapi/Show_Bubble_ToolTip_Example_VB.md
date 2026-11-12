---
title: "Show Bubble ToolTip Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Show_Bubble_ToolTip_Example_VB.htm"
---

# Show Bubble ToolTip Example (VBA)

This example shows how to display a Bubble ToolTip.

```vb
'--------------------------------------------
'
' Preconditions: HTML file exists at the specified location.
'
' Postconditions: Contents of the HTML file are displayed in a Bubble ToolTip.
'
'--------------------------------------------
Option Explicit
Public Enum swArrowPosition_e
    swArrowLeftTop = 0
    swArrowLeftBottom = 1
    swArrowRightTop = 2
    swArrowRightBottom = 3
    swArrowUpTopLeft = 4
    swArrowUpTopRight = 5
    swArrowDownBottomLeft = 6
    swArrowDownBottomRight = 7
    swArrowLeftOrRightTop = 8
    swArrowLeftOrRightBottom = 9
    swArrowLeftOrRight = 10
    swArrowUpOrDownLeft = 11
    swArrowUpOrDownRight = 12
    swArrowUpOrDown = 13
    swArrowNone = 14
    swArrowUnknown = 15
End Enum
Sub main()
    Const sURLpath                  As String = "D:/Samples/Sample_QuickTips.html"

    Dim pSldWorks                   As Object
    Set pSldWorks = CreateObject("SwHtmlControl.SwHtmlInterface")
    pSldWorks.ShowBubbleTooltipAt 300, 400, swArrowLeftTop, "Sample Bubble ToolTip", "Message of Sample Bubble ToolTip", sURLpath
End Sub
'--------------------------------------------
```
