---
title: "ShowUserNotification Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "ShowUserNotification"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowUserNotification.html"
---

# ShowUserNotification Method (ISldWorks)

Shows the specified user notification for a SOLIDWORKS add-in.

## Syntax

### Visual Basic (Declaration)

```vb
Function ShowUserNotification( _
   ByVal Definition As System.Object, _
   ByVal Handler As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Definition As System.Object
Dim Handler As System.Object
Dim value As System.Integer

value = instance.ShowUserNotification(Definition, Handler)
```

### C#

```csharp
System.int ShowUserNotification(
   System.object Definition,
   System.object Handler
)
```

### C++/CLI

```cpp
System.int ShowUserNotification(
   System.Object^ Definition,
   System.Object^ Handler
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Definition`: [IUserNotificationDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition.html)
- `Handler`: [IUserNotificationHandler](ms-its:swpublishedapi.chm::/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IUserNotificationHandler.html)

### Return Value

Result code as defined by [swShowNotificationResult_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swShowNotificationResult_e.html)

## VBA Syntax

See [SldWorks::ShowUserNotification](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~ShowUserNotification.html).

## Examples

See the [IUserNotificationHandler](ms-its:swpublishedapi.chm::/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IUserNotificationHandler.html) examples.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
