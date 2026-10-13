---
title: "mlRecipientID Field"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmRevComponent2"
member: "mlRecipientID"
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevComponent2~mlRecipientID.html"
---

# mlRecipientID Field

ID of the user or group notified by mail when the end of a revision number list is reached.

## Syntax

### Visual Basic

```vb
Public mlRecipientID As System.Integer
```

### C#

```csharp
public System.int mlRecipientID
```

### C++/CLI

```cpp
public:
System.int mlRecipientID
```

## Remarks

This member is only valid if [mlEdmRevComponentFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevComponent2~mlEdmRevComponentFlags.html) contains Edmrcf_EndOfListSendMail.

## See Also

[EdmRevComponent2 Structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevComponent2.html)
[EdmRevComponent2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevComponent2_members.html)
