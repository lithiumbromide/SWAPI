---
title: "DefineUserNotification Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "DefineUserNotification"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DefineUserNotification.html"
---

# DefineUserNotification Method (ISldWorks)

Called by a SOLIDWORKS add-in, creates a user notification definition object.

## Syntax

### Visual Basic (Declaration)

```vb
Function DefineUserNotification( _
   ByVal UniqueName As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim UniqueName As System.String
Dim value As System.Object

value = instance.DefineUserNotification(UniqueName)
```

### C#

```csharp
System.object DefineUserNotification(
   System.string UniqueName
)
```

### C++/CLI

```cpp
System.Object^ DefineUserNotification(
   System.String^ UniqueName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UniqueName`: Unique ID of this user notification

### Return Value

[IUserNotificationDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition.html)

## VBA Syntax

See [SldWorks::DefineUserNotification](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~DefineUserNotification.html).

## Examples

See the [IUserNotificationHandler](ms-its:swpublishedapi.chm::/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IUserNotificationHandler.html) examples.

## Remarks

It is the add-in's responsibility to ensure that the ID is unique by using, for example, a combination of add-in module name and unique notification identifier:

"MyAddInName+ID_MYNOTIFICATION1"

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
