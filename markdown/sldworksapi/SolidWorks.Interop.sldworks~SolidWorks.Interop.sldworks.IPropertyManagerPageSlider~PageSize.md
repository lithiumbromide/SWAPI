---
title: "PageSize Property (IPropertyManagerPageSlider)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageSlider"
member: "PageSize"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider~PageSize.html"
---

# PageSize Property (IPropertyManagerPageSlider)

Gets or sets how much the slider moves when the Page Up or Page Down keys are used to move the slider.

## Syntax

### Visual Basic (Declaration)

```vb
Property PageSize As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageSlider
Dim value As System.Integer

instance.PageSize = value

value = instance.PageSize
```

### C#

```csharp
System.int PageSize {get; set;}
```

### C++/CLI

```cpp
property System.int PageSize {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

How much the slider moves when the Page Up or Page Down keys are used to move the slider

## VBA Syntax

See [PropertyManagerPageSlider::PageSize](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageSlider~PageSize.html).

## Examples

[Set Up PropertyManager Page Slider Control (C++)](Set_Up_PropertyManager_Page_Slider_Control_Example_CPlusPlus_COM.htm)

## Remarks

If this property is not used to specified how the slider moves when the Page Up or Page Down keys are used to move the slider, the value defaults to 2.

## See Also

[IPropertyManagerPageSlider Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider.html)
[IPropertyManagerPageSlider Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
