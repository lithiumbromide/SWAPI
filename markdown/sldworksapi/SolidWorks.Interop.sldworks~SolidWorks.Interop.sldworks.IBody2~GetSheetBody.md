---
title: "GetSheetBody Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "GetSheetBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetSheetBody.html"
---

# GetSheetBody Method (IBody2)

Gets a sheet (surface) body in this body.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSheetBody( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
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

- `Index`: Index of sheet body

### Return Value

Sheet body corresponding to the index

## VBA Syntax

See [Body2::GetSheetBody](ms-its:sldworksapivb6.chm::/sldworks~Body2~GetSheetBody.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::IGetSheetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetSheetBody.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
