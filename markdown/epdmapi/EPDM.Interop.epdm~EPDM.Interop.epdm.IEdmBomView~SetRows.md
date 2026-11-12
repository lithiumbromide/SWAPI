---
title: "SetRows Method (IEdmBomView)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBomView"
member: "SetRows"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomView~SetRows.html"
---

# SetRows Method (IEdmBomView)

Adds new rows or reorders existing rows in this BOM.

## Syntax

### Visual Basic

```vb
Sub SetRows( _
   ByVal poRows() As System.Object _
)
```

### C#

```csharp
void SetRows(
   System.object[] poRows
)
```

### C++/CLI

```cpp
void SetRows(
   System.array<Object^>^ poRows
)
```

### Parameters

- `poRows`: Array of ordered [IEdmBomCell](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomCell.html) interfaces; one interface for each BOM row

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBomView Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomView.html)
[IEdmBomView Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomView_members.html)

## Availability

SOLIDWORKS PDM Professional 2009
