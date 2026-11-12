---
title: "OnCmd Method (IEdmAddIn5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmAddIn5"
member: "OnCmd"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html"
---

# OnCmd Method (IEdmAddIn5)

Called by SOLIDWORKS PDM Professional whenever one of the menu commands or hooks registered in [IEdmAddIn5::GetAddInInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~GetAddInInfo.html) is executed.

## Syntax

### Visual Basic

```vb
Sub OnCmd( _
   ByRef poCmd As EdmCmd, _
   ByRef ppoData() As EdmCmdData _
)
```

### C#

```csharp
void OnCmd(
   out EdmCmd poCmd,
   out EdmCmdData[] ppoData
)
```

### C++/CLI

```cpp
void OnCmd(
   [Out] EdmCmd poCmd,
   [Out] array<EdmCmdData>^ ppoData
)
```

### Parameters

- `poCmd`: [EdmCmd structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd.html); command information common to all affected files and folders
- `ppoData`: Array of [EdmCmdData structures](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdData.html), one for each affected file or folder

## Examples

See the [IEdmAddin5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5.html) examples.

## Remarks

See the [IEdmAddIn5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5.html) topic for more information.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmAddIn5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5.html)
[IEdmAddIn5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5_members.html)

## Availability

Version 5.2 of SOLIDWORKS PDM Professional
