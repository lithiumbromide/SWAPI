---
title: "Clone Method (IEnumEdges)"
project: "SOLIDWORKS API Help"
interface: "IEnumEdges"
member: "Clone"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumEdges~Clone.html"
---

# Clone Method (IEnumEdges)

Clones the edges enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Clone( _
   ByRef Ppenum As EnumEdges _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumEdges
Dim Ppenum As EnumEdges

instance.Clone(Ppenum)
```

### C#

```csharp
void Clone(
   out EnumEdges Ppenum
)
```

### C++/CLI

```cpp
void Clone(
   [Out] EnumEdges^ Ppenum
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Ppenum`: Pointer to the clones [edges enumeration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumEdges.html)

## VBA Syntax

See [EnumEdges::Clone](ms-its:sldworksapivb6.chm::/sldworks~EnumEdges~Clone.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumEdges Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumEdges.html)
[IEnumEdges Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumEdges_members.html)
