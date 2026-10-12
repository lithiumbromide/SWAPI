---
title: "Clone Method (IEnumFaces2)"
project: "SOLIDWORKS API Help"
interface: "IEnumFaces2"
member: "Clone"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumFaces2~Clone.html"
---

# Clone Method (IEnumFaces2)

Clones the faces enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Clone( _
   ByRef Ppenum As EnumFaces2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumFaces2
Dim Ppenum As EnumFaces2

instance.Clone(Ppenum)
```

### C#

```csharp
void Clone(
   out EnumFaces2 Ppenum
)
```

### C++/CLI

```cpp
void Clone(
   [Out] EnumFaces2^ Ppenum
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Ppenum`: Pointer to the cloned [faces enumeration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumFaces2.html)

## VBA Syntax

See [EnumFaces2::Clone](ms-its:sldworksapivb6.chm::/sldworks~EnumFaces2~Clone.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumFaces2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumFaces2.html)
[IEnumFaces2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumFaces2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
