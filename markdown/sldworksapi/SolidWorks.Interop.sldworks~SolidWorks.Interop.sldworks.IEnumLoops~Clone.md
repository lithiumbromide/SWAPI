---
title: "Clone Method (IEnumLoops)"
project: "SOLIDWORKS API Help"
interface: "IEnumLoops"
member: "Clone"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumLoops~Clone.html"
---

# Clone Method (IEnumLoops)

Obsolete. Superseded by [IEnumLoops2::Clone](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumLoops2~Clone.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub Clone( _
   ByRef Ppenum As EnumLoops _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumLoops
Dim Ppenum As EnumLoops

instance.Clone(Ppenum)
```

### C#

```csharp
void Clone(
   out EnumLoops Ppenum
)
```

### C++/CLI

```cpp
void Clone(
   [Out] EnumLoops^ Ppenum
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Ppenum`:

## VBA Syntax

See [EnumLoops::Clone](ms-its:sldworksapivb6.chm::/sldworks~EnumLoops~Clone.html).

## See Also

[IEnumLoops Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumLoops.html)
[IEnumLoops Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumLoops_members.html)
