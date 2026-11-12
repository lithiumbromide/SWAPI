---
title: "LineSize Property (IPropertyManagerPageSlider)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageSlider"
member: "LineSize"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider~LineSize.html"
---

# LineSize Property (IPropertyManagerPageSlider)

Gets or sets how much the slider moves when the arrow keys are used to move the slider.

## Syntax

### Visual Basic (Declaration)

```vb
Property LineSize As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageSlider
Dim value As System.Integer

instance.LineSize = value

value = instance.LineSize
```

### C#

```csharp
System.int LineSize {get; set;}
```

### C++/CLI

```cpp
property System.int LineSize {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

How much the slider moves when arrow keys are used to move the slider

## VBA Syntax

See [PropertyManagerPageSlider::LineSize](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageSlider~LineSize.html).

## Examples

[Set Up PropertyManager Page Slider Control (C++)](Set_Up_PropertyManager_Page_Slider_Control_Example_CPlusPlus_COM.htm)

## Remarks

If you do not set this property, the value defaults to 1.

## See Also

[IPropertyManagerPageSlider Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider.html)
[IPropertyManagerPageSlider Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
