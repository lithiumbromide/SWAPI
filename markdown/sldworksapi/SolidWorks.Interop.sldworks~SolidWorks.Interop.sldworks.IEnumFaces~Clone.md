---
title: "Clone Method (IEnumFaces)"
project: "SOLIDWORKS API Help"
interface: "IEnumFaces"
member: "Clone"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumFaces~Clone.html"
---

# Clone Method (IEnumFaces)

Obsolete. Superseded by [IEnumFaces2::Clone](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumFaces2~Clone.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub Clone( _
   ByRef Ppenum As EnumFaces _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumFaces
Dim Ppenum As EnumFaces

instance.Clone(Ppenum)
```

### C#

```csharp
void Clone(
   out EnumFaces Ppenum
)
```

### C++/CLI

```cpp
void Clone(
   [Out] EnumFaces^ Ppenum
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Ppenum`:

## VBA Syntax

See [EnumFaces::Clone](ms-its:sldworksapivb6.chm::/sldworks~EnumFaces~Clone.html).

## See Also

[IEnumFaces Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumFaces.html)
[IEnumFaces Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumFaces_members.html)
