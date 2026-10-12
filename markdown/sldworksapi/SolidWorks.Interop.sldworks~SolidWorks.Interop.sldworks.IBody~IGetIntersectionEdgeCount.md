---
title: "IGetIntersectionEdgeCount Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "IGetIntersectionEdgeCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IGetIntersectionEdgeCount.html"
---

# IGetIntersectionEdgeCount Method (IBody)

Obsolete. Superseded by [IBody2::IGetIntersectionEdgeCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IGetIntersectionEdgeCount.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetIntersectionEdgeCount( _
   ByVal ToolBodyIn As Body _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim ToolBodyIn As Body
Dim value As System.Integer

value = instance.IGetIntersectionEdgeCount(ToolBodyIn)
```

### C#

```csharp
System.int IGetIntersectionEdgeCount(
   Body ToolBodyIn
)
```

### C++/CLI

```cpp
System.int IGetIntersectionEdgeCount(
   Body^ ToolBodyIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ToolBodyIn`:

## VBA Syntax

See [Body::IGetIntersectionEdgeCount](ms-its:sldworksapivb6.chm::/sldworks~Body~IGetIntersectionEdgeCount.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
