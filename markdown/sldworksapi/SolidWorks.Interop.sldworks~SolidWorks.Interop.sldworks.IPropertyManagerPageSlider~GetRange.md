---
title: "GetRange Method (IPropertyManagerPageSlider)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageSlider"
member: "GetRange"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider~GetRange.html"
---

# GetRange Method (IPropertyManagerPageSlider)

Gets the range of the slider.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetRange( _
   ByRef Min As System.Integer, _
   ByRef Max As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageSlider
Dim Min As System.Integer
Dim Max As System.Integer

instance.GetRange(Min, Max)
```

### C#

```csharp
void GetRange(
   out System.int Min,
   out System.int Max
)
```

### C++/CLI

```cpp
void GetRange(
   [Out] System.int Min,
   [Out] System.int Max
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Min`: Minimum range of slider
- `Max`: Maximum range of slider

## VBA Syntax

See [PropertyManagerPageSlider::GetRange](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageSlider~GetRange.html).

## Remarks

Use [IPropertyManagerPageSlider::SetRange](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageSlider~SetRange.html) to set the range of the slider.

## See Also

[IPropertyManagerPageSlider Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider.html)
[IPropertyManagerPageSlider Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
