---
title: "GetColumnUseTitleAsPartNumber Method (IBomTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IBomTableAnnotation"
member: "GetColumnUseTitleAsPartNumber"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetColumnUseTitleAsPartNumber.html"
---

# GetColumnUseTitleAsPartNumber Method (IBomTableAnnotation)

Gets whether the document title is being used for the specified part-number column.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetColumnUseTitleAsPartNumber( _
   ByVal Index As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTableAnnotation
Dim Index As System.Integer
Dim value As System.Boolean

value = instance.GetColumnUseTitleAsPartNumber(Index)
```

### C#

```csharp
System.bool GetColumnUseTitleAsPartNumber(
   System.int Index
)
```

### C++/CLI

```cpp
System.bool GetColumnUseTitleAsPartNumber(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0-based number indicating the part-number column

### Return Value

True if document title is being used for the specified part-number column, false if not

## VBA Syntax

See [BomTableAnnotation::GetColumnUseTitleAsPartNumber](ms-its:sldworksapivb6.chm::/sldworks~BomTableAnnotation~GetColumnUseTitleAsPartNumber.html).

## See Also

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.html)
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.html)
[IBomTableAnnotation::SetColumnUseTitleAsPartNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~SetColumnUseTitleAsPartNumber.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12
