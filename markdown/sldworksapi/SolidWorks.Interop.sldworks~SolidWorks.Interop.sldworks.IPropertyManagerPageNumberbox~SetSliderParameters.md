---
title: "SetSliderParameters Method (IPropertyManagerPageNumberbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageNumberbox"
member: "SetSliderParameters"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~SetSliderParameters.html"
---

# SetSliderParameters Method (IPropertyManagerPageNumberbox)

Sets the parameters for the slider.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetSliderParameters( _
   ByVal PositionCount As System.Integer, _
   ByVal DivisionCount As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageNumberbox
Dim PositionCount As System.Integer
Dim DivisionCount As System.Integer

instance.SetSliderParameters(PositionCount, DivisionCount)
```

### C#

```csharp
void SetSliderParameters(
   System.int PositionCount,
   System.int DivisionCount
)
```

### C++/CLI

```cpp
void SetSliderParameters(
   System.int PositionCount,
   System.int DivisionCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PositionCount`: Number of discreet positions on the slider
- `DivisionCount`: Number of regions separated by tick marks on the slider

## VBA Syntax

See [PropertyManagerPageNumberbox::SetSliderParameters](ms-its:sldworksapivb6.chm::/Sldworks~PropertyManagerPageNumberbox~SetSliderParameters.html).

## Remarks

When a user drags the slider, PositionCount defines how sensitive the slider is. Not all of the specified discreet points are displayed if the PropertyManager page is not wide enough to show them. However, if the user widens the PropertyManager page, then more points are displayed.

When a user drags the slider, the user-interface tends to snap to the nearest tick mark when the drag is nearby, making it easier for the user to set whole values.

## See Also

[IPropertyManagerPageNumberbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox.html)
[IPropertyManagerPageNumberbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox_members.html)
[IPropertyManagerNumberbox::SetRange2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~SetRange2.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
