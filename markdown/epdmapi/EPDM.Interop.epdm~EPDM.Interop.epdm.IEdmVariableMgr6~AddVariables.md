---
title: "AddVariables Method (IEdmVariableMgr6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVariableMgr6"
member: "AddVariables"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableMgr6~AddVariables.html"
---

# AddVariables Method (IEdmVariableMgr6)

Adds the specified variables to the vault.

## Syntax

### Visual Basic

```vb
Sub AddVariables( _
   ByRef ppoVariables() As EdmVariableData _
)
```

### C#

```csharp
void AddVariables(
   out EdmVariableData[] ppoVariables
)
```

### C++/CLI

```cpp
void AddVariables(
   [Out] array<EdmVariableData>^ ppoVariables
)
```

### Parameters

- `ppoVariables`: Array of [EdmVariableData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmVariableData.html) structures; one structure for each variable (see **Remarks**)

## Examples

See the [IEdmVariableMgr6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableMgr6.html) examples.

## Remarks

In the ppoVariables structure, set mlVariableID to 0 before calling this method. The ID of the new variable is returned in mlVariableID.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmVariableMgr6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableMgr6.html)
[IEdmVariableMgr6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableMgr6_members.html)

## Availability

SOLIDWORKS PDM Professional 2007
