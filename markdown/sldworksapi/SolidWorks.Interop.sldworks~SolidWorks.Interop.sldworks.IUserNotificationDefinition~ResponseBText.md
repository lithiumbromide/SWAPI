---
title: "ResponseBText Property (IUserNotificationDefinition)"
project: "SOLIDWORKS API Help"
interface: "IUserNotificationDefinition"
member: "ResponseBText"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition~ResponseBText.html"
---

# ResponseBText Property (IUserNotificationDefinition)

Gets or sets the text displayed on the second button or command link of this user notification.

## Syntax

### Visual Basic (Declaration)

```vb
Property ResponseBText As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IUserNotificationDefinition
Dim value As System.String

instance.ResponseBText = value

value = instance.ResponseBText
```

### C#

```csharp
System.string ResponseBText {get; set;}
```

### C++/CLI

```cpp
property System.String^ ResponseBText {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Text displayed on second user response control; default is an empty string

## VBA Syntax

See [UserNotificationDefinition::ResponseBText](ms-its:sldworksapivb6.chm::/sldworks~UserNotificationDefinition~ResponseBText.html).

## See Also

[IUserNotificationDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition.html)
[IUserNotificationDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
