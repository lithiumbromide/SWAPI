---
title: "TurnBy Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "TurnBy"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~TurnBy.html"
---

# TurnBy Method (IModelView)

Rotates the camera by the specified angles about the camera's x and y axes.

## Syntax

### Visual Basic (Declaration)

```vb
Sub TurnBy( _
   ByVal XAngle As System.Double, _
   ByVal YAngle As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim XAngle As System.Double
Dim YAngle As System.Double

instance.TurnBy(XAngle, YAngle)
```

### C#

```csharp
void TurnBy(
   System.double XAngle,
   System.double YAngle
)
```

### C++/CLI

```cpp
void TurnBy(
   System.double XAngle,
   System.double YAngle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XAngle`: Angle by which to rotate the camera about its x axis
- `YAngle`: Angle by which to rotate the camera about its y axis

## VBA Syntax

See [ModelView::TurnBy](ms-its:sldworksapivb6.chm::/sldworks~ModelView~TurnBy.html).

## Remarks

The model view must have an active camera.

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[IModelView::Camera Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Camera.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
