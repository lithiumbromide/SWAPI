---
title: "GetSheetBody Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "GetSheetBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~GetSheetBody.html"
---

# GetSheetBody Method (IBody)

Obsolete. Superseded by [IBody2::GetSheetBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~GetSheetBody.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSheetBody( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetSheetBody(Index)
```

### C#

```csharp
System.object GetSheetBody(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetSheetBody(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`:

## VBA Syntax

See [Body::GetSheetBody](ms-its:sldworksapivb6.chm::/sldworks~Body~GetSheetBody.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
