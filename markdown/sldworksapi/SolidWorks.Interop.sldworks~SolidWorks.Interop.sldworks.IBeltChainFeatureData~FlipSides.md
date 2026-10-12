---
title: "FlipSides Property (IBeltChainFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBeltChainFeatureData"
member: "FlipSides"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~FlipSides.html"
---

# FlipSides Property (IBeltChainFeatureData)

Gets and sets whether to flip the belt to the other side of each pulley.

## Syntax

### Visual Basic (Declaration)

```vb
Property FlipSides As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBeltChainFeatureData
Dim value As System.Object

instance.FlipSides = value

value = instance.FlipSides
```

### C#

```csharp
System.object FlipSides {get; set;}
```

### C++/CLI

```cpp
property System.Object^ FlipSides {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of booleans; true to flip pulley sides, false to not

## VBA Syntax

See [BeltChainFeatureData::FlipSides](ms-its:sldworksapivb6.chm::/sldworks~BeltChainFeatureData~FlipSides.html).

## Examples

See the [IBeltChainFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.html) examples.

## Remarks

The array maps one-to-one with the arrays of [IBeltChainFeatureData::PulleyComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~PulleyComponents.html) and [IBeltChainFeatureData::PulleyDiameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~PulleyDiameters.html).

## See Also

[IBeltChainFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.html)
[IBeltChainFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
