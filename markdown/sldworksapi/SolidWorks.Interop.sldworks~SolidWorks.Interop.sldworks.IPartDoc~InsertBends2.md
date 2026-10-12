---
title: "InsertBends2 Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "InsertBends2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertBends2.html"
---

# InsertBends2 Method (IPartDoc)

Creates bends in a thin-feature part.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertBends2( _
   ByVal Radius As System.Double, _
   ByVal UseBendTable As System.String, _
   ByVal UseKfactor As System.Double, _
   ByVal UseBendAllowance As System.Double, _
   ByVal UseAutoRelief As System.Boolean, _
   ByVal OffsetRatio As System.Double, _
   ByVal DoFlatten As System.Boolean _
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
Dim DoFlatten As System.Boolean
Dim value As System.Boolean

value = instance.InsertBends2(Radius, UseBendTable, UseKfactor, UseBendAllowance, UseAutoRelief, OffsetRatio, DoFlatten)
```

### C#

```csharp
System.bool InsertBends2(
   System.double Radius,
   System.string UseBendTable,
   System.double UseKfactor,
   System.double UseBendAllowance,
   System.bool UseAutoRelief,
   System.double OffsetRatio,
   System.bool DoFlatten
)
```

### C++/CLI

```cpp
System.bool InsertBends2(
   System.double Radius,
   System.String^ UseBendTable,
   System.double UseKfactor,
   System.double UseBendAllowance,
   System.bool UseAutoRelief,
   System.double OffsetRatio,
   System.bool DoFlatten
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Radius`: Radius of the bends
- `UseBendTable`: Bend table name (.btl file)
- `UseKfactor`: K-Factor ratio or -1 if not used
- `UseBendAllowance`: Bend allowance value or -1 if not used
- `UseAutoRelief`: True if auto-relief cuts are to be added, false if not
- `OffsetRatio`: Distance relief cut extends beyond bend (see **Remarks)**
- `DoFlatten`: True to create these three features: Sheet-Metal, Flatten-Bends, and Process-Bends, false to create only the Sheet-Metal feature

### Return Value

True if successful, false if not

## VBA Syntax

See [PartDoc::InsertBends2](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~InsertBends2.html).

## Remarks

The offsetRatio argument is from 0.05 to 2.0. Any other value fails to create the
bend features.

When True is passed to doFlatten, all three Sheet-Metal features are created.

For more information on these arguments, see SOLIDWORKS Help.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
