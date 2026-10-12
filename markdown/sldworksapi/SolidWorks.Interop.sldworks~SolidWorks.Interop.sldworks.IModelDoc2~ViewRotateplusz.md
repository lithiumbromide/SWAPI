---
title: "ViewRotateplusz Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ViewRotateplusz"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewRotateplusz.html"
---

# ViewRotateplusz Method (IModelDoc2)

Rotates the view around z in a positive direction with the current increment.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ViewRotateplusz()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2

instance.ViewRotateplusz()
```

### C#

```csharp
void ViewRotateplusz()
```

### C++/CLI

```cpp
void ViewRotateplusz();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::ViewRotateplusz](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ViewRotateplusz.html).

## Examples

[Rotate Model (VBA)](Rotate_Model_Example_VB.htm)
[Rotate Model (VB.NET)](Rotate_Model_Example_VBNET.htm)
[Rotate Model (C#)](Rotate_Model_Example_CSharp.htm)

## Remarks

To increase the speed of dynamic view changes with hidden-edge display or hidden-grey display, use [IModelView::StartDynamics](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~StartDynamics.html) and [IModelView::StopDynamics](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~StopDynamics.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::ViewZoomToSelection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewZoomToSelection.html)
[IModelDoc2::ViewZoomtofit2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewZoomtofit2.html)
[IModelDoc2::ViewZoomTo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewZoomTo2.html)
[IModelDoc2::ViewZoomto Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewZoomto.html)
[IModelDoc2::ViewZoomout Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewZoomout.html)
[IModelDoc2::ViewZoomin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewZoomin.html)
[IModelDoc2::ViewRotYPlusNinety Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewRotYPlusNinety.html)
[IModelDoc2::ViewRotYMinusNinety Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewRotYMinusNinety.html)
[IModelDoc2::ViewRotXPlusNinety Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewRotXPlusNinety.html)
[IModelDoc2::ViewRotXMinusNinety Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewRotXMinusNinety.html)
[IModelDoc2::ViewRotateplusy Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewRotateplusy.html)
[IModelDoc2::ViewRotateplusx Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewRotateplusx.html)
[IModelDoc2::ViewRotateminusz Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewRotateminusz.html)
[IModelDoc2::ViewRotateminusy Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewRotateminusy.html)
[IModelDoc2::ViewRotateminusx Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewRotateminusx.html)
[IModelDoc2::ViewRotate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewRotate.html)
[IModelDoc2::ViewOrientationUndo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewOrientationUndo.html)
[IModelDoc2::ViewZoomto Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewZoomto.html)
[IModelDocExtension::ViewZoomToSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ViewZoomToSheet.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
