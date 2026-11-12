---
title: "Clone Method (IEnumSketchSegments)"
project: "SOLIDWORKS API Help"
interface: "IEnumSketchSegments"
member: "Clone"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchSegments~Clone.html"
---

# Clone Method (IEnumSketchSegments)

Clones the sketch segments enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Clone( _
   ByRef Ppenum As EnumSketchSegments _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumSketchSegments
Dim Ppenum As EnumSketchSegments

instance.Clone(Ppenum)
```

### C#

```csharp
void Clone(
   out EnumSketchSegments Ppenum
)
```

### C++/CLI

```cpp
void Clone(
   [Out] EnumSketchSegments^ Ppenum
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Ppenum`: Pointer to the cloned [sketch segments enumeration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumSketchSegments.html)

## VBA Syntax

See [EnumSketchSegments::Clone](ms-its:sldworksapivb6.chm::/sldworks~EnumSketchSegments~Clone.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumSketchSegments Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchSegments.html)
[IEnumSketchSegments Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchSegments_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
