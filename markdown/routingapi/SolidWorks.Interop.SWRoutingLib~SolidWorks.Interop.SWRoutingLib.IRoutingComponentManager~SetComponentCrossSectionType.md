---
title: "SetComponentCrossSectionType Method (IRoutingComponentManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRoutingComponentManager"
member: "SetComponentCrossSectionType"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~SetComponentCrossSectionType.html"
---

# SetComponentCrossSectionType Method (IRoutingComponentManager)

Sets the type of cross section for a user-defined route for the active routing component.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetComponentCrossSectionType( _
   ByVal crossSection As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRoutingComponentManager
Dim crossSection As System.Integer

instance.SetComponentCrossSectionType(crossSection)
```

### C#

```csharp
void SetComponentCrossSectionType(
   System.int crossSection
)
```

### C++/CLI

```cpp
void SetComponentCrossSectionType(
   System.int crossSection
)
```

### Parameters

- `crossSection`: Type of cross section for a user-defined route for the active routing component as defined in [swComponentCrossSectionType_e](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.swComponentCrossSectionType_e.html)

## VBA Syntax

See [RoutingComponentManager::SetComponentCrossSectionType](ms-its:routingapivb6.chm::/SWRoutingLib~RoutingComponentManager~SetComponentCrossSectionType.html).

## Examples

[Set User-defined Route (C#)](Set_User-defined_Route_Example_CSharp.htm)
[Set User-defined Route (VB.NET)](Set_User-defined_Route_Example_VBNET.htm)
[Set User-defined Route (VBA)](Set_User-defined_Route_Example_VB.htm)

## See Also

[IRoutingComponentManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager.html)
[IRoutingComponentManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager_members.html)
[IRoutingComponentManager::GetComponentCrossSectionType Method ()](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~GetComponentCrossSectionType.html)
[IRoutingComponentManager::SetComponentUserDefinedRouteTypeName Method ()](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~SetComponentUserDefinedRouteTypeName.html)
[IRoutingComponentManager::GetComponentUserDefinedRouteTypeName Method ()](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~GetComponentUserDefinedRouteTypeName.html)

## Availability

SOLIDWORKS Routing 2015 FCS
