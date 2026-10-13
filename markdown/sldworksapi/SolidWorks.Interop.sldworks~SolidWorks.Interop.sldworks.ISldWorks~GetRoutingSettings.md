---
title: "GetRoutingSettings Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetRoutingSettings"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetRoutingSettings.html"
---

# GetRoutingSettings Method (ISldWorks)

Gets routing settings.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRoutingSettings() As RoutingSettings
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As RoutingSettings

value = instance.GetRoutingSettings()
```

### C#

```csharp
RoutingSettings GetRoutingSettings()
```

### C++/CLI

```cpp
RoutingSettings^ GetRoutingSettings();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IRoutingSettings](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRoutingSettings.html)

## VBA Syntax

See [SldWorks::GetRoutingSettings](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetRoutingSettings.html).

## Examples

[Get and Save Routing Settings (VBA)](Get_and_Save_Routing_Settings_Example_VB.htm)
[Get and Save Routing Settings (VB.NET)](Get_and_Save_Routing_Settings_Example_VBNET.htm)
[Get and Save Routing Settings (C#)](Get_and_Save_Routing_Settings_Example_CSharp.htm)

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
