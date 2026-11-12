---
title: "BreakCornerRadius Property (IFlatPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFlatPatternFeatureData"
member: "BreakCornerRadius"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~BreakCornerRadius.html"
---

# BreakCornerRadius Property (IFlatPatternFeatureData)

Gets or sets the radius of the break corner for the Flat-Pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property BreakCornerRadius As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IFlatPatternFeatureData
Dim value As System.Double

instance.BreakCornerRadius = value

value = instance.BreakCornerRadius
```

### C#

```csharp
System.double BreakCornerRadius {get; set;}
```

### C++/CLI

```cpp
property System.double BreakCornerRadius {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Radius

## VBA Syntax

See [FlatPatternFeatureData::BreakCornerRadius](ms-its:sldworksapivb6.chm::/sldworks~FlatPatternFeatureData~BreakCornerRadius.html).

## See Also

[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.html)
[IFlatPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData_members.html)
[IFlatPatternFeatureData::IBreakCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData.html)
[IFlatPatternFeatureData::GetBreakCorners Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~GetBreakCorners.html)
[IFlatPatternFeatureData::SetBreakCorners Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~SetBreakCorners.html)
[IFlatPatternFeatureData::BreakCornerType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~BreakCornerType.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
