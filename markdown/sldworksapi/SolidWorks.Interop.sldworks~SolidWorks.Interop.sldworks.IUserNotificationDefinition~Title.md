---
title: "Title Property (IUserNotificationDefinition)"
project: "SOLIDWORKS API Help"
interface: "IUserNotificationDefinition"
member: "Title"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition~Title.html"
---

# Title Property (IUserNotificationDefinition)

Gets or sets the title of this user notification.

## Syntax

### Visual Basic (Declaration)

```vb
Property Title As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IUserNotificationDefinition
Dim value As System.String

instance.Title = value

value = instance.Title
```

### C#

```csharp
System.string Title {get; set;}
```

### C++/CLI

```cpp
property System.String^ Title {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Non-empty title string

## VBA Syntax

See [UserNotificationDefinition::Title](ms-its:sldworksapivb6.chm::/sldworks~UserNotificationDefinition~Title.html).

## Examples

See the [IUserNotificationHandler](ms-its:swpublishedapi.chm::/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IUserNotificationHandler.html) examples.

## Remarks

This property must be set.

## See Also

[IUserNotificationDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition.html)
[IUserNotificationDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
