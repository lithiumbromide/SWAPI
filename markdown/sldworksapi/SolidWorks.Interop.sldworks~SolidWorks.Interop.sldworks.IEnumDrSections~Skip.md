---
title: "Skip Method (IEnumDrSections)"
project: "SOLIDWORKS API Help"
interface: "IEnumDrSections"
member: "Skip"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDrSections~Skip.html"
---

# Skip Method (IEnumDrSections)

Skips the specified number of section views in the section views enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Skip( _
   ByVal Celt As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumDrSections
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

- `Celt`: Number of section views to skip

## VBA Syntax

See [EnumDrSections::Skip](ms-its:sldworksapivb6.chm::/sldworks~EnumDrSections~Skip.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumDrSections Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDrSections.html)
[IEnumDrSections Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDrSections_members.html)
