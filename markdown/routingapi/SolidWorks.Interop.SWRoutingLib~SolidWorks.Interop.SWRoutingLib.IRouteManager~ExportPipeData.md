---
title: "ExportPipeData Method (IRouteManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRouteManager"
member: "ExportPipeData"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager~ExportPipeData.html"
---

# ExportPipeData Method (IRouteManager)

Exports pipe data in Piping Component File (PCF) format.

## Syntax

### Visual Basic (Declaration)

```vb
Function ExportPipeData( _
   ByVal fileName As System.String, _
   ByVal units As System.Integer, _
   ByVal options As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRouteManager
Dim fileName As System.String
Dim units As System.Integer
Dim options As System.Integer
Dim value As System.Integer

value = instance.ExportPipeData(fileName, units, options)
```

### C#

```csharp
System.int ExportPipeData(
   System.string fileName,
   System.int units,
   System.int options
)
```

### C++/CLI

```cpp
System.int ExportPipeData(
   System.String^ fileName,
   System.int units,
   System.int options
)
```

### Parameters

- `fileName`: Directory path where `<piping_assembly_name>.`pcf is created
- `units`: Units of exported pipe data

  - 0 = millimeters
  - 3 = inches
- `options`: Export options; not yet defined

### Return Value

Status as defined in [swRoutingExportPipeDataError_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swRoutingExportPipeDataError_e.html)

## VBA Syntax

See [RouteManager::ExportPipeData](ms-its:routingapivb6.chm::/SWRoutingLib~RouteManager~ExportPipeData.html).

## Examples

[Export Pipe Data Example (C#)](Export_Pipe_Data_Example_CSharp.htm)
[Export Pipe Data Example (VB.NET)](Export_Pipe_Data_Example_VBNET.htm)
[Export Pipe Data Example (VBA)](Export_Pipe_Data_Example_VB.htm)

## Remarks

This method is only valid for use with assemblies containing pipes.

## See Also

[IRouteManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager.html)
[IRouteManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager_members.html)

## Availability

SOLIDWORKS Routing 2008 FCS
