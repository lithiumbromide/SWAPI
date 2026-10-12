---
title: "SetMenuCmds Method (IEdmTaskProperties)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTaskProperties"
member: "SetMenuCmds"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~SetMenuCmds.html"
---

# SetMenuCmds Method (IEdmTaskProperties)

Adds the specified menu commands to File Explorer context menus.

## Syntax

### Visual Basic

```vb
Sub SetMenuCmds( _
   ByVal poCmds() As EdmTaskMenuCmd _
)
```

### C#

```csharp
void SetMenuCmds(
   EdmTaskMenuCmd[] poCmds
)
```

### C++/CLI

```cpp
void SetMenuCmds(
   array<EdmTaskMenuCmd>^ poCmds
)
```

### Parameters

- `poCmds`: Array of [EdmTaskMenuCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskMenuCmd.html) structures; one structure for each menu command to add to the context menus

## Examples

See the examples in [IEdmTaskProperties](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties.html).

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmTaskProperties Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties.html)
[IEdmTaskProperties Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties_members.html)
[IEdmTaskProperties::GetMenuCmds Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~GetMenuCmds.html)

## Availability

SOLIDWORKS PDM Professional 2010
