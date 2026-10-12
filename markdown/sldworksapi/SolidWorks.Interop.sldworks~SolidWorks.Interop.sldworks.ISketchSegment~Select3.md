---
title: "Select3 Method (ISketchSegment)"
project: "SOLIDWORKS API Help"
interface: "ISketchSegment"
member: "Select3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Select3.html"
---

# Select3 Method (ISketchSegment)

Obsolete. Superseded by [ISketchSegment::Select4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment~Select4.html).

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
Dim instance As ISketchSegment
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

See [SketchSegment::Select3](ms-its:sldworksapivb6.chm::/sldworks~SketchSegment~Select3.html).

## See Also

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html)
