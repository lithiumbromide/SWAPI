---
title: "Create a Callout Independent of a Selection Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_a_Callout_Independent_of_a_Selection_Example_VB.htm"
---

# Create a Callout Independent of a Selection Example (VBA)

This example shows how to create a callout that is independent of a selection.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Document is open in SOLIDWORKS
 ' 2. Select Tools > References > SOLIDWORKS  <version> exposed type libraries for add-in use.
 ' 3. Copy Class1 to a class module named Class1.
 '
 ' Postconditions:
 ' 1. A callout is created with the specified properties.
 ' 2. Inspect the Immediate window for its text format properties.
 '-----------------------------------------------------------------------------
 Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As ModelDoc2
 Dim swExt As ModelDocExtension
 Dim swSelMgr As SelectionMgr
 Dim mathUtil As MathUtility
 Dim swTextFormat As TextFormat
 Dim handle As New Class1
 Dim mp As MathPoint
 Dim vPnt(2) As Double
 Dim myCallout As Callout
Sub main()
```

```vb
Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swExt = swModel.Extension
Set swSelMgr = swModel.SelectionManager
Set mathUtil = swApp.GetMathUtility
vPnt(0) = 0#
vPnt(1) = 0#
vPnt(2) = 0#
Set mp = mathUtil.CreatePoint(vPnt)
Set myCallout = swExt.CreateCallout(2, handle)
myCallout.Value(1) = ""
myCallout.IgnoreValue(1) = True
myCallout.Label2(1) = "SldWorks API"
myCallout.SkipColon = True
 myCallout.FontSize = 10
Call myCallout.SetLeader(True, True)
Call myCallout.SetTargetPoint(1, 0.001, 0.001, 0)
Call myCallout.SetTargetPoint(2, -0.001, 0.001, 0)
myCallout.Position = mp
myCallout.ValueInactive(0) = True
myCallout.TextBox = False
myCallout.Display (True)
Set swTextFormat = myCallout.TextFormat
 ProcessTextFormat swApp, swModel, swTextFormat
```

```vb
End Sub
Sub ProcessTextFormat(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swTextFormat As SldWorks.TextFormat)

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
'
 ' Class1 module
 '
 Implements SwCalloutHandler
 Private Sub Class_Initialize()
 End Sub
 Private Function SwCalloutHandler_OnStringValueChanged(ByVal pManipulator As Object, ByVal RowID As Long, ByVal Text As String) As Boolean
         Debug.Print ("Text: " & Text)
         Debug.Print ("Row: " & RowID)

         SwCalloutHandler_OnStringValueChanged = True

 End Function
```
