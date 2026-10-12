---
title: "Insert Weldment Cut List Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Weldment_Cut_List_Example_VB.htm"
---

# Insert Weldment Cut List Example (VBA)

This example shows how to insert a weldment cut list in a weldment part document.

```
'---------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\weldments\weldment_box2.sldprt.
' 2. Expand StructuralMember1 in the FeatureManager design tree and
'    Ctrl+click StructuralMember[1] and StructuralMember[2].
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Creates a new weldment cut-list item folder called Cut-List-Item1
'    in the FeatureManager design tree.
' 2. Places the selected solid bodies in Cut-List-Item1.
' 3. To verify:
'    * Examine the Immediate window.
'    * Expand Cut list(31) and expand Cut-List-Item1(2).
'
' NOTE: Because the part is used elsewhere, do not save changes.
'---------------------------------------------------------------------
```

```
Option Explicit
```

```
Sub main()
```

```
    Dim swApp                           As SldWorks.SldWorks
    Dim swModel                         As SldWorks.ModelDoc2
    Dim swSelMgr                        As SldWorks.SelectionMgr
    Dim swFeatMgr                       As SldWorks.FeatureManager
    Dim swCutListFeat                   As SldWorks.Feature
    Dim nSelCount                       As Long
    Dim swBody()                        As SldWorks.Body2
    Dim i                               As Long
    Dim bRet                            As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFeatMgr = swModel.FeatureManager
```

```
    nSelCount = swSelMgr.GetSelectedObjectCount
    ReDim swBody(nSelCount - 1)
    For i = 1 To nSelCount
        Set swBody(i - 1) = swSelMgr.GetSelectedObject6(i, -1)
    Next i
```

```
    Set swCutListFeat = swFeatMgr.InsertWeldmentCutList
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  " & swCutListFeat.Name
    For i = 0 To nSelCount - 1
        Debug.Print "    " & swBody(i).GetSelectionId
    Next i
```

```
End Sub
```
