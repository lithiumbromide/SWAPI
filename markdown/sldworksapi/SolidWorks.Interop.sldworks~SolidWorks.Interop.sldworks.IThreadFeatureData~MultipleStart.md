---
title: "MultipleStart Property (IThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThreadFeatureData"
member: "MultipleStart"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~MultipleStart.html"
---

# MultipleStart Property (IThreadFeatureData)

Gets or sets whether the thread has multiple starts in this thread feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property MultipleStart As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IThreadFeatureData
Dim value As System.Boolean

instance.MultipleStart = value

value = instance.MultipleStart
```

### C#

```csharp
System.bool MultipleStart {get; set;}
```

### C++/CLI

```cpp
property System.bool MultipleStart {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the thread has multiple starts, false if not (default)

## VBA Syntax

See [ThreadFeatureData::MultipleStart](ms-its:sldworksapivb6.chm::/sldworks~ThreadFeatureData~MultipleStart.html).

## Examples

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html) examples.

## Remarks

If this property is set to true, use [IThreadFeatureData::NumberOfStarts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~NumberOfStarts.html) to set the number of times the thread is created in an evenly-spaced circular pattern around the hole or shaft.

[IThreadFeatureData::Pitch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~Pitch.html) must permit multiple starts without causing crossing or self-intersecting threads. For example, the pitch of one thread must be wide enough to allow the nesting of other threads of different pitch.

## See Also

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html)
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.html)
[IThreadFeatureData::TrimEndFace Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~TrimEndFace.html)
[IThreadFeatureData::TrimStartFace Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~TrimStartFace.html)
[IThreadFeatureData::RightHanded Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~RightHanded.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
