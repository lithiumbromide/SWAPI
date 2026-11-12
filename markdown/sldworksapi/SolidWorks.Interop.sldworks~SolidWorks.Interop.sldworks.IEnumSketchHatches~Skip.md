---
title: "Skip Method (IEnumSketchHatches)"
project: "SOLIDWORKS API Help"
interface: "IEnumSketchHatches"
member: "Skip"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchHatches~Skip.html"
---

# Skip Method (IEnumSketchHatches)

Skips the specified number of sketch hatches in the sketch hatches enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Skip( _
   ByVal Celt As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumSketchHatches
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

- `Celt`: Number of sketch hatches to skip

## VBA Syntax

See [EnumSketchHatches::Skip](ms-its:sldworksapivb6.chm::/sldworks~EnumSketchHatches~Skip.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumSketchHatches Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchHatches.html)
[IEnumSketchHatches Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchHatches_members.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
