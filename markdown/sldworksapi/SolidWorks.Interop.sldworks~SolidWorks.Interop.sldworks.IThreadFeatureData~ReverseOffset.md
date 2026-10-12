---
title: "ReverseOffset Property (IThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThreadFeatureData"
member: "ReverseOffset"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~ReverseOffset.html"
---

# ReverseOffset Property (IThreadFeatureData)

Gets or sets whether to flip the offset of the helix to the opposite side of the starting entity in this thread feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseOffset As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IThreadFeatureData
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

True to flip the offset of the helix, false to not (default)

## VBA Syntax

See [ThreadFeatureData::ReverseOffset](ms-its:sldworksapivb6.chm::/sldworks~ThreadFeatureData~ReverseOffset.html).

## Examples

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html) examples.

## Remarks

This property is valid only if [IThreadFeatureData::Offset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~Offset.html) is set to true.

## See Also

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html)
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
