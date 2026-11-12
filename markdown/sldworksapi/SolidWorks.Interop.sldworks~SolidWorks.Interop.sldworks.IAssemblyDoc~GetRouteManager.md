---
title: "GetRouteManager Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "GetRouteManager"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetRouteManager.html"
---

# GetRouteManager Method (IAssemblyDoc)

Gets the SOLIDWORKS Routing API.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRouteManager() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As System.Object

value = instance.GetRouteManager()
```

### C#

```csharp
System.object GetRouteManager()
```

### C++/CLI

```cpp
System.Object^ GetRouteManager();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

SOLIDWORKS Routing API

## VBA Syntax

See [AssemblyDoc::GetRouteManager](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~GetRouteManager.html).

## Examples

[Create Auto Route (VBA)](Create_Auto_Route_Example_VB.htm)
[Create Auto Route (VB.NET)](Create_Auto_Route_Example_VBNET.htm)
[Create Auto Route (C#)](Create_Auto_Route_Example_CSharp.htm)

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::IsRouteAssembly Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IsRouteAssembly.html)
[IModelDoc2::EditRoute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRoute.html)
[IModelDoc2::InsertRoutePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertRoutePoint.html)
[IFeatureManager::InsertConnectionPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertConnectionPoint.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
