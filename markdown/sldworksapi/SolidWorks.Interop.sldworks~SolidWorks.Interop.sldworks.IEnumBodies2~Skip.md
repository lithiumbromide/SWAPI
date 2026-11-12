---
title: "Skip Method (IEnumBodies2)"
project: "SOLIDWORKS API Help"
interface: "IEnumBodies2"
member: "Skip"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies2~Skip.html"
---

# Skip Method (IEnumBodies2)

Skips the specified number of bodies in the bodies enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Skip( _
   ByVal Celt As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumBodies2
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

- `Celt`: Number of bodies to skip

## VBA Syntax

See [EnumBodies2::Skip](ms-its:sldworksapivb6.chm::/sldworks~EnumBodies2~Skip.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumBodies2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies2.html)
[IEnumBodies2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
