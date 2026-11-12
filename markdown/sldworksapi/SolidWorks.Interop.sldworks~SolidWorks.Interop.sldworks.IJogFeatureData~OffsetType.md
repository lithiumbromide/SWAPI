---
title: "OffsetType Property (IJogFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IJogFeatureData"
member: "OffsetType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~OffsetType.html"
---

# OffsetType Property (IJogFeatureData)

Gets or sets the offset type for this jog feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property OffsetType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IJogFeatureData
Dim value As System.Integer

instance.OffsetType = value

value = instance.OffsetType
```

### C#

```csharp
System.int OffsetType {get; set;}
```

### C++/CLI

```cpp
property System.int OffsetType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Offset type as defined in [swJogOffsetTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swJogOffsetTypes_e.html)

## VBA Syntax

See [JogFeatureData::OffsetType](ms-its:sldworksapivb6.chm::/sldworks~JogFeatureData~OffsetType.html).

## See Also

[IJogFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.html)
[IJogFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData_members.html)
[IJogFeatureData::GetOffsetReferenceType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~GetOffsetReferenceType.html)
[IJogFeatureData::OffsetDistance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~OffsetDistance.html)
[IJogFeatureData::OffsetReference Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~OffsetReference.html)
[IJogFeatureData::ReverseOffset Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~ReverseOffset.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
