---
title: "Clone Method (IEnumDrSections)"
project: "SOLIDWORKS API Help"
interface: "IEnumDrSections"
member: "Clone"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDrSections~Clone.html"
---

# Clone Method (IEnumDrSections)

Clones the section views enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Clone( _
   ByRef Ppenum As EnumDrSections _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumDrSections
Dim Ppenum As EnumDrSections

instance.Clone(Ppenum)
```

### C#

```csharp
void Clone(
   out EnumDrSections Ppenum
)
```

### C++/CLI

```cpp
void Clone(
   [Out] EnumDrSections^ Ppenum
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Ppenum`: Pointer to the cloned [section views enumeration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumDrSections.html)

## VBA Syntax

See [EnumDrSections::Clone](ms-its:sldworksapivb6.chm::/sldworks~EnumDrSections~Clone.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumDrSections Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDrSections.html)
[IEnumDrSections Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDrSections_members.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
