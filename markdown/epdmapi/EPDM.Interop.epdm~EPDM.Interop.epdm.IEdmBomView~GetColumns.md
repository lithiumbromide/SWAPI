---
title: "GetColumns Method (IEdmBomView)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBomView"
member: "GetColumns"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomView~GetColumns.html"
---

# GetColumns Method (IEdmBomView)

Gets the column definitions for this BOM.

## Syntax

### Visual Basic

```vb
Sub GetColumns( _
   ByRef ppoColumns() As EdmBomColumn _
)
```

### C#

```csharp
void GetColumns(
   out EdmBomColumn[] ppoColumns
)
```

### C++/CLI

```cpp
void GetColumns(
   [Out] array<EdmBomColumn>^ ppoColumns
)
```

### Parameters

- `ppoColumns`: Array of [EdmBomColumn](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomColumn.html) structures; one structure for each BOM column

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
