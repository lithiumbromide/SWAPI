---
title: "UseThicknessRatioForOffset Property (IEndCapFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEndCapFeatureData"
member: "UseThicknessRatioForOffset"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData~UseThicknessRatioForOffset.html"
---

# UseThicknessRatioForOffset Property (IEndCapFeatureData)

Gets or sets whether a ratio of the thickness is used to specify the offset for this end-cap feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseThicknessRatioForOffset As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEndCapFeatureData
Dim value As System.Boolean

instance.UseThicknessRatioForOffset = value

value = instance.UseThicknessRatioForOffset
```

### C#

```csharp
System.bool UseThicknessRatioForOffset {get; set;}
```

### C++/CLI

```cpp
property System.bool UseThicknessRatioForOffset {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use a ratio of the thickness, false to not

## VBA Syntax

See [EndCapFeatureData::UseThicknessRatioForOffset](ms-its:sldworksapivb6.chm::/sldworks~EndCapFeatureData~UseThicknessRatioForOffset.html).

## Examples

See the [IEndCapFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEndCapFeatureData.html) examples.

## Remarks

| If this property is set to... | Then you can use... |
| --- | --- |
| True | IEndCapFeatureData::ThicknessRatioForOffset to set the offset distance of the end cap as a ratio of the thickness of the structural member being capped. |
| False | IEndCapFeatureData::OffsetDistance to set the offset distance for this end-cap feature. |

## See Also

[IEndCapFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData.html)
[IEndCapFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData_members.html)
[IEndCapFeatureData::Thickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData~Thickness.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
