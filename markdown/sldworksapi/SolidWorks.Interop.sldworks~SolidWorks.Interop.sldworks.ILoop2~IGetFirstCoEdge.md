---
title: "IGetFirstCoEdge Method (ILoop2)"
project: "SOLIDWORKS API Help"
interface: "ILoop2"
member: "IGetFirstCoEdge"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetFirstCoEdge.html"
---

# IGetFirstCoEdge Method (ILoop2)

Gets the first coedge in the loop.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFirstCoEdge() As CoEdge
```

### Visual Basic (Usage)

```vb
Dim instance As ILoop2
Dim value As CoEdge

value = instance.IGetFirstCoEdge()
```

### C#

```csharp
CoEdge IGetFirstCoEdge()
```

### C++/CLI

```cpp
CoEdge^ IGetFirstCoEdge();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First [coedge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoEdge.html) in loop

## VBA Syntax

See [Loop2::IGetFirstCoEdge](ms-its:sldworksapivb6.chm::/sldworks~Loop2~IGetFirstCoEdge.html).

## Remarks

The [ICoEdge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoEdge.html) objects are returned in a CW or CCW manner based on the direction of the [ILoop2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2.html).

The loop direction is determined as follows: if a loop is viewed along its direction, with the face normal pointing upwards, then the face that owns the loop is to the left. This means that inner loops are CW and outer loops are CCW. To determine if a loop is an outer loop, see [ILoop2::IsOuter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2~IsOuter.html).

The coedge direction always aligns with the direction of the loop.

## See Also

[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.html)
[ILoop2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2_members.html)
[ILoop2::GetFirstCoEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetFirstCoEdge.html)
[ILoop2::EnumCoEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~EnumCoEdges.html)
[ILoop2::GetCoEdgeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetCoEdgeCount.html)
[ILoop2::GetCoEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetCoEdges.html)
[ILoop2::GetFirstCoEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetFirstCoEdge.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
