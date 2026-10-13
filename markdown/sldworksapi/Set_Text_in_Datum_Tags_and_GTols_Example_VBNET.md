---
title: "Set Text in Datum Tags and GTols Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Text_in_Datum_Tags_and_GTols_Example_VBNET.htm"
---

# Set Text in Datum Tags and GTols Example (VB.NET)

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

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

 Public Sub main()

         Dim swModel As ModelDoc2
         Dim swModelView As ModelView
         Dim swDraw As DrawingDoc
         Dim swView As View
         Dim swDispGtol As Gtol
         Dim swDatumTag As DatumTag
         Dim Rect As Double
         Dim bRet As Boolean

         swModel = swApp.ActiveDoc
         swModelView = swModel.ActiveView
         swDraw = swModel
         swView = swDraw.GetFirstView 'sheet
         swView = swView.GetNextView

         'Set text parts
         swDispGtol = swView.GetFirstGTOL
         swDispGtol.SetText(swGTolTextParts_e.swGTolTextPrefix, "Prefix")
         swDispGtol.SetText(swGTolTextParts_e.swGTolTextSuffix, "Suffix")
         swDispGtol.SetText(swGTolTextParts_e.swGTolTextCalloutAbove, "Above")
         swDispGtol.SetText(swGTolTextParts_e.swGTolTextCalloutBelow, "Below")
         swDispGtol.SetText(swGTolTextParts_e.swGTolTextCalloutBelow, "Below1")
         swDispGtol.SetText(swGTolTextParts_e.swGTolTextCalloutBelow, "Below2")

         swModelView.GraphicsRedraw(Rect)

         'Get text parts
         Debug.Print("Callout above: " & swDispGtol.GetText(swGTolTextParts_e.swGTolTextCalloutAbove))
         Debug.Print("Callout below: " & swDispGtol.GetText(swGTolTextParts_e.swGTolTextCalloutBelow))
         Debug.Print("Prefix: " & swDispGtol.GetText(swGTolTextParts_e.swGTolTextPrefix))
         Debug.Print("Suffix: " & swDispGtol.GetText(swGTolTextParts_e.swGTolTextSuffix))

         'Insert below frame text
         bRet = swDispGtol.InsertBelowFrameTextAt(1, "Line 1 of below frame")
         bRet = swDispGtol.InsertBelowFrameTextAt(2, "Line 2 of below frame")
         bRet = swDispGtol.InsertBelowFrameTextAt(3, "Line 3 of below frame")

         'Get below frame text
         Debug.Print("Below frame text:")
         Debug.Print("  swDispGtol.GetBelowFrameTextAt(1)")
         Debug.Print("  swDispGtol.GetBelowFrameTextAt(2)")
         Debug.Print("  swDispGtol.GetBelowFrameTextAt(3)")

         'Inserts a line at index position 2, because overwrite is set to False
         bRet = swDispGtol.SetBelowFrameTextAt(2, "Line 2 edited in below frame", False)
         Debug.Print("  swDispGtol.GetBelowFrameTextAt(2)")

         bRet = swDispGtol.DeleteBelowFrameTextAt(1)   'Deletes the first line in the below frame
         'bRet = swDispGtol.DeleteBelowFrameTextAt(-1)  'Deletes all below frame text

         swDatumTag = swView.GetFirstDatumTag
         swDatumTag.SetText(swDatumTagTextParts_e.swDatumTagTextPrefix, "prefix")
         swDatumTag.SetText(swDatumTagTextParts_e.swDatumTagTextSuffix, "suffix")
         swDatumTag.SetText(swDatumTagTextParts_e.swDatumTagTextCalloutAbove, "above")
         swDatumTag.SetText(swDatumTagTextParts_e.swDatumTagTextCalloutBelow, "below")
         Debug.Print("Datum tag label: " & swDatumTag.GetLabel)

         Rect = Nothing
         swModelView.GraphicsRedraw(Rect)

     End Sub

     Public swApp As SldWorks

 End Class
```
