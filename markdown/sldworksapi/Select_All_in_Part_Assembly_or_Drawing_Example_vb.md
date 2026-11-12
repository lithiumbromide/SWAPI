---
title: "Select All in Part, Assembly, or Drawing (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_All_in_Part_Assembly_or_Drawing_Example_vb.htm"
---

# Select All in Part, Assembly, or Drawing (VBA)

This example shows how to select everything in the graphics area of a part or assembly document or in the sheet of a drawing document, as if you box-selected everything in the graphics area or the sheet.

```
'--------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the part, assembly, and drawing documents opened by the macro
'    exist.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Examine:
'    * Sheet to verify that all of the entities in the drawing
'      are selected.
'    * Immediate window to see how many entities are selected.
' 2. Click Window > bolt-assembly.sldasm to switch to the assembly
'    document.
' 3. Examine:
'    * Graphics area to verify that the all of the components
'      in the assembly are selected.
'    * Immediate window to see how many components are selected.
' 4. Click Window > bolt.sldprt to switch to the part document.
' 5. Examine:
'    * Graphics area to verify that the all of the edges
'      in the part are selected.
'    * Immediate window to see how many edges are selected.
'
' NOTE: Because these documents are used elsewhere, do not save changes.
'--------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim partFile As String
Dim assemblyFile As String
Dim drawingFile As String
Dim errors As Long
Dim warnings As Long
Dim selCount As Integer
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    ' Open a part document and select all edges in the part
    partFile = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2017\introsw\bolt.sldprt"
    Set swModel = swApp.OpenDoc6(partFile, swDocPART, swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
    Set swSelMgr = swModel.SelectionManager
    'Select all edges in part
    SelectAllinDocument
```

```
    ' Open an assembly document and select all components in the assembly
    assemblyFile = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2017\introsw\bolt-assembly.sldasm"
    Set swModel = swApp.OpenDoc6(assemblyFile, swDocASSEMBLY, swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
    Set swSelMgr = swModel.SelectionManager
    'Select all components in assembly
    SelectAllinDocument
```

```
    ' Open a drawing document and select all entities in the drawing
    drawingFile = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2017\introsw\bolt-assembly.slddrw"
    Set swModel = swApp.OpenDoc6(drawingFile, swDocDRAWING, swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
    Set swSelMgr = swModel.SelectionManager
    'Select all entities in drawing
    SelectAllinDocument
```

```
End Sub
```

```
Sub SelectAllinDocument()
    ' Select all edges in a part, all components in an assembly,
    ' or all entities in a drawing
     swModelDocExt.SelectAll
```

```
    ' Get and print the number of selections
    selCount = 0
    selCount = swSelMgr.GetSelectedObjectCount2(-1)
```

```
    Select Case swModel.GetType
    Case swDocPART
        Debug.Print "Number of edges selected in part          = " & selCount
    Case swDocASSEMBLY
        Debug.Print "Number of components selected in assembly = " & selCount
    Case swDocDRAWING
        Debug.Print "Number of entities selected in drawing    = " & selCount
    Case Else
        Debug.Print "Unknown type of document."
    End Select
```

```
End Sub
```
