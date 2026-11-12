---
title: "IUserNotificationDefinition Interface"
project: "SOLIDWORKS API Help"
interface: "IUserNotificationDefinition"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition.html"
---

# IUserNotificationDefinition Interface

Allows access to a user notification of an add-in.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IUserNotificationDefinition
```

### Visual Basic (Usage)

```vb
Dim instance As IUserNotificationDefinition
```

### C#

```csharp
public interface IUserNotificationDefinition
```

### C++/CLI

```cpp
public interface class IUserNotificationDefinition
```

## VBA Syntax

See [UserNotificationDefinition](ms-its:sldworksapivb6.chm::/sldworks~UserNotificationDefinition.html).

## Examples

See the [IUserNotificationHandler](ms-its:swpublishedapi.chm::/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IUserNotificationHandler.html) examples.

## Remarks

A user notification is an add-in dialog that:

- Allows an add-in to display a unique message to SOLIDWORKS Design users.
- Is modeless.
- May appear within the context of a document open in its own frame or within SOLIDWORKS itself.
- Replaces any previously displayed user notification.
- Requires an IUserNotificationHandler to handle user notification events.

## Accessors

[ISldWorks::DefineUserNotification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DefineUserNotification.html)

## Access Diagram

[UserNotificationDefinition](SWObjectModel.pdf#UserNotificationDefinition)

## See Also

[IUserNotificationDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IMessageBarDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition.html)
