---
title: "Update Notes Without Activating Sheets Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Update_Notes_Without_Activating_Sheets_Example_VB.htm"
---

# Update Notes Without Activating Sheets Example (VBA)

This example shows how to update the notes in a drawing document without activating the drawing sheets.

```
'-----------------------------------------------
' Preconditions:
' 1. Open a drawing document that has multiple
'    sheets that have multiple drawing views.
' 2. Insert a "Note" note in a drawing view
'    on one or more one drawing sheets.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Traverses:
'    a. features, getting drawing sheets only.
'    b. subfeatures, getting the drawing views.
'    c. annotations in the drawing views, getting
'       the notes and appending the letter Z to
'       the end of all "Note" notes in all drawing views
'       in all drawing sheets.
' 2. To verify step 1c, examine the Immediate window and
'    open each sheet that contained a "Note" note and
'    click that note.
'-----------------------------------------------
Option Explicit
```

```
' From swstrings.bas
Public Const swTnDrSheet As String = "DrSheet"
Public Const swTnAbsoluteView As String = "AbsoluteView"
Public Const swTnDetailView As String = "DetailView"
Public Const swTnRelativeView As String = "RelativeView"
Public Const swTnSectionPartView As String = "SectionPartView"
Public Const swTnSectionAssemView As String = "SectionAssemView"
Public Const swTnUnfoldedView As String = "UnfoldedView"
Public Const swTnAuxiliaryView As String = "AuxiliaryView"
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim myModel As SldWorks.ModelDoc2
    Dim myDrawing As SldWorks.DrawingDoc
    Dim curFeature As SldWorks.Feature
    Dim featureTypeName As String
    Dim thisSheet As SldWorks.Sheet
```

```
    Set swApp = Application.SldWorks
    Set myModel = swApp.ActiveDoc
    Set myDrawing = myModel
```

```
    Dim boolstatus As Boolean
```

```
' Loop through the features in the document, looking at the drawings sheets only
    Set curFeature = myModel.FirstFeature
    While Not curFeature Is Nothing
        featureTypeName = curFeature.GetTypeName()
        If (featureTypeName = swTnDrSheet) Then
            Set thisSheet = curFeature.GetSpecificFeature2()
            Debug.Print thisSheet.GetName()
            ' Test the sheet feature by getting and editing
            ' certain notes on any sheet, active or not
            Call test_sheet_feature(curFeature)
            ' Test the sheet feature by using it to activate the sheet.
            ' boolstatus = myDrawing.ActivateSheet(thisSheet.GetName)
        End If
        Set curFeature = curFeature.GetNextFeature
    Wend
```

```
End Sub
```

```
Sub test_sheet_feature(thisSheetFeature As SldWorks.Feature)
    Dim curFeature As SldWorks.Feature
    Dim featureTypeName As String
    Dim thisView As SldWorks.View
    Dim viewName As String
    Dim curAnno As SldWorks.Annotation
    Dim annoType As Long
    Dim thisNote As SldWorks.Note
    Dim noteText As String, newNoteText As String, noteText2 As String
    Dim boolstatus As Boolean
```

```
    ' Continue traversing through the subfeatures of this sheet feature
    ' The drawing views should show up as subfeatures of the sheet feature
    Set curFeature = thisSheetFeature.GetFirstSubFeature()
    While Not curFeature Is Nothing
        featureTypeName = curFeature.GetTypeName()
        If (featureTypeName = swTnAbsoluteView Or featureTypeName = swTnDetailView Or featureTypeName = swTnRelativeView Or featureTypeName = swTnSectionPartView Or featureTypeName = swTnSectionAssemView Or featureTypeName = swTnUnfoldedView Or featureTypeName = swTnAuxiliaryView) Then
            Set thisView = curFeature.GetSpecificFeature2()
        ' Loop through the annotations in this view, specifically looking for notes
            If Not thisView Is Nothing Then
                Debug.Print "  " & thisView.GetName2()
                Set curAnno = thisView.GetFirstAnnotation3()
                While Not curAnno Is Nothing
                    annoType = curAnno.GetType()
                    If annoType = SwConst.swAnnotationType_e.swNote Then
                        Set thisNote = curAnno.GetSpecificAnnotation()
                        If Not thisNote Is Nothing Then
                        ' Do something with this note; make sure that it seems to be completely
                        ' accessible even if the sheet is not the current sheet
                            noteText = thisNote.GetText()
                            If (Left(noteText, 4) = "Note") Then
                                newNoteText = noteText & "Z"
                                boolstatus = thisNote.SetText(newNoteText)
                            End If
                            noteText2 = thisNote.GetText()
                            Debug.Print "    " & noteText & " - " & noteText2
                        End If
                    End If
                    Set curAnno = curAnno.GetNext3()
                Wend
            End If
        End If
        Set curFeature = curFeature.GetNextSubFeature()
    Wend
```

```
End Sub
```
