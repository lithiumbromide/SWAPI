---
title: "Select3 Method (ISketchPoint)"
project: "SOLIDWORKS API Help"
interface: "ISketchPoint"
member: "Select3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~Select3.html"
---

# Select3 Method (ISketchPoint)

Obsolete. Superseded by [ISketchPoint::Select4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint~Select4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function Select3( _
   ByVal Append As System.Boolean, _
   ByVal Mark As System.Integer, _
   ByVal Callout As Callout _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPoint
Dim Append As System.Boolean
Dim Mark As System.Integer
Dim Callout As Callout
Dim value As System.Boolean

value = instance.Select3(Append, Mark, Callout)
```

### C#

```csharp
System.bool Select3(
   System.bool Append,
   System.int Mark,
   Callout Callout
)
```

### C++/CLI

```cpp
System.bool Select3(
   System.bool Append,
   System.int Mark,
   Callout^ Callout
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Append`:
- `Mark`:
- `Callout`:

## VBA Syntax

See [SketchPoint::Select3](ms-its:sldworksapivb6.chm::/sldworks~SketchPoint~Select3.html).

## See Also

[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)
[ISketchPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint_members.html)
