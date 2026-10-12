---
title: "Clone Method (IEnumLoops2)"
project: "SOLIDWORKS API Help"
interface: "IEnumLoops2"
member: "Clone"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumLoops2~Clone.html"
---

# Clone Method (IEnumLoops2)

Clones the loops enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Clone( _
   ByRef Ppenum As EnumLoops2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumLoops2
Dim Ppenum As EnumLoops2

instance.Clone(Ppenum)
```

### C#

```csharp
void Clone(
   out EnumLoops2 Ppenum
)
```

### C++/CLI

```cpp
void Clone(
   [Out] EnumLoops2^ Ppenum
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Ppenum`: Pointer to the clones [loops enumeration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumLoops2.html)

## VBA Syntax

See [EnumLoops2::Clone](ms-its:sldworksapivb6.chm::/sldworks~EnumLoops2~Clone.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumLoops2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumLoops2.html)
[IEnumLoops2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumLoops2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
