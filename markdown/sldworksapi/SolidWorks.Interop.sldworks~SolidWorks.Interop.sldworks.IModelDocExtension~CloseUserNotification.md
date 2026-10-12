---
title: "CloseUserNotification Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "CloseUserNotification"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CloseUserNotification.html"
---

# CloseUserNotification Method (IModelDocExtension)

Closes the specified user notification in this document's window.

## Syntax

### Visual Basic (Declaration)

```vb
Sub CloseUserNotification( _
   ByVal Handler As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Handler As System.Object

instance.CloseUserNotification(Handler)
```

### C#

```csharp
void CloseUserNotification(
   System.object Handler
)
```

### C++/CLI

```cpp
void CloseUserNotification(
   System.Object^ Handler
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Handler`: [IUserNotificationHandler](ms-its:swpublishedapi.chm::/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IUserNotificationHandler.html)

## VBA Syntax

See [ModelDocExtension::CloseUserNotification](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~CloseUserNotification.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
