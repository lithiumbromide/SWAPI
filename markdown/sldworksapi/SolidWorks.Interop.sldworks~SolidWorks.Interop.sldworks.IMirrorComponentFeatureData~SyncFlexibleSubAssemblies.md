---
title: "SyncFlexibleSubAssemblies Property (IMirrorComponentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorComponentFeatureData"
member: "SyncFlexibleSubAssemblies"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~SyncFlexibleSubAssemblies.html"
---

# SyncFlexibleSubAssemblies Property (IMirrorComponentFeatureData)

Gets or sets whether to synchronize the movement of mirrored components with the movement of seed components in the flexible subassembly.

## Syntax

### Visual Basic (Declaration)

```vb
Property SyncFlexibleSubAssemblies As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorComponentFeatureData
Dim value As System.Boolean

instance.SyncFlexibleSubAssemblies = value

value = instance.SyncFlexibleSubAssemblies
```

### C#

```csharp
System.bool SyncFlexibleSubAssemblies {get; set;}
```

### C++/CLI

```cpp
property System.bool SyncFlexibleSubAssemblies {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to synchronize movements of mirrored and seed flexible subassembly components, false to not

## VBA Syntax

See [MirrorComponentFeatureData::SyncFlexibleSubAssemblies](ms-its:sldworksapivb6.chm::/sldworks~MirrorComponentFeatureData~SyncFlexibleSubAssemblies.html).

## Examples

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html) example.

## See Also

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html)
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
