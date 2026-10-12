---
title: "OnUserResponseA Method (UserNotificationHandler)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "UserNotificationHandler"
member: "OnUserResponseA"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.UserNotificationHandler~OnUserResponseA.html"
---

# OnUserResponseA Method (UserNotificationHandler)

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
Dim instance As UserNotificationHandler
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

See [UserNotificationHandler::OnUserResponseA](ms-its:swpublishedapivb6.chm::/swpublished~UserNotificationHandler~OnUserResponseA.html).

## Examples

See the [IUserNotificationHandler](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IUserNotificationHandler.html) examples.

## See Also

[UserNotificationHandler Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.UserNotificationHandler.html)
[UserNotificationHandler Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.UserNotificationHandler_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
