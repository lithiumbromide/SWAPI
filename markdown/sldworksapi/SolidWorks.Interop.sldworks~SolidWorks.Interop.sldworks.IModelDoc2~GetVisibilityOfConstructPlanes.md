---
title: "GetVisibilityOfConstructPlanes Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetVisibilityOfConstructPlanes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetVisibilityOfConstructPlanes.html"
---

# GetVisibilityOfConstructPlanes Method (IModelDoc2)

Gets whether construction (reference) planes are currently visible.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetVisibilityOfConstructPlanes() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Boolean

value = instance.GetVisibilityOfConstructPlanes()
```

### C#

```csharp
System.bool GetVisibilityOfConstructPlanes()
```

### C++/CLI

```cpp
System.bool GetVisibilityOfConstructPlanes();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if construction planes are currently visible, false if not

## VBA Syntax

See [ModelDoc2::GetVisibilityOfConstructPlanes](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetVisibilityOfConstructPlanes.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::ViewDispRefplanes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewDispRefplanes.html)
[IModelDoc2::CreatePlaneAtAngle3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneAtAngle3.html)
[IModelDoc2::CreatePlaneAtOffset3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneAtOffset3.html)
[IModelDoc2::CreatePlaneAtSurface3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneAtSurface3.html)
[IModelDoc2::CreatePlaneFixed2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneFixed2.html)
[IModelDoc2::CreatePlanePerCurveAndPassPoint3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlanePerCurveAndPassPoint3.html)
[IModelDoc2::CreatePlaneThru3Points3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneThru3Points3.html)
[IModelDoc2::CreatePlaneThruLineAndPt Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneThruLineAndPt.html)
[IModelDoc2::CreatePlaneThruPtParallelToPlane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneThruPtParallelToPlane.html)
[IModelDoc2::ICreatePlaneAtAngle3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneAtAngle3.html)
[IModelDoc2::ICreatePlaneAtOffset3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneAtOffset3.html)
[IModelDoc2::ICreatePlaneAtSurface3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneAtSurface3.html)
[IModelDoc2::ICreatePlaneFixed2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneFixed2.html)
[IModelDoc2::ICreatePlanePerCurveAndPassPoint3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlanePerCurveAndPassPoint3.html)
[IModelDoc2::ICreatePlaneThru3Points3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneThru3Points3.html)
[IModelDoc2::ICreatePlaneThruLineAndPt Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneThruLineAndPt.html)
[IModelDoc2::ICreatePlaneThruPtParallelToPlane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneThruPtParallelToPlane.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
