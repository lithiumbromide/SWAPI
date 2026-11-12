---
title: "GetElectricalDrawingSettings Method (IElectricalFlatRoute)"
project: "SOLIDWORKS Routing API Help"
interface: "IElectricalFlatRoute"
member: "GetElectricalDrawingSettings"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalFlatRoute~GetElectricalDrawingSettings.html"
---

# GetElectricalDrawingSettings Method (IElectricalFlatRoute)

Gets the electrical drawing settings for this flat route.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetElectricalDrawingSettings( _
   ByRef elecBomTblTmplt As System.String, _
   ByRef cutListTmplt As System.String, _
   ByRef ConnectorTblTmplt As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IElectricalFlatRoute
Dim elecBomTblTmplt As System.String
Dim cutListTmplt As System.String
Dim ConnectorTblTmplt As System.String
Dim value As System.Integer

value = instance.GetElectricalDrawingSettings(elecBomTblTmplt, cutListTmplt, ConnectorTblTmplt)
```

### C#

```csharp
System.int GetElectricalDrawingSettings(
   out System.string elecBomTblTmplt,
   out System.string cutListTmplt,
   out System.string ConnectorTblTmplt
)
```

### C++/CLI

```cpp
System.int GetElectricalDrawingSettings(
   [Out] System.String^ elecBomTblTmplt,
   [Out] System.String^ cutListTmplt,
   [Out] System.String^ ConnectorTblTmplt
)
```

### Parameters

- `elecBomTblTmplt`: Path and filename of the electrical (ECAD) BOM table template
- `cutListTmplt`: Path and filename of the cut list table template
- `ConnectorTblTmplt`: Path and filename of the connector table template

### Return Value

0 if successful, 1 if not

## VBA Syntax

See [ElectricalFlatRoute::GetElectricalDrawingSettings](ms-its:routingapivb6.chm::/SWRoutingLib~ElectricalFlatRoute~GetElectricalDrawingSettings.html).

## See Also

[IElectricalFlatRoute Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalFlatRoute.html)
[IElectricalFlatRoute Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IElectricalFlatRoute_members.html)

## Availability

SOLIDWORKS Routing 2009 FCS
