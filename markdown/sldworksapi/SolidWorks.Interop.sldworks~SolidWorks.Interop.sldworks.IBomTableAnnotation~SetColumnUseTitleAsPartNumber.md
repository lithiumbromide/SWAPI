---
title: "SetColumnUseTitleAsPartNumber Method (IBomTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IBomTableAnnotation"
member: "SetColumnUseTitleAsPartNumber"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~SetColumnUseTitleAsPartNumber.html"
---

# SetColumnUseTitleAsPartNumber Method (IBomTableAnnotation)

Sets whether to use the document title for the specified part-number column.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetColumnUseTitleAsPartNumber( _
   ByVal Index As System.Integer, _
   ByVal UseTitle As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTableAnnotation
Dim Index As System.Integer
Dim UseTitle As System.Boolean
Dim value As System.Boolean

value = instance.SetColumnUseTitleAsPartNumber(Index, UseTitle)
```

### C#

```csharp
System.bool SetColumnUseTitleAsPartNumber(
   System.int Index,
   System.bool UseTitle
)
```

### C++/CLI

```cpp
System.bool SetColumnUseTitleAsPartNumber(
   System.int Index,
   System.bool UseTitle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0-based index indicating the part-number column
- `UseTitle`: True to use the document title for the specified part-number column, false to not

### Return Value

True to use the document title for the specified part-number column, false if you specify an invalid column number or the specified column is not the part-number column

## VBA Syntax

See [BomTableAnnotation::SetColumnUseTitleAsPartNumber](ms-its:sldworksapivb6.chm::/sldworks~BomTableAnnotation~SetColumnUseTitleAsPartNumber.html).

## See Also

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.html)
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.html)
[IBomTableAnnotation::GetColumnCustomProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetColumnCustomProperty.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12
