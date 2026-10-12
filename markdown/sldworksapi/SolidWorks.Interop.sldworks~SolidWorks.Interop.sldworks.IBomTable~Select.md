---
title: "Select Method (IBomTable)"
project: "SOLIDWORKS API Help"
interface: "IBomTable"
member: "Select"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~Select.html"
---

# Select Method (IBomTable)

Selects this BOM table and marks it.

## Syntax

### Visual Basic (Declaration)

```vb
Function Select( _
   ByVal Append As System.Boolean, _
   ByVal Mark As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTable
Dim Append As System.Boolean
Dim Mark As System.Integer
Dim value As System.Boolean

value = instance.Select(Append, Mark)
```

### C#

```csharp
System.bool Select(
   System.bool Append,
   System.int Mark
)
```

### C++/CLI

```cpp
System.bool Select(
   System.bool Append,
   System.int Mark
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Append`: True appends the selection list, false replaces the selection list
- `Mark`: Value you want to use as a mark

### Return Value

True if the BOM table is selected, false if not

## VBA Syntax

See [BomTable::Select](ms-its:sldworksapivb6.chm::/sldworks~BomTable~Select.html).

## Remarks

Before you use any of the IBomTable methods, activate the BOM table using [IBomTable::Attach3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTable~Attach3.html). After you finish getting BOM data, use [IBomTable::Detach](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTable~Detach.html) to deactivate the table.

## See Also

[IBomTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable.html)
[IBomTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable_members.html)
[IBomTable::DeSelect Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~DeSelect.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
