---
title: "CloseUserNotification Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "CloseUserNotification"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseUserNotification.html"
---

# CloseUserNotification Method (ISldWorks)

Closes the specified user notification.

## Syntax

### Visual Basic (Declaration)

```vb
Sub CloseUserNotification( _
   ByVal Definition As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Definition As System.Object

instance.CloseUserNotification(Definition)
```

### C#

```csharp
void CloseUserNotification(
   System.object Definition
)
```

### C++/CLI

```cpp
void CloseUserNotification(
   System.Object^ Definition
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Definition`: [IUserNotificationDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition.html)

## VBA Syntax

See [SldWorks::CloseUserNotification](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~CloseUserNotification.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
