---
title: "Get Multi-jog Leader Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Multi-jog_Leader_Data_Example_VB.htm"
---

# Get Multi-jog Leader Data Example (VBA)

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
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swDrawingDoc As SldWorks.DrawingDoc
Dim swSheet As SldWorks.Sheet
Dim swView As SldWorks.View
Dim obj As Object
Dim swAnnotation As SldWorks.Annotation
Dim swMultiJogLeader As SldWorks.MultiJogLeader
Dim nbrLines As Long
Dim lineData As Variant
Dim i As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Get multi-jog leader
    Set swModel = swApp.ActiveDoc
    Set swDrawingDoc = swModel
    Set swSheet = swDrawingDoc.GetCurrentSheet
    Debug.Print "Sheet name: " & swSheet.GetName
    'First view is Sheet, so get next view
    Set swView = swDrawingDoc.GetFirstView
    Set swView = swView.GetNextView
```

```
    Debug.Print "View name: " & swView.GetName2
    Set obj = swView.GetFirstMultiJogLeader2
    Set swMultiJogLeader = obj
```

```
    'Get multi-jog leader data
    Set swAnnotation = swMultiJogLeader.GetAnnotation
    Debug.Print "Annotation name: " & swAnnotation.GetName
    Debug.Print "Type of annotation (11 = multi-jog leader): " & swAnnotation.GetType
    nbrLines = swMultiJogLeader.GetLineCount
    Debug.Print "Number of lines in multi-jog leader: " & nbrLines
    lineData = swMultiJogLeader.GetLineAtIndex(1)
    For i = 0 To nbrLines - 1
        If Not IsEmpty(lineData) Then
            Debug.Print " Line " & i + 1 & ":"
            Debug.Print "  Line type as defined by swLineTypes_e: " & lineData(0)
            Debug.Print "  Line x, y, and z start points: " & lineData(1) & ", " & lineData(2) & ", and " & lineData(3)
            Debug.Print "  Line x, y, and z end points: " & lineData(4) & ", " & lineData(5) & ", and " & lineData(6)
        End If
    Next i
```

```
    Debug.Print "Number of arrow heads in multi-jog leader: " & swMultiJogLeader.GetArrowHeadCount
```

```
End Sub
```
