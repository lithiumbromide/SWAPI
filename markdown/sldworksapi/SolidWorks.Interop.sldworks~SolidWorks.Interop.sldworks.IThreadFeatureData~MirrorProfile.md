---
title: "MirrorProfile Property (IThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThreadFeatureData"
member: "MirrorProfile"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~MirrorProfile.html"
---

# MirrorProfile Property (IThreadFeatureData)

Gets or sets whether to flip the profile of the thread helix about its horizontal or vertical axis in this thread feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property MirrorProfile As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IThreadFeatureData
Dim value As System.Boolean

instance.MirrorProfile = value

value = instance.MirrorProfile
```

### C#

```csharp
System.bool MirrorProfile {get; set;}
```

### C++/CLI

```cpp
property System.bool MirrorProfile {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to flip the profile of the thread helix about its horizontal or vertical axis, false to not (default)

## VBA Syntax

See [ThreadFeatureData::MirrorProfile](ms-its:sldworksapivb6.chm::/sldworks~ThreadFeatureData~MirrorProfile.html).

## Examples

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html) examples.

## Remarks

If this property is set to true, use [IThreadFeatureData::MirrorType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~MirrorType.html) to specify the axis about which to flip the thread helix profile.

## See Also

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html)
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
