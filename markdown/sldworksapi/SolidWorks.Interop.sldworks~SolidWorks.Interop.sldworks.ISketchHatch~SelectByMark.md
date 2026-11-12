---
title: "SelectByMark Method (ISketchHatch)"
project: "SOLIDWORKS API Help"
interface: "ISketchHatch"
member: "SelectByMark"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~SelectByMark.html"
---

# SelectByMark Method (ISketchHatch)

Obsolete. Superseded by [ISketchHatch::Select4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchHatch~Select4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SelectByMark( _
   ByVal AppendFlag As System.Boolean, _
   ByVal Mark As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchHatch
Dim AppendFlag As System.Boolean
Dim Mark As System.Integer
Dim value As System.Boolean

value = instance.SelectByMark(AppendFlag, Mark)
```

### C#

```csharp
System.bool SelectByMark(
   System.bool AppendFlag,
   System.int Mark
)
```

### C++/CLI

```cpp
System.bool SelectByMark(
   System.bool AppendFlag,
   System.int Mark
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AppendFlag`:
- `Mark`:

## VBA Syntax

See [SketchHatch::SelectByMark](ms-its:sldworksapivb6.chm::/sldworks~SketchHatch~SelectByMark.html).

## See Also

[ISketchHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.html)
[ISketchHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch_members.html)
