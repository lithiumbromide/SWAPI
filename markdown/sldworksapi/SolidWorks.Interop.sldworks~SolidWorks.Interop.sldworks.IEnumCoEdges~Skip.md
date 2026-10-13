---
title: "Skip Method (IEnumCoEdges)"
project: "SOLIDWORKS API Help"
interface: "IEnumCoEdges"
member: "Skip"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumCoEdges~Skip.html"
---

# Skip Method (IEnumCoEdges)

Skips the specified number of coedges in the coedges enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Skip( _
   ByVal Celt As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumCoEdges
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

- `Celt`: Number of coedges to skip

## VBA Syntax

See [EnumCoEdges::Skip](ms-its:sldworksapivb6.chm::/sldworks~EnumCoEdges~Skip.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumCoEdges Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumCoEdges.html)
[IEnumCoEdges Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumCoEdges_members.html)
