---
title: "SelectByMark Method (ISketchSegment)"
project: "SOLIDWORKS API Help"
interface: "ISketchSegment"
member: "SelectByMark"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~SelectByMark.html"
---

# SelectByMark Method (ISketchSegment)

Obsolete. Superseded by [ISketchSegment::Select4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment~Select4.html).

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
Dim instance As ISketchSegment
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

See [SketchSegment::SelectByMark](ms-its:sldworksapivb6.chm::/sldworks~SketchSegment~SelectByMark.html).

## See Also

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html)
