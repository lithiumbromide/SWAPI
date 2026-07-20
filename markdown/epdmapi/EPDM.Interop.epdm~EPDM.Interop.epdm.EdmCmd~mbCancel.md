---
title: "mbCancel Field"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmCmd"
member: "mbCancel"
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mbCancel.html"
---

# mbCancel Field

Command cancel status.

## Syntax

### Visual Basic

```vb
Public mbCancel As System.Short
```

### C#

```csharp
public System.short mbCancel
```

### C++/CLI

```cpp
public:
System.short mbCancel
```

### Field Value

True (1) to prevent a command from running using

[EdmCmd_PreXxxx hooks](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html)

, false (0) to disallow canceling the command

## See Also

[EdmCmd Structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd.html)

[EdmCmd Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd_members.html)
