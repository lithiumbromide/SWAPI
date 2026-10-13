---
title: "Set Text in Datum Tags and GTols Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Text_in_Datum_Tags_and_GTols_Example_VB.htm"
---

# Set Text in Datum Tags and GTols Example (VBA)

This example shows how to set the text in datum tags and geometric tolerances.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a drawing that contains at least one view, a datum feature,
 '    and a geometric tolerance.
 ' 2. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Sets prefix, suffix, and callouts for the first GTol.
 ' 2. Inserts below frame text in the first GTol.
 ' 3. Edits below frame text.
 ' 4. Deletes the first line of the below frame.
 ' 5. Gets the datum tag label.
 ' 6. Examine the Immediate window.
 ' ---------------------------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swModelView As SldWorks.ModelView
 Dim swDraw As SldWorks.DrawingDoc
 Dim swView As SldWorks.View
 Dim swDispGtol As SldWorks.Gtol
 Dim swDatumTag As SldWorks.DatumTag
 Dim Rect As Variant
Dim bRet as Boolean

Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swModelView = swModel.ActiveView
     Set swDraw = swModel
     Set swView = swDraw.GetFirstView 'sheet
     Set swView = swView.GetNextView

    'Set text parts
     Set swDispGtol = swView.GetFirstGTOL
     swDispGtol.SetText swGTolTextPrefix, "Prefix"
     swDispGtol.SetText swGTolTextSuffix, "Suffix"
     swDispGtol.SetText swGTolTextCalloutAbove, "Above"
     swDispGtol.SetText swGTolTextCalloutBelow, "Below"
     swDispGtol.SetText swGTolTextCalloutBelow, "Below1"
     swDispGtol.SetText swGTolTextCalloutBelow, "Below2"

    swModelView.GraphicsRedraw (Rect)

    'Get text parts
     Debug.Print "Callout above: " & swDispGtol.GetText(swGTolTextParts_e.swGTolTextCalloutAbove)
     Debug.Print "Callout below: " & swDispGtol.GetText(swGTolTextParts_e.swGTolTextCalloutBelow)
     Debug.Print "Prefix: " & swDispGtol.GetText(swGTolTextParts_e.swGTolTextPrefix)
     Debug.Print "Suffix: " & swDispGtol.GetText(swGTolTextParts_e.swGTolTextSuffix)

    'Insert below frame text
     bRet = swDispGtol.InsertBelowFrameTextAt(1, "Line 1 of below frame")
     bRet = swDispGtol.InsertBelowFrameTextAt(2, "Line 2 of below frame")
     bRet = swDispGtol.InsertBelowFrameTextAt(3, "Line 3 of below frame")

    'Get below frame text
     Debug.Print "Below frame text:"
     Debug.Print "  swDispGtol.GetBelowFrameTextAt(1)"
     Debug.Print "  swDispGtol.GetBelowFrameTextAt(2)"
     Debug.Print "  swDispGtol.GetBelowFrameTextAt(3)"

    'Inserts a line at index position 2, because overwrite is set to False
     bRet = swDispGtol.SetBelowFrameTextAt(2, "Line 2 edited in below frame", False)
     Debug.Print "  swDispGtol.GetBelowFrameTextAt(2)"

    bRet = swDispGtol.DeleteBelowFrameTextAt(1)   'Deletes the first line in the below frame
     'bRet = swDispGtol.DeleteBelowFrameTextAt(-1)  'Deletes all below frame text

    Set swDatumTag = swView.GetFirstDatumTag
     swDatumTag.SetText swDatumTagTextPrefix, "prefix"
     swDatumTag.SetText swDatumTagTextSuffix, "suffix"
     swDatumTag.SetText swDatumTagTextCalloutAbove, "above"
     swDatumTag.SetText swDatumTagTextCalloutBelow, "below"
     Debug.Print ("Datum tag label: " & swDatumTag.GetLabel)

    Set Rect = Nothing
     swModelView.GraphicsRedraw (Rect)

 End Sub
```
