---
title: "CornerTreatment Property (IFlatPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFlatPatternFeatureData"
member: "CornerTreatment"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~CornerTreatment.html"
---

# CornerTreatment Property (IFlatPatternFeatureData)

Gets or sets whether to apply smooth edges in the flat pattern to the Flat-Pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property CornerTreatment As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFlatPatternFeatureData
Dim value As System.Boolean

instance.CornerTreatment = value

value = instance.CornerTreatment
```

### C#

```csharp
System.bool CornerTreatment {get; set;}
```

### C++/CLI

```cpp
property System.bool CornerTreatment {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to apply smooth edges, false to not

## VBA Syntax

See [FlatPatternFeatureData::CornerTreatment](ms-its:sldworksapivb6.chm::/sldworks~FlatPatternFeatureData~CornerTreatment.html).

## See Also

[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.html)
[IFlatPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData_members.html)
[IFlatPatternFeatureData::ShowSlitInCornerRelief Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~ShowSlitInCornerRelief.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
