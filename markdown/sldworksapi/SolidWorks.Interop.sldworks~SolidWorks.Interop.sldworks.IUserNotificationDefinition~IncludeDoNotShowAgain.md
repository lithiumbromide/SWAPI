---
title: "IncludeDoNotShowAgain Property (IUserNotificationDefinition)"
project: "SOLIDWORKS API Help"
interface: "IUserNotificationDefinition"
member: "IncludeDoNotShowAgain"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition~IncludeDoNotShowAgain.html"
---

# IncludeDoNotShowAgain Property (IUserNotificationDefinition)

Gets or sets whether to display the "Do not show again" check box for this user notification.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeDoNotShowAgain As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IUserNotificationDefinition
Dim value As System.Boolean

instance.IncludeDoNotShowAgain = value

value = instance.IncludeDoNotShowAgain
```

### C#

```csharp
System.bool IncludeDoNotShowAgain {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeDoNotShowAgain {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True (default) to display the check box, false to not.

## VBA Syntax

See [UserNotificationDefinition::IncludeDoNotShowAgain](ms-its:sldworksapivb6.chm::/sldworks~UserNotificationDefinition~IncludeDoNotShowAgain.html).

## See Also

[IUserNotificationDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition.html)
[IUserNotificationDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
