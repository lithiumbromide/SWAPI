---
title: "HasLoadBearingFaces Property (IMate2)"
project: "SOLIDWORKS API Help"
interface: "IMate2"
member: "HasLoadBearingFaces"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~HasLoadBearingFaces.html"
---

# HasLoadBearingFaces Property (IMate2)

Gets whether this mate has load bearing faces.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property HasLoadBearingFaces As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMate2
Dim value As System.Boolean

value = instance.HasLoadBearingFaces
```

### C#

```csharp
System.bool HasLoadBearingFaces {get;}
```

### C++/CLI

```cpp
property System.bool HasLoadBearingFaces {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the mate has load bearing faces, false if not

## VBA Syntax

See [Mate2::HasLoadBearingFaces](ms-its:sldworksapivb6.chm::/sldworks~Mate2~HasLoadBearingFaces.html).

## See Also

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.html)
[IMate2::IsLoadBearingFacesBonded Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~IsLoadBearingFacesBonded.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
