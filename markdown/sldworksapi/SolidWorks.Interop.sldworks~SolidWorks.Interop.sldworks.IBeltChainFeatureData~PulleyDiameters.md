---
title: "PulleyDiameters Property (IBeltChainFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBeltChainFeatureData"
member: "PulleyDiameters"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~PulleyDiameters.html"
---

# PulleyDiameters Property (IBeltChainFeatureData)

Gets and sets the diameters of the pulleys.

## Syntax

### Visual Basic (Declaration)

```vb
Property PulleyDiameters As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBeltChainFeatureData
Dim value As System.Object

instance.PulleyDiameters = value

value = instance.PulleyDiameters
```

### C#

```csharp
System.object PulleyDiameters {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PulleyDiameters {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of diameters

## VBA Syntax

See [BeltChainFeatureData::PulleyDiameters](ms-its:sldworksapivb6.chm::/sldworks~BeltChainFeatureData~PulleyDiameters.html).

## Examples

See the [IBeltChainFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.html) examples.

## Remarks

The array maps one-to-one with the arrays of [IBeltChainFeatureData::PulleyComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~PulleyComponents.html) and [IBeltChainFeatureData::FlipSides](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~FlipSides.html).

## See Also

[IBeltChainFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.html)
[IBeltChainFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
