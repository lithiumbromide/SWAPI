---
title: "Select Method (ISketchContour)"
project: "SOLIDWORKS API Help"
interface: "ISketchContour"
member: "Select"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour~Select.html"
---

# Select Method (ISketchContour)

Obsolete. Superseded by [ISketchContour::Select2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchContour~Select2.html).

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
Dim instance As ISketchContour
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

See [SketchContour::Select](ms-its:sldworksapivb6.chm::/sldworks~SketchContour~Select.html).

## See Also

[ISketchContour Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour.html)
[ISketchContour Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour_members.html)
