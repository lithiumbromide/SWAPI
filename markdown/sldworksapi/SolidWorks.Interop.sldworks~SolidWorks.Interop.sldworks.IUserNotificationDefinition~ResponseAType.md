---
title: "ResponseAType Property (IUserNotificationDefinition)"
project: "SOLIDWORKS API Help"
interface: "IUserNotificationDefinition"
member: "ResponseAType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition~ResponseAType.html"
---

# ResponseAType Property (IUserNotificationDefinition)

Gets or sets the first response user control for this user notification.

## Syntax

### Visual Basic (Declaration)

```vb
Property ResponseAType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IUserNotificationDefinition
Dim value As System.Integer

instance.ResponseAType = value

value = instance.ResponseAType
```

### C#

```csharp
System.int ResponseAType {get; set;}
```

### C++/CLI

```cpp
property System.int ResponseAType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

First response user control as defined by [swUserNotificationResponseType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserNotificationResponseType_e.html)

## VBA Syntax

See [UserNotificationDefinition::ResponseAType](ms-its:sldworksapivb6.chm::/sldworks~UserNotificationDefinition~ResponseAType.html).

## Examples

See the [IUserNotificationHandler](ms-its:swpublishedapi.chm::/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IUserNotificationHandler.html) examples.

## See Also

[IUserNotificationDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition.html)
[IUserNotificationDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
