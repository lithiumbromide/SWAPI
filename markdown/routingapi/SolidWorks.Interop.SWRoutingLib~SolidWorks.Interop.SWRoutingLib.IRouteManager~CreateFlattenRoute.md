---
title: "CreateFlattenRoute Method (IRouteManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRouteManager"
member: "CreateFlattenRoute"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager~CreateFlattenRoute.html"
---

# CreateFlattenRoute Method (IRouteManager)

Creates a flattened route and optionally its drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateFlattenRoute( _
   ByVal flattenType As System.Integer, _
   ByVal connectorOption As System.Integer, _
   ByVal formboardWidth As System.Double, _
   ByVal formboardHeight As System.Double, _
   ByVal segmentOrientation As System.Integer, _
   ByVal drawingOption As System.Boolean, _
   ByVal sheetFormatTemplate As System.String, _
   ByVal elecBOMTemplate As System.String, _
   ByVal cutListTemplate As System.String, _
   ByVal connectorTableTemplate As System.String, _
   ByVal autoBalloons As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRouteManager
Dim flattenType As System.Integer
Dim connectorOption As System.Integer
Dim formboardWidth As System.Double
Dim formboardHeight As System.Double
Dim segmentOrientation As System.Integer
Dim drawingOption As System.Boolean
Dim sheetFormatTemplate As System.String
Dim elecBOMTemplate As System.String
Dim cutListTemplate As System.String
Dim connectorTableTemplate As System.String
Dim autoBalloons As System.Boolean
Dim value As System.Integer

value = instance.CreateFlattenRoute(flattenType, connectorOption, formboardWidth, formboardHeight, segmentOrientation, drawingOption, sheetFormatTemplate, elecBOMTemplate, cutListTemplate, connectorTableTemplate, autoBalloons)
```

### C#

```csharp
System.int CreateFlattenRoute(
   System.int flattenType,
   System.int connectorOption,
   System.double formboardWidth,
   System.double formboardHeight,
   System.int segmentOrientation,
   System.bool drawingOption,
   System.string sheetFormatTemplate,
   System.string elecBOMTemplate,
   System.string cutListTemplate,
   System.string connectorTableTemplate,
   System.bool autoBalloons
)
```

### C++/CLI

```cpp
System.int CreateFlattenRoute(
   System.int flattenType,
   System.int connectorOption,
   System.double formboardWidth,
   System.double formboardHeight,
   System.int segmentOrientation,
   System.bool drawingOption,
   System.String^ sheetFormatTemplate,
   System.String^ elecBOMTemplate,
   System.String^ cutListTemplate,
   System.String^ connectorTableTemplate,
   System.bool autoBalloons
)
```

### Parameters

- `flattenType`: Type of routing drawing as defined in [swRoutingFlattenTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRoutingFlattenTypes_e.html)
- `connectorOption`: Type of connector to display as defined in [swRoutingFlattenConnectorOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRoutingFlattenConnectorOptions_e.html)
- `formboardWidth`: Width of the formboard; only applies if flattenType = 2 (manufacture type)
- `formboardHeight`: Height of the formboard; only applies if flattenType = 2 (manufacture type)
- `segmentOrientation`: Segment orientation as defined in [swRoutingFlattenSegmentOrientation_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRoutingFlattenSegmentOrientation_e.html); only applies if flattenType = 2 (manufacture type)
- `drawingOption`: True to create a drawing of the flattened route, false to not
- `sheetFormatTemplate`: Full pathname of drawing sheet template to use to create the drawing; only applies if drawingOption = true
- `elecBOMTemplate`: Full pathname of electrical BOM table template to use to create the drawing; only applies if drawingOption = true
- `cutListTemplate`: Full pathname of electrical cut list table template to use to create the drawing; only applies if drawingOption = true
- `connectorTableTemplate`: Full pathname of electrical connector table template to use to create the drawing; only applies if drawingOption = true
- `autoBalloons`: True to insert balloons, false to not; only applies if drawingOption = true

### Return Value

Error code as defined in [swFlattenRouteErrorType_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swFlattenRouteErrorType_e.html)

## VBA Syntax

See [RouteManager::CreateFlattenRoute](ms-its:routingapivb6.chm::/SWRoutingLib~RouteManager~CreateFlattenRoute.html).

## Examples

[Create a Flattened Route Example (C#)](Create_a_Flattened_Route_Example_CSharp.htm)
[Create a Flattened Route Example (VB.NET)](Create_a_Flattened_Route_Example_VBNET.htm)
[Create a Flattened Route Example (VBA)](Create_a_Flattened_Route_Example_VB.htm)

## Remarks

Before calling this method, select the assembly that contains the route to flatten.

## See Also

[IRouteManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager.html)
[IRouteManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager_members.html)

## Availability

SOLIDWORKS Routing 2011 FCS
