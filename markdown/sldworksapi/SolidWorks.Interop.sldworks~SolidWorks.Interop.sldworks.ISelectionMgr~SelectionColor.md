---
title: "SelectionColor Property (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "SelectionColor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~SelectionColor.html"
---

# SelectionColor Property (ISelectionMgr)

Gets or sets the selection color.

## Syntax

### Visual Basic (Declaration)

```vb
Property SelectionColor( _
   ByVal Mark As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim Mark As System.Integer
Dim value As System.Integer

instance.SelectionColor(Mark) = value

value = instance.SelectionColor(Mark)
```

### C#

```csharp
System.int SelectionColor(
   System.int Mark
) {get; set;}
```

### C++/CLI

```cpp
property System.int SelectionColor {
   System.int get(System.int Mark);
   void set (System.int Mark, System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Mark`: Mark value (see **Remarks**)

### Property Value

Value indicating the color to use for a selection as defined by swSystemColors; these values are from [swUserPreferenceIntegerValue_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceIntegerValue_e.html) (see Remarks)

## VBA Syntax

See [SelectionMgr::SelectionColor](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~SelectionColor.html).

## Remarks

You should have a set of marks that you want to apply to selected objects. These marks are application specific and should be designed to present to the user a visual collection of like objects.

The values that SOLIDWORKS internal dialogs typically use for selection colors are:

- swSystemColorsSelectedItem1
- swSystemColorsSelectedItem2
- swSystemColorsSelectedItem3

You can also specify any of the following values:

- swSystemColorsViewportBackground
- swSystemColorsTopGradientColor
- swSystemColorsBottomGradientColor
- swSystemColorsDynamicHighlight
- swSystemColorsHighlight
- swSystemColorsSelectedFaceShaded
- swSystemColorsDrawingsVisibleModelEdge
- swSystemColorsDrawingsHiddenModelEdge

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)
[ISelectionMgr::ClearSelectionColors Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~ClearSelectionColors.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
