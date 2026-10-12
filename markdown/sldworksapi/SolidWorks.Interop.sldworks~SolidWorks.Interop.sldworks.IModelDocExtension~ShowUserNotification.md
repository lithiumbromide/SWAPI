---
title: "ShowUserNotification Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "ShowUserNotification"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ShowUserNotification.html"
---

# ShowUserNotification Method (IModelDocExtension)

Displays the specified user notfication for this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function ShowUserNotification( _
   ByVal Definition As System.Object, _
   ByVal Handler As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Definition As System.Object
Dim Handler As System.Object
Dim value As System.Integer

value = instance.ShowUserNotification(Definition, Handler)
```

### C#

```csharp
System.int ShowUserNotification(
   System.object Definition,
   System.object Handler
)
```

### C++/CLI

```cpp
System.int ShowUserNotification(
   System.Object^ Definition,
   System.Object^ Handler
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Definition`: [IUserNotificationDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition.html)
- `Handler`: [IUserNotificationHandler](ms-its:swpublishedapi.chm::/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IUserNotificationHandler.html)

### Return Value

Result code as defined by [swShowNotificationResult_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swShowNotificationResult_e.html)

## VBA Syntax

See [ModelDocExtension::ShowUserNotification](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~ShowUserNotification.html).

## Examples

See the [IUserNotificationHandler](ms-its:swpublishedapi.chm::/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IUserNotificationHandler.html) examples.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
