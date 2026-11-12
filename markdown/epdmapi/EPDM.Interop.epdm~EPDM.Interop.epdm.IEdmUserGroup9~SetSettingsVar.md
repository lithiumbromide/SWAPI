---
title: "SetSettingsVar Method (IEdmUserGroup9)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUserGroup9"
member: "SetSettingsVar"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup9~SetSettingsVar.html"
---

# SetSettingsVar Method (IEdmUserGroup9)

Sets the specified user group setting.

## Syntax

### Visual Basic

```vb
Sub SetSettingsVar( _
   ByVal eVar As EdmGroupSetting, _
   ByVal pbsVal As System.String _
)
```

### C#

```csharp
void SetSettingsVar(
   EdmGroupSetting eVar,
   System.string pbsVal
)
```

### C++/CLI

```cpp
void SetSettingsVar(
   EdmGroupSetting eVar,
   System.String^ pbsVal
)
```

### Parameters

- `eVar`: User group setting as defined by [EdmGroupSetting](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupSetting.html)
- `pbsVal`: Value of eVar

## Examples

See the [IEdmUser11::SetSettingsVar](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser11~SetSettingsVar.html) example.

## See Also

[IEdmUserGroup9 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup9.html)
[IEdmUserGroup9 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup9_members.html)

## Availability

SOLIDWORKS PDM Professional 2022
