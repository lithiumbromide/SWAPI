---
title: "Create a Callout Independent of a Selection Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_a_Callout_Independent_of_a_Selection_Example_VBNET.htm"
---

# Create a Callout Independent of a Selection Example (VB.NET)

This example shows how to create a callout that is independent of a selection.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a model document in SOLIDWORKS.
 ' 2. Click Project > Add Reference > SolidWorks.interop.swpublished
 '    on the .NET tab.
 '
 ' Postconditions:
 ' 1. Creates a callout with the specified properties.
 ' 2. Inspect the Immediate window for its text format properties.
 '---------------------------------------------------------------------------

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.swpublished
 Imports System
 Imports System.Diagnostics
 Partial Class SolidWorksMacro
     Dim swModel As ModelDoc2
     Dim swExt As ModelDocExtension
     Dim swSelMgr As SelectionMgr
     Dim mathUtil As MathUtility
     Dim swTextFormat As TextFormat
     Public Sub main()
         swModel = swApp.ActiveDoc
         swExt = swModel.Extension
         swSelMgr = swModel.SelectionManager
         mathUtil = swApp.GetMathUtility
         Dim handle As New calloutHandler
         Dim mp As MathPoint
         Dim vPnt(2) As Double
         vPnt(0) = 0.0#
         vPnt(1) = 0.0#
         vPnt(2) = 0.0#
         mp = mathUtil.CreatePoint(vPnt)
         Dim myCallout As Callout
         myCallout = swExt.CreateCallout(2, handle)
         myCallout.Value(1) =  ""
         myCallout.IgnoreValue(1) = True
         myCallout.Label2(1) = "SldWorks API"
         myCallout.SkipColon = True
         Call myCallout.SetLeader(True, True)
         Call myCallout.SetTargetPoint(1, 0.001, 0.001, 0)
         Call myCallout.SetTargetPoint(2, -0.001, 0.001, 0)
         myCallout.Position = mp
         myCallout.ValueInactive(0) =  True
         myCallout.TextBox = False
         myCallout.Display(True)
        swTextFormat = myCallout.TextFormat
         ProcessTextFormat swApp, swModel, swTextFormat
     End Sub
     Sub ProcessTextFormat(swApp As SldWorks, swModel As ModelDoc2, swTextFormat As TextFormat)

     Debug.Print "    BackWards                    = " & swTextFormat.BackWards
     Debug.Print "    Bold                         = " & swTextFormat.Bold
     Debug.Print "    CharHeight                   = " & swTextFormat.CharHeight
     Debug.Print "    CharHeightInPts              = " & swTextFormat.CharHeightInPts
     Debug.Print "    CharSpacingFactor            = " & swTextFormat.CharSpacingFactor
     Debug.Print "    Escapement                   = " & swTextFormat.Escapement
     Debug.Print "    IsHeightSpecifiedInPts       = " & swTextFormat.IsHeightSpecifiedInPts
     Debug.Print "    Italic                       = " & swTextFormat.Italic
     Debug.Print "    LineLength                   = " & swTextFormat.LineLength
     Debug.Print "    LineSpacing                  = " & swTextFormat.LineSpacing
     Debug.Print "    ObliqueAngle                 = " & swTextFormat.ObliqueAngle
     Debug.Print "    Strikeout                    = " & swTextFormat.Strikeout
     Debug.Print "    TypeFaceName                 = " & swTextFormat.TypeFaceName
     Debug.Print "    Underline                    = " & swTextFormat.Underline
     Debug.Print "    UpsideDown                   = " & swTextFormat.UpsideDown
     Debug.Print "    Vertical                     = " & swTextFormat.Vertical
     Debug.Print "    WidthFactor                  = " & swTextFormat.WidthFactor

     Debug.Print ""
     End Sub

     Public swApp As SldWorks
 End Class
```

```vb
'
 ' calloutHandler.vb
 '

 <System.Runtime.InteropServices.ComVisible(True)> _
 Public Class calloutHandler
     Implements SwCalloutHandler
     Private Function OnStringValueChanged(ByVal pManipulator As Object, ByVal RowID As Integer, ByVal Text As String) As Boolean Implements SolidWorks.Interop.swpublished.ISwCalloutHandler.OnStringValueChanged
         Debug.Print("Text: " & Text)
         Debug.Print("Row: " & RowID)
         Return True
     End Function
 End  Class
```
