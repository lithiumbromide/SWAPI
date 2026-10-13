---
title: "Skip Method (IEnumFaces2)"
project: "SOLIDWORKS API Help"
interface: "IEnumFaces2"
member: "Skip"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumFaces2~Skip.html"
---

# Skip Method (IEnumFaces2)

Skips the specified number of faces in the faces enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Skip( _
   ByVal Celt As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumFaces2
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

- `Celt`: Number of faces to skip

## VBA Syntax

See [EnumFaces2::Skip](ms-its:sldworksapivb6.chm::/sldworks~EnumFaces2~Skip.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumFaces2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumFaces2.html)
[IEnumFaces2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumFaces2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
