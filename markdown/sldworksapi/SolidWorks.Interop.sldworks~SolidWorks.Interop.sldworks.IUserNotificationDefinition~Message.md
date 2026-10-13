---
title: "Message Property (IUserNotificationDefinition)"
project: "SOLIDWORKS API Help"
interface: "IUserNotificationDefinition"
member: "Message"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition~Message.html"
---

# Message Property (IUserNotificationDefinition)

Gets or sets the message displayed on this message bar.

## Syntax

### Visual Basic (Declaration)

```vb
Property Message As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IUserNotificationDefinition
Dim value As System.String

instance.Message = value

value = instance.Message
```

### C#

```csharp
System.string Message {get; set;}
```

### C++/CLI

```cpp
property System.String^ Message {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Non-empty message string

## VBA Syntax

See [UserNotificationDefinition::Message](ms-its:sldworksapivb6.chm::/sldworks~UserNotificationDefinition~Message.html).

## Examples

See the [IUserNotificationHandler](ms-its:swpublishedapi.chm::/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IUserNotificationHandler.html) examples.

## Remarks

This property must be set.

## See Also

[IUserNotificationDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition.html)
[IUserNotificationDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
