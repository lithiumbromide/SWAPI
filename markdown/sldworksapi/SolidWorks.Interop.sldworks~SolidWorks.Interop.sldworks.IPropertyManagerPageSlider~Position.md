---
title: "Position Property (IPropertyManagerPageSlider)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageSlider"
member: "Position"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider~Position.html"
---

# Position Property (IPropertyManagerPageSlider)

Gets or sets the current position of the slider.

## Syntax

### Visual Basic (Declaration)

```vb
Property Position As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageSlider
Dim value As System.Integer

instance.Position = value

value = instance.Position
```

### C#

```csharp
System.int Position {get; set;}
```

### C++/CLI

```cpp
property System.int Position {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Current position of slider

## VBA Syntax

See [PropertyManagerPageSlider::Position](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageSlider~Position.html).

## Examples

[Set Up PropertyManager Page Slider Control (C++)](Set_Up_PropertyManager_Page_Slider_Control_Example_CPlusPlus_COM.htm)

## Remarks

Position must be a value within the specified range. To get the range, use [IPropertyManagerPageSlider::GetRange](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageSlider~GetRange.html); to set the range, use [IPropertyManagerPageSlider::SetRange](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageSlider~SetRange.html).

If you do not set the initial position of a slider, then the value defaults to a position of 5.

## See Also

[IPropertyManagerPageSlider Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider.html)
[IPropertyManagerPageSlider Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
