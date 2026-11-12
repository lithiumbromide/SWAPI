---
title: "Insert Alternate Position View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Alternate_Position_View_Example_VB.htm"
---

# Insert Alternate Position View Example (VBA)

This example shows how to insert an Alternate Position View.

```vb
'--------------------------------------------------
'
' Preconditions: Drawing sheet is open with a
'                drawing view selected.
'
' Postconditions: An alternate position view is created.
'
'--------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swView As SldWorks.View
Dim swSelMgr As SldWorks.SelectionMgr

Sub main()

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager

    ' Select the drawing on which to superimpose
    ' an Alternate Position View
    Set swView = swSelMgr.GetSelectedObject6(1, 0)

    ' Insert the Alternate Position View and
    ' create the configuration called Configxxx
    Set swView = swView.InsertAlternateView("Configxxx")

    ' Print the type of view; should be 10, which
    ' is an Alternate Position View
    If Not swView Is Nothing Then
        Debug.Print "Type of view: " & swView.Type
    End If

End Sub
```
