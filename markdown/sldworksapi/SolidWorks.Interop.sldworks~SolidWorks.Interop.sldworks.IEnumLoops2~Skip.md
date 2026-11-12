---
title: "Skip Method (IEnumLoops2)"
project: "SOLIDWORKS API Help"
interface: "IEnumLoops2"
member: "Skip"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumLoops2~Skip.html"
---

# Skip Method (IEnumLoops2)

Skips the specified number of loops in the loops enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Skip( _
   ByVal Celt As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumLoops2
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

- `Celt`: Number of loops

## VBA Syntax

See [EnumLoops2::Skip](ms-its:sldworksapivb6.chm::/sldworks~EnumLoops2~Skip.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumLoops2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumLoops2.html)
[IEnumLoops2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumLoops2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
