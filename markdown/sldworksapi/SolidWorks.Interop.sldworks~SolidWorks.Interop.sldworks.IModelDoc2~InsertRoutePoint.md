---
title: "InsertRoutePoint Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertRoutePoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertRoutePoint.html"
---

# InsertRoutePoint Method (IModelDoc2)

Adds a route point based on the selected point.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertRoutePoint()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2

instance.InsertRoutePoint()
```

### C#

```csharp
void InsertRoutePoint()
```

### C++/CLI

```cpp
void InsertRoutePoint();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::InsertRoutePoint](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertRoutePoint.html).

## Remarks

If the selection set is not complete, then the Insert Route Point dialog is displayed.

The route point is the point on the fitting that aligns with the sketch point when the fitting is inserted.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::EditRoute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRoute.html)
[IAssemblyDoc::GetRouteManager Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetRouteManager.html)
[IAssemblyDoc::IsRouteAssembly Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IsRouteAssembly.html)
[IFeatureManager::InsertConnectionPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertConnectionPoint.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
