---
title: "ResponseAText Property (IUserNotificationDefinition)"
project: "SOLIDWORKS API Help"
interface: "IUserNotificationDefinition"
member: "ResponseAText"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition~ResponseAText.html"
---

# ResponseAText Property (IUserNotificationDefinition)

Gets or sets the text displayed on the first button or command link of this user notification.

## Syntax

### Visual Basic (Declaration)

```vb
Property ResponseAText As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IUserNotificationDefinition
Dim value As System.String

instance.ResponseAText = value

value = instance.ResponseAText
```

### C#

```csharp
System.string ResponseAText {get; set;}
```

### C++/CLI

```cpp
property System.String^ ResponseAText {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Text displayed on first user response control; default is an empty string

## VBA Syntax

See [UserNotificationDefinition::ResponseAText](ms-its:sldworksapivb6.chm::/sldworks~UserNotificationDefinition~ResponseAText.html).

## Examples

See the [IUserNotificationHandler](ms-its:swpublishedapi.chm::/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IUserNotificationHandler.html) examples.

## See Also

[IUserNotificationDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition.html)
[IUserNotificationDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
