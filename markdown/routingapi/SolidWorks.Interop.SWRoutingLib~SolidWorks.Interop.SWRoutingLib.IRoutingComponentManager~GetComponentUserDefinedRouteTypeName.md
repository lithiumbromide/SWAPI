---
title: "GetComponentUserDefinedRouteTypeName Method (IRoutingComponentManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRoutingComponentManager"
member: "GetComponentUserDefinedRouteTypeName"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~GetComponentUserDefinedRouteTypeName.html"
---

# GetComponentUserDefinedRouteTypeName Method (IRoutingComponentManager)

Gets the name of the user-defined route for the active routing component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponentUserDefinedRouteTypeName() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IRoutingComponentManager
Dim value As System.String

value = instance.GetComponentUserDefinedRouteTypeName()
```

### C#

```csharp
System.string GetComponentUserDefinedRouteTypeName()
```

### C++/CLI

```cpp
System.String^ GetComponentUserDefinedRouteTypeName();
```

### Return Value

Name of the user-defined route for the active routing component

## VBA Syntax

See [RoutingComponentManager::GetComponentUserDefinedRouteTypeName](ms-its:routingapivb6.chm::/SWRoutingLib~RoutingComponentManager~GetComponentUserDefinedRouteTypeName.html).

## Examples

[Set User-defined Route (C#)](Set_User-defined_Route_Example_CSharp.htm)
[Set User-defined Route (VB.NET)](Set_User-defined_Route_Example_VBNET.htm)
[Set User-defined Route (VBA)](Set_User-defined_Route_Example_VB.htm)

## Remarks

The name of a user-defined route for the active routing component is optional and intended for:

- air conditioning and other mechanical styles of ducting.
- space planning.

Examples of names of user-defined route types are **HVAC**, **Ducting**, **Conveyors**, **Space** **Planning**, etc.

## See Also

[IRoutingComponentManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager.html)
[IRoutingComponentManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager_members.html)
[IRoutingComponentManager::SetComponentUserDefinedRouteTypeName Method ()](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~SetComponentUserDefinedRouteTypeName.html)
[IRoutingComponentManager::GetComponentCrossSectionType Method ()](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~GetComponentCrossSectionType.html)
[IRoutingComponentManager::SetComponentCrossSectionType Method ()](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~SetComponentCrossSectionType.html)

## Availability

SOLIDWORKS Routing 2015 FCS
