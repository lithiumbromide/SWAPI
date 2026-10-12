---
title: "ViewZoomTo2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ViewZoomTo2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewZoomTo2.html"
---

# ViewZoomTo2 Method (IModelDoc2)

Zooms to the specified region.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ViewZoomTo2( _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal Z1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double, _
   ByVal Z2 As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim X1 As System.Double
Dim Y1 As System.Double
Dim Z1 As System.Double
Dim X2 As System.Double
Dim Y2 As System.Double
Dim Z2 As System.Double

instance.ViewZoomTo2(X1, Y1, Z1, X2, Y2, Z2)
```

### C#

```csharp
void ViewZoomTo2(
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2
)
```

### C++/CLI

```cpp
void ViewZoomTo2(
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X1`: X value for the lower-left point of the zoom area
- `Y1`: Y value for the lower- left point of the zoom area
- `Z1`: Z value for the lower-left point of the zoom area
- `X2`: X value for the upper-right point of the zoom area
- `Y2`: Y value for the upper-right point of the zoom area
- `Z2`: Z value for the upper-right point of the zoom area

## VBA Syntax

See [ModelDoc2::ViewZoomTo2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ViewZoomTo2.html).

## Examples

[Zoom To Region (VBA)](Zoom_to_Region_Example_VB.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::ViewZoomin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewZoomin.html)
[IModelDoc2::ViewZoomout Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewZoomout.html)
[IModelDoc2::ViewZoomto Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewZoomto.html)
[IModelDoc2::ViewZoomtofit2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewZoomtofit2.html)
[IModelDoc2::ViewZoomToSelection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewZoomToSelection.html)
[IModelDoc2::ViewOrientationUndo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewOrientationUndo.html)
[IModelDoc2::ViewRotate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewRotate.html)
[IModelDoc2::ViewRotateminusx Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewRotateminusx.html)
[IModelDoc2::ViewRotateminusy Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewRotateminusy.html)
[IModelDoc2::ViewRotateminusz Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewRotateminusz.html)
[IModelDoc2::ViewRotateplusx Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewRotateplusx.html)
[IModelDoc2::ViewRotateplusy Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewRotateplusy.html)
[IModelDoc2::ViewRotateplusz Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewRotateplusz.html)
[IModelDoc2::ViewRotXMinusNinety Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewRotXMinusNinety.html)
[IModelDoc2::ViewRotXPlusNinety Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewRotXPlusNinety.html)
[IModelDoc2::ViewRotYMinusNinety Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewRotYMinusNinety.html)
[IModelDoc2::ViewRotYPlusNinety Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewRotYPlusNinety.html)
[IModelDocExtension::ViewZoomToSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ViewZoomToSheet.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
