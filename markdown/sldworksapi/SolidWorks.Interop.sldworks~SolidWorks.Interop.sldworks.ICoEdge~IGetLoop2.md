---
title: "IGetLoop2 Method (ICoEdge)"
project: "SOLIDWORKS API Help"
interface: "ICoEdge"
member: "IGetLoop2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetLoop2.html"
---

# IGetLoop2 Method (ICoEdge)

Gets the loop containing this coedge.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetLoop2() As Loop2
```

### Visual Basic (Usage)

```vb
Dim instance As ICoEdge
Dim value As Loop2

value = instance.IGetLoop2()
```

### C#

```csharp
Loop2 IGetLoop2()
```

### C++/CLI

```cpp
Loop2^ IGetLoop2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [loop](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2.html)

## VBA Syntax

See [CoEdge::IGetLoop2](ms-its:sldworksapivb6.chm::/sldworks~CoEdge~IGetLoop2.html).

## See Also

[ICoEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge.html)
[ICoEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge_members.html)
[ICoEdge::GetLoop Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetLoop.html)
[ILoop2::GetFirstCoEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetFirstCoEdge.html)
[ILoop2::IGetFirstCoEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetFirstCoEdge.html)
