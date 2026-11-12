---
title: "GetRoutingStringValue Method (IRoutingComponentManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRoutingComponentManager"
member: "GetRoutingStringValue"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager~GetRoutingStringValue.html"
---

# GetRoutingStringValue Method (IRoutingComponentManager)

Gets the string value for the specified aspect of the active routing component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRoutingStringValue( _
   ByVal StringID As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IRoutingComponentManager
Dim StringID As System.Integer
Dim value As System.String

value = instance.GetRoutingStringValue(StringID)
```

### C#

```csharp
System.string GetRoutingStringValue(
   System.int StringID
)
```

### C++/CLI

```cpp
System.String^ GetRoutingStringValue(
   System.int StringID
)
```

### Parameters

- `StringID`: Integer representing one of the aspects of the routing component as follows:

  - 0 - pipe sketch
  - 1 - inner diameter
  - 2 - outer diameter
  - 3 - filter sketch
  - 4 - nominal diameter
  - 5 - length extrusion
  - 6 - specification
  - 7 - pipe identifier
  - 8 - elbow arc
  - 9 - bend angle
  - 10 - bend radius
  - 11 - BOM elbow angle
  - 12 - BOM pipe length
  - 13 - BOM total pipe length
  - 14 - vertical axis
  - 15 - axis of rotation
  - 16 - clip axis
  - 17 - BOM route length
  - 18 - ignore BOM value

### Return Value

String value for the specified aspect

## VBA Syntax

See [RoutingComponentManager::GetRoutingStringValue](ms-its:routingapivb6.chm::/SWRoutingLib~RoutingComponentManager~GetRoutingStringValue.html).

## Examples

[Get and Set Routing Component Properties Example (C#)](Get_and_Set_Routing_Component_Properties_Example_CSharp.htm)
[Get and Set Routing Component Properties Example (VB.NET)](Get_and_Set_Routing_Component_Properties_Example_VBNET.htm)
[Get and Set Routing Component Properties Example (VBA)](Get_and_Set_Routing_Component_Properties_Example_VB.htm)

## See Also

[IRoutingComponentManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager.html)
[IRoutingComponentManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRoutingComponentManager_members.html)

## Availability

SOLIDWORKS Routing 2011 FCS
