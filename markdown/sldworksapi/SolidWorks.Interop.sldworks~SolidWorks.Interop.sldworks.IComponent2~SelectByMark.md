---
title: "SelectByMark Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "SelectByMark"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SelectByMark.html"
---

# SelectByMark Method (IComponent2)

Obsolete. Superseded by [IComponent2::Select3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~Select3.html).

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
Dim instance As IComponent2
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

See [Component2::SelectByMark](ms-its:sldworksapivb6.chm::/sldworks~Component2~SelectByMark.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
