---
title: "Clone Method (IEnumSketchPoints)"
project: "SOLIDWORKS API Help"
interface: "IEnumSketchPoints"
member: "Clone"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchPoints~Clone.html"
---

# Clone Method (IEnumSketchPoints)

Clones the sketch points enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Clone( _
   ByRef Ppenum As EnumSketchPoints _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumSketchPoints
Dim Ppenum As EnumSketchPoints

instance.Clone(Ppenum)
```

### C#

```csharp
void Clone(
   out EnumSketchPoints Ppenum
)
```

### C++/CLI

```cpp
void Clone(
   [Out] EnumSketchPoints^ Ppenum
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Ppenum`: Pointer to the cloned [sketch points enumeration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumSketchPoints.html)

## VBA Syntax

See [EnumSketchPoints::Clone](ms-its:sldworksapivb6.chm::/sldworks~EnumSketchPoints~Clone.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumSketchPoints Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchPoints.html)
[IEnumSketchPoints Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchPoints_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
