---
title: "Select Method (ISketchSegment)"
project: "SOLIDWORKS API Help"
interface: "ISketchSegment"
member: "Select"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Select.html"
---

# Select Method (ISketchSegment)

Obsolete. Superseded by [ISketchSegment::Select4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment~Select4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function Select( _
   ByVal AppendFlag As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSegment
Dim AppendFlag As System.Boolean
Dim value As System.Boolean

value = instance.Select(AppendFlag)
```

### C#

```csharp
System.bool Select(
   System.bool AppendFlag
)
```

### C++/CLI

```cpp
System.bool Select(
   System.bool AppendFlag
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AppendFlag`:

## VBA Syntax

See [SketchSegment::Select](ms-its:sldworksapivb6.chm::/sldworks~SketchSegment~Select.html).

## See Also

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html)
