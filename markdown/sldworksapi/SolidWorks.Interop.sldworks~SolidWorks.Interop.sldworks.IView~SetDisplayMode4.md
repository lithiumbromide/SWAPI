---
title: "SetDisplayMode4 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "SetDisplayMode4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetDisplayMode4.html"
---

# SetDisplayMode4 Method (IView)

Sets the display mode of this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetDisplayMode4( _
   ByVal UseParent As System.Boolean, _
   ByVal Mode As System.Integer, _
   ByVal Faceted As System.Boolean, _
   ByVal Edges As System.Boolean, _
   ByVal CThreadHighQuality As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim UseParent As System.Boolean
Dim Mode As System.Integer
Dim Faceted As System.Boolean
Dim Edges As System.Boolean
Dim CThreadHighQuality As System.Boolean
Dim value As System.Boolean

value = instance.SetDisplayMode4(UseParent, Mode, Faceted, Edges, CThreadHighQuality)
```

### C#

```csharp
System.bool SetDisplayMode4(
   System.bool UseParent,
   System.int Mode,
   System.bool Faceted,
   System.bool Edges,
   System.bool CThreadHighQuality
)
```

### C++/CLI

```cpp
System.bool SetDisplayMode4(
   System.bool UseParent,
   System.int Mode,
   System.bool Faceted,
   System.bool Edges,
   System.bool CThreadHighQuality
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseParent`: True to use the parent's settings, false to use this drawing view's local settings (see **Remarks**)
- `Mode`: Display mode of the drawing view as defined in [swDisplayMode_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDisplayMode_e.html) (see **Remarks**)
- `Faceted`: True for draft quality, false for precision quality (see **Remarks**)
- `Edges`: True if edges are displayed when this view is in shaded mode, false if not
- `CThreadHighQuality`: True for precision quality cosmetic threads, false for draft quality

### Return Value

True if the display mode is reset, false if not

## VBA Syntax

See [View::SetDisplayMode4](ms-its:sldworksapivb6.chm::/sldworks~View~SetDisplayMode4.html).

## Examples

'VBA

'-------------------------------------
' Preconditions:
' 1. Open a drawing and select a drawing view.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the selected view's current display mode properties.
' 2. Resets the display mode properties.
' 3. Gets the new display mode properties.
' 4. Examine the Immediate window.
'--------------------------------------

Option Explicit
Sub main()

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swDraw As SldWorks.DrawingDoc
Dim swSheet As SldWorks.Sheet
Dim swView As SldWorks.View
Dim bRet As Boolean
Dim swSelectionMgr As SldWorks.SelectionMgr

Set swApp = SolidWorks.SldWorks
Set swModel = swApp.ActiveDoc
Set swDraw = swModel
Set swSheet = swDraw.GetCurrentSheet
Set swSelectionMgr = swModel.SelectionManager

Set swView = swSelectionMgr.GetSelectedObject6(1, -1)

Debug.Print "=====Current Display Mode======"
Debug.Print ""

Dim UseParentProp As Boolean
UseParentProp = swView.**GetUseParentDisplayMode**
Debug.Print "Using parent view's display mode? " & UseParentProp

Dim displayMode As Long
displayMode = swView.**GetDisplayMode2**
Debug.Print "Current display mode as defined by swDisplayMode_e: " & displayMode

Dim Faceted As Boolean
Faceted = swView.**GetFacettedHlrDisplay**
Debug.Print "Display faceted?: " & Faceted

Dim EdgesMode As Boolean
EdgesMode = swView.**GetDisplayEdgesInShadedMode**
Debug.Print "Display edges when the view is in shaded mode? " & EdgesMode

Dim cThreadQuality As Boolean
cThreadQuality = swView.**GetCThreadQuality**
Debug.Print "Precision quality for cosmetic threads? " & swView.GetCThreadQuality

swView.**SetDisplayMode4** False, 3, True, False, True

Debug.Print "=====After Re-setting Display Mode======"
Debug.Print ""
Debug.Print "Using parent view's display mode? " & swView.**GetUseParentDisplayMode**
Debug.Print "Current display mode as defined by swDisplayMode_e: " & swView.**GetDisplayMode2**
Debug.Print "Display faceted? " & swView.**GetFacettedHlrDisplay**
Debug.Print "Display edges when the view is in shaded mode? " & swView.**GetDisplayEdgesInShadedMode**
Debug.Print "Precision quality for cosmetic threads? " & swView.**GetCThreadQuality**

End Sub

## Examples

[Set Display Mode of View (VB.NET)](Set_Display_Mode_of_View_Example_VBNET.htm)
[Set Display Mode of View (C#)](Set_Display_Mode_of_View_Example_CSharp.htm)

## Remarks

If UseParent is true and a parent view:

- Exists, then this method's Mode, Faceted, and Edges parameters are ignored.
- Does not exist, then this method does not change the current display mode of this drawing view.

Mode specifies the drawing view display as defined by swDisplayMode_e.:

- swWIREFRAME
- swHIDDEN (Hidden Lines Removed)
- swHIDDEN_GREYED (Hidden Lines Visible)
- swSHADED
- swSHADED_EDGES

swDisplayMode_e also contains three other values that seem to indicate faceted (draft) geometry:

- swFACETED_WIREFRAME
- swFACETED_HIDDEN_GREYED
- swFACETED_HIDDEN

However in this method, you must use the Faceted parameter (not the Mode parameter) to specify draft or precision quality. If you specify Mode with swFACETED_WIREFRAME, swFACETED_HIDDEN_GREYED, or swFACETED_HIDDEN, then SOLIDWORKS instead uses swWIREFRAME, swHIDDEN_GREYED, or swHIDDEN.

NOTE: Just as displaying geometry precisely can decrease performance, setting the Faceted argument to true (draft quality) can increase performance.

| To determine for this view... | Use... |
| --- | --- |
| Whether its edges are displayed when it's in shaded mode | IView::GetDisplayEdgesInShadedMode |
| Whether its geometry is faceted | IView::GetFacettedHlrDisplay |
| Its current display mode | IView::GetDisplayMode2 |
| Whether its parent's display mode is being used | IView::GetUseParentDisplayMode |
| Its cosmetic thread display quality | IView::GetCThreadQuality |

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
