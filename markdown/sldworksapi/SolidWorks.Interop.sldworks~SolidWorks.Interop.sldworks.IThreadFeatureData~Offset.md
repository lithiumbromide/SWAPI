---
title: "Offset Property (IThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThreadFeatureData"
member: "Offset"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~Offset.html"
---

# Offset Property (IThreadFeatureData)

Gets or sets whether to offset the starting location of the helix of this thread feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Offset As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IThreadFeatureData
Dim value As System.Boolean

instance.Offset = value

value = instance.Offset
```

### C#

```csharp
System.bool Offset {get; set;}
```

### C++/CLI

```cpp
property System.bool Offset {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True of offset the starting location of the thread helix, false to not (default)

## VBA Syntax

See [ThreadFeatureData::Offset](ms-its:sldworksapivb6.chm::/sldworks~ThreadFeatureData~Offset.html).

## Examples

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html) examples.

## See Also

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html)
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.html)
[IThreadFeatureData::MaintainThreadLength Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~MaintainThreadLength.html)
[IThreadFeatureData::OffsetDistance Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~OffsetDistance.html)
[IThreadFeatureData::ReverseOffset Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~ReverseOffset.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
