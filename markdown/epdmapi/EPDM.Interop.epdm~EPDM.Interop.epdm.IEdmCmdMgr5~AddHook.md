---
title: "AddHook Method (IEdmCmdMgr5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCmdMgr5"
member: "AddHook"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr5~AddHook.html"
---

# AddHook Method (IEdmCmdMgr5)

Adds a hook that makes SOLIDWORKS PDM Professional call this add-in's implementation of [IEdmAddIn5::OnCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html) whenever the specified events occur.

## Syntax

### Visual Basic

```vb
Sub AddHook( _
   ByVal eCmdType As EdmCmdType, _
   Optional ByVal poReserved As System.Object _
)
```

### C#

```csharp
void AddHook(
   EdmCmdType eCmdType,
   System.object poReserved
)
```

### C++/CLI

```cpp
void AddHook(
   EdmCmdType eCmdType,
   System.Object^ poReserved
)
```

### Parameters

- `eCmdType`: Types of event that trigger IEdmAddIn5::OnCmd as defined in [EdmCmdType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html)
- `poReserved`: Null; reserved for future use

## Examples

See [IEdmCmdMgr5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr5.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmCmdMgr5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr5.html)
[IEdmCmdMgr5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
