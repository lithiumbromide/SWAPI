---
title: "ThicknessRatioForOffset Property (IEndCapFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEndCapFeatureData"
member: "ThicknessRatioForOffset"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData~ThicknessRatioForOffset.html"
---

# ThicknessRatioForOffset Property (IEndCapFeatureData)

Gets or sets the offset distance of the end cap as a ratio of the thickness of the structural member being capped.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThicknessRatioForOffset As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IEndCapFeatureData
Dim value As System.Double

instance.ThicknessRatioForOffset = value

value = instance.ThicknessRatioForOffset
```

### C#

```csharp
System.double ThicknessRatioForOffset {get; set;}
```

### C++/CLI

```cpp
property System.double ThicknessRatioForOffset {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Ratio of the thickness

## VBA Syntax

See [EndCapFeatureData::ThicknessRatioForOffset](ms-its:sldworksapivb6.chm::/sldworks~EndCapFeatureData~ThicknessRatioForOffset.html).

## Examples

See the [IEndCapFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEndCapFeatureData.html) examples.

## Remarks

[IEndCapFeatureData::UseThicknessRatioForOffset](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEndCapFeatureData~UseThicknessRatioForOffset.html) must be set to true for this property to have an effect.

## See Also

[IEndCapFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData.html)
[IEndCapFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData_members.html)
[IEndCapFeatureData::Thickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData~Thickness.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
