---
title: "SetComponentUserDefinedRouteTypeName Method (IRoutingComponentManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRoutingComponentManager"
member: "SetComponentUserDefinedRouteTypeName"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~SetComponentUserDefinedRouteTypeName.html"
---

# SetComponentUserDefinedRouteTypeName Method (IRoutingComponentManager)

Sets the name of the user-defined route for the active routing component.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetComponentUserDefinedRouteTypeName( _
   ByVal StringID As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRoutingComponentManager
Dim StringID As System.String

instance.SetComponentUserDefinedRouteTypeName(StringID)
```

### C#

```csharp
void SetComponentUserDefinedRouteTypeName(
   System.string StringID
)
```

### C++/CLI

```cpp
void SetComponentUserDefinedRouteTypeName(
   System.String^ StringID
)
```

### Parameters

- `StringID`: Name of the user-defined route for the active routing component

## VBA Syntax

See [RoutingComponentManager::SetComponentUserDefinedRouteTypeName](ms-its:routingapivb6.chm::/SWRoutingLib~RoutingComponentManager~SetComponentUserDefinedRouteTypeName.html).

## Examples

[Set User-defined Route (C#)](Set_User-defined_Route_Example_CSharp.htm)
[Set User-defined Route (VB.NET)](Set_User-defined_Route_Example_VBNET.htm)
[Set User-defined Route (VBA)](Set_User-defined_Route_Example_VB.htm)

## Remarks

Specifying a name for a user-defined route for the active routing component is optional and intended for:

- air conditioning and other mechanical styles of ducting.
- space planning.

Examples of names of user-defined route types are **HVAC**, **Ducting**, **Conveyors**, **Space** **Planning**, etc.

## See Also

[IRoutingComponentManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager.html)
[IRoutingComponentManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager_members.html)
[IRoutingComponentManager::GetComponentUserDefinedRouteTypeName Method ()](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~GetComponentUserDefinedRouteTypeName.html)
[IRoutingComponentManager::SetComponentCrossSectionType Method ()](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~SetComponentCrossSectionType.html)
[IRoutingComponentManager::GetComponentCrossSectionType Method ()](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~GetComponentCrossSectionType.html)

## Availability

SOLIDWORKS Routing 2015 FCS
