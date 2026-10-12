---
title: "TrimStartFace Property (IThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThreadFeatureData"
member: "TrimStartFace"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~TrimStartFace.html"
---

# TrimStartFace Property (IThreadFeatureData)

Gets or sets whether to align the thread to the start face of this thread feaure.

## Syntax

### Visual Basic (Declaration)

```vb
Property TrimStartFace As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IThreadFeatureData
Dim value As System.Boolean

instance.TrimStartFace = value

value = instance.TrimStartFace
```

### C#

```csharp
System.bool TrimStartFace {get; set;}
```

### C++/CLI

```cpp
property System.bool TrimStartFace {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to align the thread to the start face, false to not (default)

## VBA Syntax

See [ThreadFeatureData::TrimStartFace](ms-its:sldworksapivb6.chm::/sldworks~ThreadFeatureData~TrimStartFace.html).

## Examples

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html) examples.

## Remarks

This property is valid only if the thread profile extends beyond the trimming face.

## See Also

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html)
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.html)
[IThreadFeatureData::TrimEndFace Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~TrimEndFace.html)
[IThreadFeatureData::MultipleStart Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~MultipleStart.html)
[IThreadFeatureData::RightHanded Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~RightHanded.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
