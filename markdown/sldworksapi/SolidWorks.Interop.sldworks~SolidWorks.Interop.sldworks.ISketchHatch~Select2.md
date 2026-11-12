---
title: "Select2 Method (ISketchHatch)"
project: "SOLIDWORKS API Help"
interface: "ISketchHatch"
member: "Select2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~Select2.html"
---

# Select2 Method (ISketchHatch)

Obsolete. Superseded by [ISketchHatch::Select4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchHatch~Select4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function Select2( _
   ByVal Append As System.Boolean, _
   ByVal Mark As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchHatch
Dim Append As System.Boolean
Dim Mark As System.Integer
Dim value As System.Boolean

value = instance.Select2(Append, Mark)
```

### C#

```csharp
System.bool Select2(
   System.bool Append,
   System.int Mark
)
```

### C++/CLI

```cpp
System.bool Select2(
   System.bool Append,
   System.int Mark
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Append`:
- `Mark`:

## VBA Syntax

See [SketchHatch::Select2](ms-its:sldworksapivb6.chm::/sldworks~SketchHatch~Select2.html).

## See Also

[ISketchHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.html)
[ISketchHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch_members.html)
