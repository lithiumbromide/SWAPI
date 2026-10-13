---
title: "Select Method (ISketchHatch)"
project: "SOLIDWORKS API Help"
interface: "ISketchHatch"
member: "Select"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~Select.html"
---

# Select Method (ISketchHatch)

Obsolete. Superseded by [ISketchHatch::Select4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchHatch~Select4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function Select( _
   ByVal AppendFlag As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchHatch
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

See [SketchHatch::Select](ms-its:sldworksapivb6.chm::/sldworks~SketchHatch~Select.html).

## See Also

[ISketchHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.html)
[ISketchHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch_members.html)
