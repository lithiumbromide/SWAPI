---
title: "OnUserResponseB Method (IUserNotificationHandler)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IUserNotificationHandler"
member: "OnUserResponseB"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IUserNotificationHandler~OnUserResponseB.html"
---

# OnUserResponseB Method (IUserNotificationHandler)

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
Dim instance As IUserNotificationHandler
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

See [UserNotificationHandler::OnUserResponseB](ms-its:swpublishedapivb6.chm::/swpublished~UserNotificationHandler~OnUserResponseB.html).

## Examples

See the [IUserNotificationHandler](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IUserNotificationHandler.html) examples.

## See Also

[IUserNotificationHandler Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IUserNotificationHandler.html)
[IUserNotificationHandler Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IUserNotificationHandler_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
