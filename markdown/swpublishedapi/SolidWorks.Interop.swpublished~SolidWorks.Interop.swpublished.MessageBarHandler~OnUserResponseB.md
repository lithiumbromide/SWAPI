---
title: "OnUserResponseB Method (MessageBarHandler)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "MessageBarHandler"
member: "OnUserResponseB"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.MessageBarHandler~OnUserResponseB.html"
---

# OnUserResponseB Method (MessageBarHandler)

Called by SOLIDWORKS when the user selects the second response control.

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnUserResponseB( _
   ByVal DoNotShowAgain As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As MessageBarHandler
Dim DoNotShowAgain As System.Boolean

instance.OnUserResponseB(DoNotShowAgain)
```

### C#

```csharp
void OnUserResponseB(
   System.bool DoNotShowAgain
)
```

### C++/CLI

```cpp
void OnUserResponseB(
   System.bool DoNotShowAgain
)
```

### Parameters

- `DoNotShowAgain`: True to check "Don't Show Again", false to not

## VBA Syntax

See [MessageBarHandler::OnUserResponseB](ms-its:swpublishedapivb6.chm::/swpublished~MessageBarHandler~OnUserResponseB.html).

## Examples

See the [IMessageBarHandler](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IMessageBarHandler.html) examples.

## See Also

[MessageBarHandler Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.MessageBarHandler.html)
[MessageBarHandler Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.MessageBarHandler_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
