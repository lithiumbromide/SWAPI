---
title: "Clone Method (IEnumBodies2)"
project: "SOLIDWORKS API Help"
interface: "IEnumBodies2"
member: "Clone"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies2~Clone.html"
---

# Clone Method (IEnumBodies2)

Clones a bodies enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Clone( _
   ByRef Ppenum As EnumBodies2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumBodies2
Dim Ppenum As EnumBodies2

instance.Clone(Ppenum)
```

### C#

```csharp
void Clone(
   out EnumBodies2 Ppenum
)
```

### C++/CLI

```cpp
void Clone(
   [Out] EnumBodies2^ Ppenum
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Ppenum`: Pointer to the [bodies enumeration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumBodies2.html)

## VBA Syntax

See [EnumBodies2::Clone](ms-its:sldworksapivb6.chm::/sldworks~EnumBodies2~Clone.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumBodies2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies2.html)
[IEnumBodies2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
