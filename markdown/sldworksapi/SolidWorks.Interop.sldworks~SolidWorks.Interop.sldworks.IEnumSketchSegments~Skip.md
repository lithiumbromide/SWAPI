---
title: "Skip Method (IEnumSketchSegments)"
project: "SOLIDWORKS API Help"
interface: "IEnumSketchSegments"
member: "Skip"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchSegments~Skip.html"
---

# Skip Method (IEnumSketchSegments)

Skips the specified number of sketch segments in the sketch segments enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Skip( _
   ByVal Celt As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumSketchSegments
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

- `Celt`: Number of sketch segments to skip

## VBA Syntax

See [EnumSketchSegments::Skip](ms-its:sldworksapivb6.chm::/sldworks~EnumSketchSegments~Skip.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumSketchSegments Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchSegments.html)
[IEnumSketchSegments Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchSegments_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
