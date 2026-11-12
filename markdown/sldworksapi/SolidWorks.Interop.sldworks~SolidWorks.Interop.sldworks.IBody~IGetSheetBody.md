---
title: "IGetSheetBody Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "IGetSheetBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IGetSheetBody.html"
---

# IGetSheetBody Method (IBody)

Obsolete. Superseded by [IBody2::IGetSheetBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IGetSheetBody.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSheetBody( _
   ByVal Index As System.Integer _
) As Body
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim Index As System.Integer
Dim value As Body

value = instance.IGetSheetBody(Index)
```

### C#

```csharp
Body IGetSheetBody(
   System.int Index
)
```

### C++/CLI

```cpp
Body^ IGetSheetBody(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`:

## VBA Syntax

See [Body::IGetSheetBody](ms-its:sldworksapivb6.chm::/sldworks~Body~IGetSheetBody.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
