---
title: "Select All Center Marks Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_All_Center_Marks_Example_VBNET.htm"
---

# Select All Center Marks Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModExt As ModelDocExtension
        Dim swDrawing As DrawingDoc
        Dim swView As View
        Dim swCtrMark As CenterMark
        Dim swAnn As Annotation
        Dim swFeat As Feature
        Dim swSubFeat As Feature
        Dim swSubSubFeat As Feature
        Dim swSelMgr As SelectionMgr
        Dim swSelData As SelectData
        Dim status As Boolean
        Dim fileName As String
        Dim errors As Integer
        Dim warnings As Integer
        Dim i As Integer

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2025\samples\tutorial\advdrawings\foodprocessor.slddrw"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModExt = swModel.Extension
        swSelMgr = swModel.SelectionManager
        swSelData = swSelMgr.CreateSelectData
        swDrawing = swModel
        swView = swDrawing.GetFirstView
        swModel.ClearSelection2(True)
        Debug.Print("File = " & swModel.GetPathName)
        Debug.Print("---------------")

        i = 0
        Do While Not swView Is Nothing
            Debug.Print("  View = " & swView.Name)
            ' Traverse over annotation center marks
            swCtrMark = swView.GetFirstCenterMark2
            Do While Not swCtrMark Is Nothing
                swAnn = swCtrMark.GetAnnotation
                Debug.Print("    " & swAnn.GetName)
                ' Select directly through annotation
                status = swAnn.Select3(True, swSelData) : Debug.Assert(status)
                swCtrMark = swCtrMark.GetNext
                i = i + 1
            Loop
            swView = swView.GetNextView
        Loop

        If i = 0 Then
            Debug.Print("No center mark annotations.")
        End If

        Debug.Print("---------------")
        ' Traverse over feature center marks
        i = 0
        swFeat = swModel.FirstFeature
        While Not swFeat Is Nothing
            swSubFeat = swFeat.GetFirstSubFeature
            While Not swSubFeat Is Nothing
                swSubSubFeat = swSubFeat.GetFirstSubFeature
                While Not swSubSubFeat Is Nothing
                    If "CenterMark" = swSubSubFeat.GetTypeName2 Then
                        Debug.Print("  " & swSubSubFeat.Name)
                        ' Cannot directly select feature because feature does not
                        ' explicitly appear in FeatureManager design tree
                        ' Must indirectly select feature through user interface
                        status = swModExt.SelectByID2(swSubSubFeat.Name, "CENTERMARKS", 0.0#, 0.0#, 0.0#, True, 0, Nothing, swSelectOption_e.swSelectOptionDefault) : Debug.Assert(status)
                    End If
                    swSubSubFeat = swSubSubFeat.GetNextSubFeature
                End While
                swSubFeat = swSubFeat.GetNextSubFeature
            End While
            swFeat = swFeat.GetNextFeature
        End While
        If i = 0 Then
            Debug.Print("No center mark features.")
        End If

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
