---
title: "GetRows Method (IEdmBomView)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBomView"
member: "GetRows"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomView~GetRows.html"
---

# GetRows Method (IEdmBomView)

Gets the row definitions for this BOM.

## Syntax

### Visual Basic

```vb
Sub GetRows( _
   ByRef ppoRows() As System.Object _
)
```

### C#

```csharp
void GetRows(
   out System.object[] ppoRows
)
```

### C++/CLI

```cpp
void GetRows(
   [Out] System.array<Object^>^ ppoRows
)
```

### Parameters

- `ppoRows`: Array of [IEdmBomCells](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomCell.html); one interface for each BOM row

## Examples

See the [IEdmBomView](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomView.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBomView Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomView.html)
[IEdmBomView Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomView_members.html)

## Availability

SOLIDWORKS PDM Professional 2009
