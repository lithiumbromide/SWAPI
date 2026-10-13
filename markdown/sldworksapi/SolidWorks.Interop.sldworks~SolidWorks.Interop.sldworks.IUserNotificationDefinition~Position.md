---
title: "Position Property (IUserNotificationDefinition)"
project: "SOLIDWORKS API Help"
interface: "IUserNotificationDefinition"
member: "Position"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition~Position.html"
---

# Position Property (IUserNotificationDefinition)

Gets or sets the relative position of this user notification within the parent window.

## Syntax

### Visual Basic (Declaration)

```vb
Property Position As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IUserNotificationDefinition
Dim value As System.Integer

instance.Position = value

value = instance.Position
```

### C#

```csharp
System.int Position {get; set;}
```

### C++/CLI

```cpp
property System.int Position {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Position as defined by [swUserNotificationPosition_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserNotificationPosition_e.html)

## VBA Syntax

See [UserNotificationDefinition::Position](ms-its:sldworksapivb6.chm::/sldworks~UserNotificationDefinition~Position.html).

## Remarks

Default value of this property is swUserNotificationPosition_e.swUserNotificationPosition_Default.

## See Also

[IUserNotificationDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition.html)
[IUserNotificationDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
