---
title: "MirrorType Property (IThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThreadFeatureData"
member: "MirrorType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~MirrorType.html"
---

# MirrorType Property (IThreadFeatureData)

Gets or sets how to flip the profile of the thread helix of this thread feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property MirrorType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IThreadFeatureData
Dim value As System.Integer

instance.MirrorType = value

value = instance.MirrorType
```

### C#

```csharp
System.int MirrorType {get; set;}
```

### C++/CLI

```cpp
property System.int MirrorType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Mirror profile type as defined in [swThreadMirrorType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swThreadMirrorType_e.html); default is swThreadMirrorType_e.swThreadMirrorType_Horizontally

## VBA Syntax

See [ThreadFeatureData::MirrorType](ms-its:sldworksapivb6.chm::/sldworks~ThreadFeatureData~MirrorType.html).

## Examples

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html) examples.

## Remarks

This property is valid only if [IThreadFeatureData::MirrorProfile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~MirrorProfile.html) is set to true.

## See Also

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html)
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
