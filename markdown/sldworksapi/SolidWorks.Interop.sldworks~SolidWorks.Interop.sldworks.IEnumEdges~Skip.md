---
title: "Skip Method (IEnumEdges)"
project: "SOLIDWORKS API Help"
interface: "IEnumEdges"
member: "Skip"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumEdges~Skip.html"
---

# Skip Method (IEnumEdges)

Skips the specified number edges in the edges enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Skip( _
   ByVal Celt As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumEdges
Dim Celt As System.Integer

instance.Skip(Celt)
```

### C#

```csharp
void Skip(
   System.int Celt
)
```

### C++/CLI

```cpp
void Skip(
   System.int Celt
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Celt`: Number of edges to skip

## VBA Syntax

See [EnumEdges::Skip](ms-its:sldworksapivb6.chm::/sldworks~EnumEdges~Skip.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumEdges Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumEdges.html)
[IEnumEdges Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumEdges_members.html)
