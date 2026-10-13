---
title: "Clone Method (IEnumCoEdges)"
project: "SOLIDWORKS API Help"
interface: "IEnumCoEdges"
member: "Clone"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumCoEdges~Clone.html"
---

# Clone Method (IEnumCoEdges)

Clones the a coedges enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Clone( _
   ByRef Ppenum As EnumCoEdges _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumCoEdges
Dim Ppenum As EnumCoEdges

instance.Clone(Ppenum)
```

### C#

```csharp
void Clone(
   out EnumCoEdges Ppenum
)
```

### C++/CLI

```cpp
void Clone(
   [Out] EnumCoEdges^ Ppenum
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Ppenum`: Pointer to the cloned [coedges enumeration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumCoEdges.html)

## VBA Syntax

See [EnumCoEdges::Clone](ms-its:sldworksapivb6.chm::/sldworks~EnumCoEdges~Clone.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumCoEdges Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumCoEdges.html)
[IEnumCoEdges Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumCoEdges_members.html)
