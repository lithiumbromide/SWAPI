---
title: "EnumCoEdges Method (ILoop2)"
project: "SOLIDWORKS API Help"
interface: "ILoop2"
member: "EnumCoEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~EnumCoEdges.html"
---

# EnumCoEdges Method (ILoop2)

Enumerates the coedges in a loop.

## Syntax

### Visual Basic (Declaration)

```vb
Function EnumCoEdges() As EnumCoEdges
```

### Visual Basic (Usage)

```vb
Dim instance As ILoop2
Dim value As EnumCoEdges

value = instance.EnumCoEdges()
```

### C#

```csharp
EnumCoEdges EnumCoEdges()
```

### C++/CLI

```cpp
EnumCoEdges^ EnumCoEdges();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Coedges enumeration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumCoEdges.html)

## VBA Syntax

See [Loop2::EnumCoEdges](ms-its:sldworksapivb6.chm::/sldworks~Loop2~EnumCoEdges.html).

## Remarks

The [ICoEdge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoEdge.html) objects are returned in a CW or CCW manner based on the direction of the [ILoop2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2.html).

The loop direction is determined as follows: if a loop is viewed along its direction, with the face normal pointing upwards, then the face that owns the loop is to the left. This means that inner loops are CW and outer loops are CCW. To determine if a loop is an outer loop, see [ILoop2::IsOuter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2~IsOuter.html).

The coedge direction always aligns with the direction of the ILoop2.

## See Also

[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.html)
[ILoop2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2_members.html)
[ILoop2::GetFirstCoEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetFirstCoEdge.html)
[ILoop2::IGetFirstCoEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetFirstCoEdge.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
