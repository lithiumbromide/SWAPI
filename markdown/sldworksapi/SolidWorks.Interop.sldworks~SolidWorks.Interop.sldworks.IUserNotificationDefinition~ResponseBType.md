---
title: "ResponseBType Property (IUserNotificationDefinition)"
project: "SOLIDWORKS API Help"
interface: "IUserNotificationDefinition"
member: "ResponseBType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition~ResponseBType.html"
---

# ResponseBType Property (IUserNotificationDefinition)

Gets or sets the second response user control for this message bar.

## Syntax

### Visual Basic (Declaration)

```vb
Property ResponseBType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IUserNotificationDefinition
Dim value As System.Integer

instance.ResponseBType = value

value = instance.ResponseBType
```

### C#

```csharp
System.int ResponseBType {get; set;}
```

### C++/CLI

```cpp
property System.int ResponseBType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Second response user control as defined by [swUserNotificationResponseType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserNotificationResponseType_e.html)

## VBA Syntax

See [UserNotificationDefinition::ResponseBType](ms-its:sldworksapivb6.chm::/sldworks~UserNotificationDefinition~ResponseBType.html).

## See Also

[IUserNotificationDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition.html)
[IUserNotificationDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
