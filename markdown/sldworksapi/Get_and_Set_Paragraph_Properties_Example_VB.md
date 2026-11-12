---
title: "Get and Set Paragraph Properties Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Paragraph_Properties_Example_VB.htm"
---

# Get and Set Paragraph Properties Example (VBA)

This example shows how to get and set the properties of paragraphs in note annotations.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a drawing with a note annotation that contains one or more
 '    paragraphs.
 ' 2. Select the annotation in the graphics area.
 ' 3. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. For each paragraph in the selected note:
 '    * Sets the paragraph and line spacing.
 '    * Gets properties of numbered lists, if present.
 '    * Gets text segment formatting.
 '    * Bolds the text of each text segment.
 ' 2. Inspect the Immediate window.
 '----------------------------------------------------------------------------
 Option Explicit

Sub main()
    Dim swApp                       As SldWorks.SldWorks
     Dim swModel                     As SldWorks.ModelDoc2
     Dim swSelMgr                    As SldWorks.SelectionMgr
     Dim swAnnObj                    As Object
     Dim swAnn                       As SldWorks.Annotation
     Dim paragraphs                  As SldWorks.paragraphs
     Dim numSegs                     As Long
     Dim paragraphIndex              As Long
     Dim iseg                        As Long
     Dim textFormat                  As SldWorks.textFormat
     Dim paraType                    As Long
     Dim numberingtype               As Long
     Dim startas                     As Long
     Dim format                      As Long
     Dim numtype                     As Long
     Dim numParagraphs               As Long
     Dim Text                        As String

    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager

    If swSelMgr.GetSelectedObjectCount > 0 Then

        Set swAnnObj = swSelMgr.GetSelectedObject6(1, -1)
         Set swAnn = swAnnObj.GetAnnotation
         Set paragraphs = swAnn.GetParagraphs

        numParagraphs = paragraphs.count
         Debug.Print "Number of paragraphs = " & numParagraphs
         Debug.Print ""

        For paragraphIndex = 0 To numParagraphs - 1

            paragraphs.CurrentParagraph = paragraphIndex
             Debug.Print "paragraph(" & paragraphIndex & "): "; paragraphs.GetText(True)

            If paragraphIndex = 0 Then
                paragraphs.SetFormatting 0.0011, 0.0012
             Else
                paragraphs.SetFormatting 0.0021, 0.0022
             End If

            paragraphs.GetBulletsAndNumbering paraType, numberingtype, startas, numtype, format
             Debug.Print "Paragraph list type as defined in swParagraphType_e: " & paraType
             If paraType = 1 Then
                 Debug.Print "Numbered list:"
                 Debug.Print "  Start numbering from location as defined in swNumberedListStartType_e: " & numberingtype
                 Debug.Print "  Start numbering index: " & startas
                 Debug.Print "  Type as defined in swNumberedListType_e: " & numtype
                 Debug.Print "  Format as defined in swNumberingFormat_e: " & format
             End If

            numSegs = paragraphs.GetTextSegmentCount
             Debug.Print "Text segment count: " & numSegs

            For iseg = 0 To numSegs - 1
                 Text = paragraphs.GetTextSegmentText(iseg)
                 Debug.Print "segment(" & iseg & "): " & Text

                Set textFormat = paragraphs.GetTextSegmentFormat(iseg)
                 Debug.Print "  Typeface: " & textFormat.TypeFaceName
                 Debug.Print "  Backwards? " & textFormat.BackWards
                 Debug.Print "  Bold? " & textFormat.Bold
                 Debug.Print "  Italic? " & textFormat.Italic
                 Debug.Print "  Strikeout? " & textFormat.Strikeout

                textFormat.Bold = True
                 paragraphs.SetTextSegmentFormat iseg, textFormat

            Next

            paragraphs.UpdateParagraph

        Next

        swModel.GraphicsRedraw2

    End If
End Sub
```
