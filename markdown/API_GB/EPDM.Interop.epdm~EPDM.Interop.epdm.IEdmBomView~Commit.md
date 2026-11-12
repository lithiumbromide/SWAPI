---
title: "Commit Method (IEdmBomView)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBomView"
member: "Commit"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomView~Commit.html"
---

# Commit Method (IEdmBomView)

Saves the BOM content.

## Syntax

### Visual Basic

```vb
Function Commit( _
   ByVal bsSaveAsBomName As System.String, _
   ByRef pbsErrorMessage As System.String, _
   ByRef plFocusNodeID As System.Integer _
) As System.Integer
```

### C#

```csharp
System.int Commit(
   System.string bsSaveAsBomName,
   out System.string pbsErrorMessage,
   out System.int plFocusNodeID
)
```

### C++/CLI

```cpp
System.int Commit(
   System.String^ bsSaveAsBomName,
   [Out] System.String^ pbsErrorMessage,
   [Out] System.int plFocusNodeID
)
```

### Parameters

- `bsSaveAsBomName`: Name of new BOM in which to save the BOM content; empty string to save changes to an existing BOM
- `pbsErrorMessage`: Error message
- `plFocusNodeID`: ID of node to which to set focus

### Return Value

[Return codes](ReturnCodes.htm)

## Examples

[Add Row to Bill of Materials (VB.NET)](Add_Row_to_Bill_of_Materials_Example_VBNET.htm)
[Add Row to Bill of Materials (C#)](Add_Row_to_Bill_of_Materials_Example_CSharp.htm)

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBomView Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomView.html)
[IEdmBomView Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomView_members.html)

## Availability

SOLIDWORKS PDM Professional 2009
