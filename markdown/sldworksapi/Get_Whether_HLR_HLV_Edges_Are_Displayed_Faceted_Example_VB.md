---
title: "Get Whether HLR/HLV Edges Are Displayed Faceted Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Whether_HLR_HLV_Edges_Are_Displayed_Faceted_Example_VB.htm"
---

# Get Whether HLR/HLV Edges Are Displayed Faceted Example (VBA)

This example gets whether HLR or HLV edges (Hidden Lines Removed or Hidden Lines Visible) in the selected view are displayed faceted or not.

```
'-------------------------------------
' Preconditions:
' 1. Open a drawing and select a drawing view.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the pathname of the drawing, the selected
'    view name, and whether HLR/HLV edges are
'    displayed faceted in the drawing view.
' 2. Examine the Immediate window.
'--------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swView As SldWorks.View
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swView = swSelMgr.GetSelectedObject6(1, -1)
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  " & swView.Name & " [" & swView.GetDisplayMode2 & "]"
    Debug.Print "    HLR/HLV edges displayed faceted in this drawing view = " & swView.GetFacettedHlrDisplay
```

```
End Sub
```
