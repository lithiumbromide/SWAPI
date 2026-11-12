---
title: "OnUserResponseA Method (MessageBarHandler)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "MessageBarHandler"
member: "OnUserResponseA"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.MessageBarHandler~OnUserResponseA.html"
---

# OnUserResponseA Method (MessageBarHandler)

Called by SOLIDWORKS when the user selects the first response control.

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnUserResponseA( _
   ByVal DoNotShowAgain As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As MessageBarHandler
Dim DoNotShowAgain As System.Boolean

instance.OnUserResponseA(DoNotShowAgain)
```

### C#

```csharp
void OnUserResponseA(
   System.bool DoNotShowAgain
)
```

### C++/CLI

```cpp
void OnUserResponseA(
   System.bool DoNotShowAgain
)
```

### Parameters

- `DoNotShowAgain`: True to check "Don't Show Again", false to not

## VBA Syntax

See [MessageBarHandler::OnUserResponseA](ms-its:swpublishedapivb6.chm::/swpublished~MessageBarHandler~OnUserResponseA.html).

## Examples

See the [IMessageBarHandler](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IMessageBarHandler.html) examples.

## See Also

[MessageBarHandler Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.MessageBarHandler.html)
[MessageBarHandler Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.MessageBarHandler_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
