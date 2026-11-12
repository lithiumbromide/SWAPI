---
title: "IGetIntersectionEdges Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "IGetIntersectionEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IGetIntersectionEdges.html"
---

# IGetIntersectionEdges Method (IBody)

Obsolete. Superseded by [IBody2::IGetIntersectionEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IGetIntersectionEdges.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetIntersectionEdges( _
   ByVal ToolBodyIn As Body _
) As System.IntPtr
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim ToolBodyIn As Body
Dim value As System.IntPtr

value = instance.IGetIntersectionEdges(ToolBodyIn)
```

### C#

```csharp
System.IntPtr IGetIntersectionEdges(
   Body ToolBodyIn
)
```

### C++/CLI

```cpp
System.IntPtr IGetIntersectionEdges(
   Body^ ToolBodyIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ToolBodyIn`:

## VBA Syntax

See [Body::IGetIntersectionEdges](ms-its:sldworksapivb6.chm::/sldworks~Body~IGetIntersectionEdges.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
