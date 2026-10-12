---
title: "Severity Property (IUserNotificationDefinition)"
project: "SOLIDWORKS API Help"
interface: "IUserNotificationDefinition"
member: "Severity"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition~Severity.html"
---

# Severity Property (IUserNotificationDefinition)

Gets or sets the severity level of this user notification.

## Syntax

### Visual Basic (Declaration)

```vb
Property Severity As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IUserNotificationDefinition
Dim value As System.Integer

instance.Severity = value

value = instance.Severity
```

### C#

```csharp
System.int Severity {get; set;}
```

### C++/CLI

```cpp
property System.int Severity {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Severity level as defined by [swUserNotificationSeverity_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserNotificationSeverity_e.html)

## VBA Syntax

See [UserNotificationDefinition::Severity](ms-its:sldworksapivb6.chm::/sldworks~UserNotificationDefinition~Severity.html).

## Examples

See the [IUserNotificationHandler](ms-its:swpublishedapi.chm::/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IUserNotificationHandler.html) examples.

## See Also

[IUserNotificationDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition.html)
[IUserNotificationDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
