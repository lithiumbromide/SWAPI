---
title: "OffsetDistance Property (IJogFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IJogFeatureData"
member: "OffsetDistance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~OffsetDistance.html"
---

# OffsetDistance Property (IJogFeatureData)

Gets or sets the offset distance for this jog feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property OffsetDistance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IJogFeatureData
Dim value As System.Double

instance.OffsetDistance = value

value = instance.OffsetDistance
```

### C#

```csharp
System.double OffsetDistance {get; set;}
```

### C++/CLI

```cpp
property System.double OffsetDistance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Offset distance

## VBA Syntax

See [JogFeatureData::OffsetDistance](ms-its:sldworksapivb6.chm::/sldworks~JogFeatureData~OffsetDistance.html).

## See Also

[IJogFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.html)
[IJogFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData_members.html)
[IJogFeatureData::GetOffsetReferenceType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~GetOffsetReferenceType.html)
[IJogFeatureData::OffsetReference Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~OffsetReference.html)
[IJogFeatureData::OffsetType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~OffsetType.html)
[IJogFeatureData::ReverseOffset Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~ReverseOffset.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
