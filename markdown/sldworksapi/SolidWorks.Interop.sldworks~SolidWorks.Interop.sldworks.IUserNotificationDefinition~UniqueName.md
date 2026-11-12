---
title: "UniqueName Property (IUserNotificationDefinition)"
project: "SOLIDWORKS API Help"
interface: "IUserNotificationDefinition"
member: "UniqueName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition~UniqueName.html"
---

# UniqueName Property (IUserNotificationDefinition)

Gets the ID of this user notification.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property UniqueName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IUserNotificationDefinition
Dim value As System.String

value = instance.UniqueName
```

### C#

```csharp
System.string UniqueName {get;}
```

### C++/CLI

```cpp
property System.String^ UniqueName {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Unique ID of this user notification

## VBA Syntax

See [UserNotificationDefinition::UniqueName](ms-its:sldworksapivb6.chm::/sldworks~UserNotificationDefinition~UniqueName.html).

## Remarks

It is the add-in's responsibility to ensure that the ID is unique by using, for example, a combination of add-in module name and unique notification identifier:

"MyAddInName+ID_MYNOTIFICATION1"

## See Also

[IUserNotificationDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition.html)
[IUserNotificationDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
