---
title: "IsLoadBearingFacesBonded Property (IMate2)"
project: "SOLIDWORKS API Help"
interface: "IMate2"
member: "IsLoadBearingFacesBonded"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~IsLoadBearingFacesBonded.html"
---

# IsLoadBearingFacesBonded Property (IMate2)

Get whether the load bearing faces of this mate are bonded.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IsLoadBearingFacesBonded As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMate2
Dim value As System.Boolean

value = instance.IsLoadBearingFacesBonded
```

### C#

```csharp
System.bool IsLoadBearingFacesBonded {get;}
```

### C++/CLI

```cpp
property System.bool IsLoadBearingFacesBonded {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the load-bearing faces of this mate are bonded, false if not

## VBA Syntax

See [Mate2::IsLoadBearingFacesBonded](ms-its:sldworksapivb6.chm::/sldworks~Mate2~IsLoadBearingFacesBonded.html).

## See Also

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.html)
[IMate2::HasLoadBearingFaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~HasLoadBearingFaces.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
