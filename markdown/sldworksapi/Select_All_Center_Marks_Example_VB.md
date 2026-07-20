---
title: "Select All Center Marks Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_All_Center_Marks_Example_VB.htm"
---

# Select All Center Marks Example (VBA)

In the SOLIDWORKS API, center marks can be features or annotations.
Use these enumerators with ISelectionMgr::GetSelectedObjectType3 to return
that specific type of center mark:

- swSelCENTERMARKS for center marks that are features
- swSelCENTERMARKSSYMS for center marks that are
  annotations

Traversal over the two types is different for the center marks that
are:

- Annotations. Use IView::GetFirstCenterMark and
  ICenterMark::GetNext
- Features. Use IView::GetCenterMarks.

It is not directly possible to select center marks that are features,
even though they appear in a feature traversal. This example shows how
to indirectly select center marks that are features.

```
'------------------------------------------------
' Preconditions:
' 1. Verify that the drawing document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified drawing document.
' 2. Prints the path and file name of the drawing document to
'    the Immediate window.
' 3. Iterates the sheet and drawing views.
' 4. Prints the name of the sheet, drawing views,
'    and center mark annotations to the Immediate window.
' 5. Iterates the FeatureManager design tree.
' 6. Prints to the Immediate window that no center mark
'    features exist in the drawing document.
'------------------------------------------------
```

```
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModExt As SldWorks.ModelDocExtension
    Dim swDrawing As SldWorks.DrawingDoc
    Dim swView As SldWorks.View
    Dim swCtrMark As SldWorks.CenterMark
    Dim swAnn As SldWorks.Annotation
    Dim swFeat As SldWorks.Feature
    Dim swSubFeat As SldWorks.Feature
    Dim swSubSubFeat As SldWorks.Feature
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swSelData As SldWorks.SelectData
    Dim status As Boolean
    Dim fileName As String
    Dim errors As Long
    Dim warnings As Long
    Dim i As Long
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2025\samples\tutorial\advdrawings\foodprocessor.slddrw"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModExt = swModel.Extension
    Set swSelMgr = swModel.SelectionManager
    Set swSelData = swSelMgr.CreateSelectData
    Set swDrawing = swModel
    Set swView = swDrawing.GetFirstView
```

```
    swModel.ClearSelection2 True
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "---------------"
```

```
    i = 0
    Do While Not swView Is Nothing
        Debug.Print "  View = " & swView.Name
        ' Traverse over annotation center marks
        Set swCtrMark = swView.GetFirstCenterMark2
        Do While Not swCtrMark Is Nothing
            Set swAnn = swCtrMark.GetAnnotation
            Debug.Print "    " & swAnn.GetName
            ' Select directly through annotation
            status = swAnn.Select3(True, swSelData): Debug.Assert status
            Set swCtrMark = swCtrMark.GetNext
            i = i + 1
        Loop
        Set swView = swView.GetNextView
    Loop
```

```
    If i = 0 Then
        Debug.Print "No center mark annotations."
    End If
```

```
    Debug.Print "---------------"
```

```
    ' Traverse over feature center marks
    i = 0
    Set swFeat = swModel.FirstFeature
    While Not swFeat Is Nothing
        Set swSubFeat = swFeat.GetFirstSubFeature
        While Not swSubFeat Is Nothing
            Set swSubSubFeat = swSubFeat.GetFirstSubFeature
            While Not swSubSubFeat Is Nothing
                If "CenterMark" = swSubSubFeat.GetTypeName2 Then
                    Debug.Print "  " & swSubSubFeat.Name
                    ' Cannot directly select feature because feature does not
                    ' explicitly appear in FeatureManager design tree
                    ' Must indirectly select feature through user interface
                    status = swModExt.SelectByID2(swSubSubFeat.Name, "CENTERMARKS", 0#, 0#, 0#, True, 0, Nothing, swSelectOptionDefault): Debug.Assert status
                 End If
                Set swSubSubFeat = swSubSubFeat.GetNextSubFeature
            Wend
            Set swSubFeat = swSubFeat.GetNextSubFeature
        Wend
        Set swFeat = swFeat.GetNextFeature
    Wend
    If i = 0 Then
        Debug.Print "No center mark features."
    End If
```

```
End Sub
```
