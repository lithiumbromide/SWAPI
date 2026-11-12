---
title: "ExportTubeData Method (IRouteManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRouteManager"
member: "ExportTubeData"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager~ExportTubeData.html"
---

# ExportTubeData Method (IRouteManager)

Exports an HTML bend data table containing the tangent or intersection points in a tubing assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function ExportTubeData( _
   ByVal fileName As System.String, _
   ByVal type As System.Integer, _
   ByVal options As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRouteManager
Dim fileName As System.String
Dim type As System.Integer
Dim options As System.Integer
Dim value As System.Integer

value = instance.ExportTubeData(fileName, type, options)
```

### C#

```csharp
System.int ExportTubeData(
   System.string fileName,
   System.int type,
   System.int options
)
```

### C++/CLI

```cpp
System.int ExportTubeData(
   System.String^ fileName,
   System.int type,
   System.int options
)
```

### Parameters

- `fileName`: Specify `<path_name>.<file_extension>`; for example, specify **c:\temp.html** to create **default.html** in **c:\temp**
- `type`: Bend data type as defined in [swExportTubeDataReportType_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swExportTubeDataReportType_e.html)
- `options`: Export options; not yet defined

### Return Value

Status as defined in [swRoutingExportDataError_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swRoutingExportDataError_e.html)

## VBA Syntax

See [RouteManager::ExportTubeData](ms-its:routingapivb6.chm::/SWRoutingLib~RouteManager~ExportTubeData.html).

## Examples

[Export Tube Data Example (C#)](Export_Tube_Data_Example_CSharp.htm)
[Export Tube Data Example (VB.NET)](Export_Tube_Data_Example_VBNET.htm)
[Export Tube Data Example (VBA)](Export_Tube_Data_Example_VB.htm)

## Remarks

This method is only valid for use with assemblies containing tubes.

## See Also

[IRouteManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager.html)
[IRouteManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager_members.html)

## Availability

SOLIDWORKS Routing 2011 FCS
