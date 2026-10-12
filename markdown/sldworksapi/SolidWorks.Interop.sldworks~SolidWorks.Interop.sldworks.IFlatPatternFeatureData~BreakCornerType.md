---
title: "BreakCornerType Property (IFlatPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFlatPatternFeatureData"
member: "BreakCornerType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~BreakCornerType.html"
---

# BreakCornerType Property (IFlatPatternFeatureData)

Gets or sets the type of break corner for the Flat-Pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property BreakCornerType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFlatPatternFeatureData
Dim value As System.Integer

instance.BreakCornerType = value

value = instance.BreakCornerType
```

### C#

```csharp
System.int BreakCornerType {get; set;}
```

### C++/CLI

```cpp
property System.int BreakCornerType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of break corner as defined in [swBreakCornerTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBreakCornerTypes_e.html)

## VBA Syntax

See [FlatPatternFeatureData::BreakCornerType](ms-its:sldworksapivb6.chm::/sldworks~FlatPatternFeatureData~BreakCornerType.html).

## See Also

[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.html)
[IFlatPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData_members.html)
[IFlatPatternFeatureData::GetBreakCorners Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~GetBreakCorners.html)
[IFlatPatternFeatureData::SetBreakCorners Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~SetBreakCorners.html)
[IFlatPatternFeatureData::BreakCornerRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~BreakCornerRadius.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
