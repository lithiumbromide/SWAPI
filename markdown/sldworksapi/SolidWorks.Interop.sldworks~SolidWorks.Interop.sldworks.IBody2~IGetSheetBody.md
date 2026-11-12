---
title: "IGetSheetBody Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IGetSheetBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetSheetBody.html"
---

# IGetSheetBody Method (IBody2)

Gets a sheet (surface) body in this body.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSheetBody( _
   ByVal Index As System.Integer _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Index As System.Integer
Dim value As Body2

value = instance.IGetSheetBody(Index)
```

### C#

```csharp
Body2 IGetSheetBody(
   System.int Index
)
```

### C++/CLI

```cpp
Body2^ IGetSheetBody(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of sheet body

### Return Value

Pointer to the sheet [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) corresponding to the index

## VBA Syntax

See [Body2::IGetSheetBody](ms-its:sldworksapivb6.chm::/sldworks~Body2~IGetSheetBody.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::GetSheetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetSheetBody.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
