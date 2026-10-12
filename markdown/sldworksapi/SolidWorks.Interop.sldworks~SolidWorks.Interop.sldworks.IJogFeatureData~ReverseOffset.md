---
title: "ReverseOffset Property (IJogFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IJogFeatureData"
member: "ReverseOffset"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~ReverseOffset.html"
---

# ReverseOffset Property (IJogFeatureData)

Gets or sets whether to reverse the offset of this jog feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseOffset As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IJogFeatureData
Dim value As System.Boolean

instance.ReverseOffset = value

value = instance.ReverseOffset
```

### C#

```csharp
System.bool ReverseOffset {get; set;}
```

### C++/CLI

```cpp
property System.bool ReverseOffset {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True enables the reverse offset, false disables it

## VBA Syntax

See [JogFeatureData::ReverseOffset](ms-its:sldworksapivb6.chm::/sldworks~JogFeatureData~ReverseOffset.html).

## See Also

[IJogFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.html)
[IJogFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData_members.html)
[IJogFeatureData::GetOffsetReferenceType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~GetOffsetReferenceType.html)
[IJogFeatureData::OffsetDistance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~OffsetDistance.html)
[IJogFeatureData::OffsetReference Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~OffsetReference.html)
[IJogFeatureData::OffsetType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~OffsetType.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
