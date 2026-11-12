---
title: "RightHanded Property (IThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThreadFeatureData"
member: "RightHanded"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~RightHanded.html"
---

# RightHanded Property (IThreadFeatureData)

Gets or sets how the thread is wound in this thread feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property RightHanded As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IThreadFeatureData
Dim value As System.Boolean

instance.RightHanded = value

value = instance.RightHanded
```

### C#

```csharp
System.bool RightHanded {get; set;}
```

### C++/CLI

```cpp
property System.bool RightHanded {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the thread is wound clockwise (default), false if counter clockwise

## VBA Syntax

See [ThreadFeatureData::RightHanded](ms-its:sldworksapivb6.chm::/sldworks~ThreadFeatureData~RightHanded.html).

## Examples

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html) examples.

## See Also

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html)
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.html)
[IThreadFeatureData::MultipleStart Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~MultipleStart.html)
[IThreadFeatureData::TrimEndFace Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~TrimEndFace.html)
[IThreadFeatureData::TrimStartFace Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~TrimStartFace.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
