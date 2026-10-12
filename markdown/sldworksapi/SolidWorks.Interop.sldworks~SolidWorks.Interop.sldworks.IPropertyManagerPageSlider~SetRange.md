---
title: "SetRange Method (IPropertyManagerPageSlider)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageSlider"
member: "SetRange"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider~SetRange.html"
---

# SetRange Method (IPropertyManagerPageSlider)

Sets the range of a slider.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetRange( _
   ByVal Min As System.Integer, _
   ByVal Max As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageSlider
Dim Min As System.Integer
Dim Max As System.Integer
Dim value As System.Boolean

value = instance.SetRange(Min, Max)
```

### C#

```csharp
System.bool SetRange(
   System.int Min,
   System.int Max
)
```

### C++/CLI

```cpp
System.bool SetRange(
   System.int Min,
   System.int Max
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Min`: Minimum range of slider
- `Max`: Maximum range of slider

### Return Value

True if range is set, false if not

## VBA Syntax

See [PropertyManagerPageSlider::SetRange](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageSlider~SetRange.html).

## Examples

[Set Up PropertyManager Page Slider Control (C++)](Set_Up_PropertyManager_Page_Slider_Control_Example_CPlusPlus_COM.htm)

## Remarks

If you do not use this method to specify the range, it will default to a range of 0 to 10. Use [IPropertyManagerPageStyle::GetRange](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageSlider~GetRange.html) to get the current range of the slider.

## See Also

[IPropertyManagerPageSlider Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider.html)
[IPropertyManagerPageSlider Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider_members.html)
