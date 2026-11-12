---
title: "Skip Method (IEnumSketchPoints)"
project: "SOLIDWORKS API Help"
interface: "IEnumSketchPoints"
member: "Skip"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchPoints~Skip.html"
---

# Skip Method (IEnumSketchPoints)

Skips the specified number of sketch points in the sketch points enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Skip( _
   ByVal Celt As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumSketchPoints
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

- `Celt`: Number of sketch points to skip

## VBA Syntax

See [EnumSketchPoints::Skip](ms-its:sldworksapivb6.chm::/sldworks~EnumSketchPoints~Skip.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumSketchPoints Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchPoints.html)
[IEnumSketchPoints Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchPoints_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
