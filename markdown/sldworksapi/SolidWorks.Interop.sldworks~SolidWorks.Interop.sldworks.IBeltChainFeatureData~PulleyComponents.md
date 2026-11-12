---
title: "PulleyComponents Property (IBeltChainFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBeltChainFeatureData"
member: "PulleyComponents"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~PulleyComponents.html"
---

# PulleyComponents Property (IBeltChainFeatureData)

Gets and sets the components in this belt/chain assembly feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PulleyComponents As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBeltChainFeatureData
Dim value As System.Object

instance.PulleyComponents = value

value = instance.PulleyComponents
```

### C#

```csharp
System.object PulleyComponents {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PulleyComponents {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of pulley members, e.g., cylindrical faces, axes, wheels, gears

## VBA Syntax

See [BeltChainFeatureData::PulleyComponents](ms-its:sldworksapivb6.chm::/sldworks~BeltChainFeatureData~PulleyComponents.html).

## Examples

See the [IBeltChainFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.html) examples.

## Remarks

The array maps one-to-one with the arrays of [IBeltChainFeatureData::FlipSides](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~FlipSides.html) and [IBeltChainFeatureData::PulleyDiameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~PulleyDiameters.html).

## See Also

[IBeltChainFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.html)
[IBeltChainFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
