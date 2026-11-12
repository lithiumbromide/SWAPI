---
title: "EditVariables Method (IEdmVariableMgr5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVariableMgr5"
member: "EditVariables"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableMgr5~EditVariables.html"
---

# EditVariables Method (IEdmVariableMgr5)

Displays the Edit Variables dialog box.

## Syntax

### Visual Basic

```vb
Function EditVariables( _
   ByVal hParentWnd As System.Integer _
) As System.Boolean
```

### C#

```csharp
System.bool EditVariables(
   System.int hParentWnd
)
```

### C++/CLI

```cpp
System.bool EditVariables(
   System.int hParentWnd
)
```

### Parameters

- `hParentWnd`: Parent window handle

### Return Value

True if one or more variables are updated; false if not

## Examples

[Add Card Variables to Vault (VB.NET)](Add_Variables_to_Vault_Example_VBNET.htm)
[Add Card Variables to Vault (C#)](Add_Variables_to_Vault_Example_CSharp.htm)

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_PERMISSION_DENIED: The user lacks permission to edit variables.

## See Also

[IEdmVariableMgr5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableMgr5.html)
[IEdmVariableMgr5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableMgr5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
