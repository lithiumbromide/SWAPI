---
title: "ImportFromToList Method (IRouteManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRouteManager"
member: "ImportFromToList"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager~ImportFromToList.html"
---

# ImportFromToList Method (IRouteManager)

Imports electrical connection data (guidelines) using the specified from-to list.

## Syntax

### Visual Basic (Declaration)

```vb
Function ImportFromToList( _
   ByVal fromtoListFileName As System.String, _
   ByVal componentLibraryFilename As System.String, _
   ByVal cableWireLibraryFileName As System.String, _
   ByVal useExistingAssembly As System.Boolean, _
   ByVal overwriteData As System.Boolean, _
   ByVal searchAllSubAssemblies As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRouteManager
Dim fromtoListFileName As System.String
Dim componentLibraryFilename As System.String
Dim cableWireLibraryFileName As System.String
Dim useExistingAssembly As System.Boolean
Dim overwriteData As System.Boolean
Dim searchAllSubAssemblies As System.Boolean
Dim value As System.Boolean

value = instance.ImportFromToList(fromtoListFileName, componentLibraryFilename, cableWireLibraryFileName, useExistingAssembly, overwriteData, searchAllSubAssemblies)
```

### C#

```csharp
System.bool ImportFromToList(
   System.string fromtoListFileName,
   System.string componentLibraryFilename,
   System.string cableWireLibraryFileName,
   System.bool useExistingAssembly,
   System.bool overwriteData,
   System.bool searchAllSubAssemblies
)
```

### C++/CLI

```cpp
System.bool ImportFromToList(
   System.String^ fromtoListFileName,
   System.String^ componentLibraryFilename,
   System.String^ cableWireLibraryFileName,
   System.bool useExistingAssembly,
   System.bool overwriteData,
   System.bool searchAllSubAssemblies
)
```

### Parameters

- `fromtoListFileName`: Pathname of the Excel file (*.xlsx) containing the from-to list
- `componentLibraryFilename`: Pathname of a SOLIDWORKS component library in XML format
- `cableWireLibraryFileName`: Pathname of a SOLIDWORKS cable/wire library in XML format
- `useExistingAssembly`: True to use an existing assembly, false to start a new assembly
- `overwriteData`: True to overwrite data, false to insert data; applies only if useExistingAssembly = true
- `searchAllSubAssemblies`: True to search all sub-assemblies for pre-placed connectors, false to not

### Return Value

True if successful, false if not

## VBA Syntax

See [RouteManager::ImportFromToList](ms-its:routingapivb6.chm::/SWRoutingLib~RouteManager~ImportFromToList.html).

## Examples

[Import a From-To List Example (C#)](Import_a_From-To_List_Example_CSharp.htm)
[Import a From-To List Example (VB.NET)](Import_a_From-To_List_Example_VBNET.htm)
[Import a From-To List Example (VBA)](Import_a_From-To_List_Example_VB.htm)

## Remarks

Before calling this method:

1. In the FeatureManager design tree, select the assembly that contains the route to which to add guidelines.
2. Call [IRouteManager::EditRoute](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IRouteManager~EditRoute.html).

## See Also

[IRouteManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager.html)
[IRouteManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager_members.html)
[IAutoRoute::ConvertGuidelinesToRoute Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAutoRoute~ConvertGuidelinesToRoute.html)
[IAutoRoute::MergeGuidelines Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAutoRoute~MergeGuidelines.html)
[IAutoRoute::SelectGuidelines Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAutoRoute~SelectGuidelines.html)
[IAutoRoute::ShowGuidelines Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAutoRoute~ShowGuidelines.html)

## Availability

SOLIDWORKS Routing 2011 FCS
