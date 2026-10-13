---
title: "GetComponentCrossSectionType Method (IRoutingComponentManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRoutingComponentManager"
member: "GetComponentCrossSectionType"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~GetComponentCrossSectionType.html"
---

# GetComponentCrossSectionType Method (IRoutingComponentManager)

Gets the type of cross section for a user-defined route for the active routing component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponentCrossSectionType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRoutingComponentManager
Dim value As System.Integer

value = instance.GetComponentCrossSectionType()
```

### C#

```csharp
System.int GetComponentCrossSectionType()
```

### C++/CLI

```cpp
System.int GetComponentCrossSectionType();
```

### Return Value

Type of cross section for a user-defined route for the active routing component as defined in [swComponentCrossSectionType_e](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.swComponentCrossSectionType_e.html)

## VBA Syntax

See [RoutingComponentManager::GetComponentCrossSectionType](ms-its:routingapivb6.chm::/SWRoutingLib~RoutingComponentManager~GetComponentCrossSectionType.html).

## Examples

[Set User-defined Route (C#)](Set_User-defined_Route_Example_CSharp.htm)
[Set User-defined Route (VB.NET)](Set_User-defined_Route_Example_VBNET.htm)
[Set User-defined Route (VBA)](Set_User-defined_Route_Example_VB.htm)

## See Also

[IRoutingComponentManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager.html)
[IRoutingComponentManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager_members.html)
[IRoutingComponentManager::SetComponentCrossSectionType Method ()](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~SetComponentCrossSectionType.html)
[IRoutingComponentManager::GetComponentUserDefinedRouteTypeName Method ()](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~GetComponentUserDefinedRouteTypeName.html)
[IRoutingComponentManager::SetComponentUserDefinedRouteTypeName Method ()](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~SetComponentUserDefinedRouteTypeName.html)

## Availability

SOLIDWORKS Routing 2015 FCS
