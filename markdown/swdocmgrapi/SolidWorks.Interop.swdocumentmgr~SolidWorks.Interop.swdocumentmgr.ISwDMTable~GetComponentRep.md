---
title: "GetComponentRep Method (ISwDMTable)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMTable"
member: "GetComponentRep"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetComponentRep.html"
---

# GetComponentRep Method (ISwDMTable)

Gets the component representation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponentRep( _
   ByVal RowIndex As System.Integer, _
   ByRef ComponentRep As System.String _
) As SwDmTableError
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMTable
Dim RowIndex As System.Integer
Dim ComponentRep As System.String
Dim value As SwDmTableError

value = instance.GetComponentRep(RowIndex, ComponentRep)
```

### C#

```csharp
SwDmTableError GetComponentRep(
   System.int RowIndex,
   out System.string ComponentRep
)
```

### C++/CLI

```cpp
SwDmTableError GetComponentRep(
   System.int RowIndex,
   [Out] System.String^ ComponentRep
)
```

### Parameters

- `RowIndex`: Row number for the component representation
- `ComponentRep`: Component representation

### Return Value

Error as defined in [SwDmTableError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmTableError.html)

## VBA Syntax

See [SwDMTable::GetComponentRep](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMTable~GetComponentRep.html).

## Remarks

Before calling this method, call [ISwDMTable::GetRowCount](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMTable~GetRowCount.html) to determine the index of the row for the component representation.

## See Also

[ISwDMTable Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable.html)
[ISwDMTable Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable_members.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
