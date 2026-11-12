---
title: "Select Method (ISketchRegion)"
project: "SOLIDWORKS API Help"
interface: "ISketchRegion"
member: "Select"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion~Select.html"
---

# Select Method (ISketchRegion)

Obsolete. Superseded by [ISketchRegion::Select2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRegion~Select2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function Select( _
   ByVal Append As System.Boolean, _
   ByVal Mark As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchRegion
Dim Append As System.Boolean
Dim Mark As System.Integer
Dim value As System.Boolean

value = instance.Select(Append, Mark)
```

### C#

```csharp
System.bool Select(
   System.bool Append,
   System.int Mark
)
```

### C++/CLI

```cpp
System.bool Select(
   System.bool Append,
   System.int Mark
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Append`:
- `Mark`:

## VBA Syntax

See [SketchRegion::Select](ms-its:sldworksapivb6.chm::/sldworks~SketchRegion~Select.html).

## See Also

[ISketchRegion Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion.html)
[ISketchRegion Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion_members.html)
