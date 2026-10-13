---
title: "meCmdType Field"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmCmd"
member: "meCmdType"
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~meCmdType.html"
---

# meCmdType Field

Type of command.

## Syntax

### Visual Basic

```vb
Public meCmdType As EdmCmdType
```

### C#

```csharp
public EdmCmdType meCmdType
```

### C++/CLI

```cpp
public:
EdmCmdType meCmdType
```

### Field Value

Type of command as defined in [EdmCmdType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html)

## Remarks

To use this command in your add-in, you must subscribe to it using [IEdmCmdMgr5::AddCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr5~AddCmd.html) and [IEdmCmdMgr5::AddHook](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr5~AddHook.html).

## See Also

[EdmCmd Structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd.html)
[EdmCmd Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd_members.html)
