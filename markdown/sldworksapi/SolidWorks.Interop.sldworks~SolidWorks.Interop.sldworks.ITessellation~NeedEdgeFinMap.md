---
title: "NeedEdgeFinMap Property (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "NeedEdgeFinMap"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~NeedEdgeFinMap.html"
---

# NeedEdgeFinMap Property (ITessellation)

Gets or sets the need edge fin map option.

## Syntax

### Visual Basic (Declaration)

```vb
Property NeedEdgeFinMap As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim value As System.Boolean

instance.NeedEdgeFinMap = value

value = instance.NeedEdgeFinMap
```

### C#

```csharp
System.bool NeedEdgeFinMap {get; set;}
```

### C++/CLI

```cpp
property System.bool NeedEdgeFinMap {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True generates this information, false does not

## VBA Syntax

See [Tessellation::NeedEdgeFinMap](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~NeedEdgeFinMap.html).

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
