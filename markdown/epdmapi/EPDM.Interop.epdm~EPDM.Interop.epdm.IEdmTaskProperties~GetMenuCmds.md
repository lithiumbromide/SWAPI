---
title: "GetMenuCmds Method (IEdmTaskProperties)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTaskProperties"
member: "GetMenuCmds"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~GetMenuCmds.html"
---

# GetMenuCmds Method (IEdmTaskProperties)

Gets the menu commands set with [IEdmTaskProperties::SetMenuCmds](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~SetMenuCmds.html).

## Syntax

### Visual Basic

```vb
Sub GetMenuCmds( _
   ByRef ppoCmds() As EdmTaskMenuCmd _
)
```

### C#

```csharp
void GetMenuCmds(
   out EdmTaskMenuCmd[] ppoCmds
)
```

### C++/CLI

```cpp
void GetMenuCmds(
   [Out] array<EdmTaskMenuCmd>^ ppoCmds
)
```

### Parameters

- `ppoCmds`: Array of [EdmTaskMenuCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskMenuCmd.html) structures; one structure for each menu command

## Remarks

The menu commands display in a File Explorer context menu.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmTaskProperties Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties.html)
[IEdmTaskProperties Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties_members.html)
[Task Add-in Sample](TaskSample.htm)

## Availability

SOLIDWORKS PDM Professional 2010
