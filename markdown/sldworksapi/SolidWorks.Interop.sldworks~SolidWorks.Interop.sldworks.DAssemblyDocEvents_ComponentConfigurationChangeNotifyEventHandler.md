---
title: "DAssemblyDocEvents_ComponentConfigurationChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_ComponentConfigurationChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ComponentConfigurationChangeNotifyEventHandler.html"
---

# DAssemblyDocEvents_ComponentConfigurationChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when a reference component's configuration is being changed in an assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_ComponentConfigurationChangeNotifyEventHandler( _
   ByVal componentName As System.String, _
   ByVal oldConfigurationName As System.String, _
   ByVal newConfigurationName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_ComponentConfigurationChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_ComponentConfigurationChangeNotifyEventHandler(
   System.string componentName,
   System.string oldConfigurationName,
   System.string newConfigurationName
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_ComponentConfigurationChangeNotifyEventHandler(
   System.String^ componentName,
   System.String^ oldConfigurationName,
   System.String^ newConfigurationName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `componentName`: Name of reference component whose configuration is changing
- `oldConfigurationName`: Old name of reference component's configuration
- `newConfigurationName`: New name of reference component's configuration

## VBA Syntax

See [ComponentConfigurationChangeNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~ComponentConfigurationChangeNotify_EV.html).

## Examples

[Fire Notification When Changing Configuration of Reference Component (C#)](Fire_Notification_When_Changing_Configuration_of_Reference_Component_Example_CSharp.htm)
[Fire Notification When Changing Configuration of Reference Component (VB.NET)](Fire_Notification_When_Changing_Configuration_of_Reference_Component__Example_VBNET.htm)
[Fire Notification When Changing Configuration of Reference Component (VBA)](Fire_Notification_When_Changing_Configuration_of_Reference_Component_Example_VB.htm)

## Remarks

If developing a C++ application, use [swAssemblyComponentConfigurationChangeNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2009 SP4, Revision Number 17.4
