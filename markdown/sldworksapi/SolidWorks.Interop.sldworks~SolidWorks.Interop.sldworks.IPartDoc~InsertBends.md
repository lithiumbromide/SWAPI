---
title: "InsertBends Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "InsertBends"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertBends.html"
---

# InsertBends Method (IPartDoc)

Obsolete. Superseded by [IPartDoc::InsertBends2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~InsertBends2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertBends( _
   ByVal Radius As System.Double, _
   ByVal UseBendTable As System.String, _
   ByVal UseKfactor As System.Double, _
   ByVal UseBendAllowance As System.Double, _
   ByVal UseAutoRelief As System.Boolean, _
   ByVal OffsetRatio As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim Radius As System.Double
Dim UseBendTable As System.String
Dim UseKfactor As System.Double
Dim UseBendAllowance As System.Double
Dim UseAutoRelief As System.Boolean
Dim OffsetRatio As System.Double
Dim value As System.Boolean

value = instance.InsertBends(Radius, UseBendTable, UseKfactor, UseBendAllowance, UseAutoRelief, OffsetRatio)
```

### C#

```csharp
System.bool InsertBends(
   System.double Radius,
   System.string UseBendTable,
   System.double UseKfactor,
   System.double UseBendAllowance,
   System.bool UseAutoRelief,
   System.double OffsetRatio
)
```

### C++/CLI

```cpp
System.bool InsertBends(
   System.double Radius,
   System.String^ UseBendTable,
   System.double UseKfactor,
   System.double UseBendAllowance,
   System.bool UseAutoRelief,
   System.double OffsetRatio
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Radius`:
- `UseBendTable`:
- `UseKfactor`:
- `UseBendAllowance`:
- `UseAutoRelief`:
- `OffsetRatio`:

## VBA Syntax

See [PartDoc::InsertBends](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~InsertBends.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
