---
title: "MaintainThreadLength Property (IThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThreadFeatureData"
member: "MaintainThreadLength"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~MaintainThreadLength.html"
---

# MaintainThreadLength Property (IThreadFeatureData)

Gets or sets whether to keep the thread a constant length from the starting surface in this thread feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaintainThreadLength As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IThreadFeatureData
Dim value As System.Boolean

instance.MaintainThreadLength = value

value = instance.MaintainThreadLength
```

### C#

```csharp
System.bool MaintainThreadLength {get; set;}
```

### C++/CLI

```cpp
property System.bool MaintainThreadLength {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to maintain a constant thread length, false to not (default)

## VBA Syntax

See [ThreadFeatureData::MaintainThreadLength](ms-its:sldworksapivb6.chm::/sldworks~ThreadFeatureData~MaintainThreadLength.html).

## Examples

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html) examples.

## Remarks

This property is valid only if:

- [IThreadFeatureData::Offset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~Offset.html) is set to true.
- [IThreadFeatureData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~EndCondition.html) is set to [swThreadEndCondition_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swThreadEndCondition_e.html):

- swThreadEndCondition_Blind

- or -

- swThreadEndCondition_Revolutions

## See Also

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html)
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
