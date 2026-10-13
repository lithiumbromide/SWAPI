---
title: "Select3 Method (ISketchHatch)"
project: "SOLIDWORKS API Help"
interface: "ISketchHatch"
member: "Select3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~Select3.html"
---

# Select3 Method (ISketchHatch)

Obsolete. Superseded by [ISketchHatch::Select4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchHatch~Select4.html).

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
Dim instance As ISketchHatch
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

See [SketchHatch::Select3](ms-its:sldworksapivb6.chm::/sldworks~SketchHatch~Select3.html).

## See Also

[ISketchHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.html)
[ISketchHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch_members.html)
