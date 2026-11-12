---
title: "ICreateEllipticalArcByCenter Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ICreateEllipticalArcByCenter"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateEllipticalArcByCenter.html"
---

# ICreateEllipticalArcByCenter Method (IModelDoc2)

Creates an elliptical arc trimmed between two points.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ICreateEllipticalArcByCenter( _
   ByRef Center As System.Double, _
   ByRef Major As System.Double, _
   ByRef Minor As System.Double, _
   ByRef Start As System.Double, _
   ByRef End As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Center As System.Double
Dim Major As System.Double
Dim Minor As System.Double
Dim Start As System.Double
Dim End As System.Double

instance.ICreateEllipticalArcByCenter(Center, Major, Minor, Start, End)
```

### C#

```csharp
void ICreateEllipticalArcByCenter(
   ref System.double Center,
   ref System.double Major,
   ref System.double Minor,
   ref System.double Start,
   ref System.double End
)
```

### C++/CLI

```cpp
void ICreateEllipticalArcByCenter(
   System.double% Center,
   System.double% Major,
   System.double% Minor,
   System.double% Start,
   System.double% End
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Center`: Array of 3 doubles (x1, y1, z1) in meters that describe the ellipse center
- `Major`: Array of 3 doubles (x1, y1, z1) in meters that describe a point on the ellipse and on the major axis
- `Minor`: Array of 3 doubles (x1, y1, z1) in meters that describe a point on the ellipse and on the minor axis
- `Start`: Array of 3 doubles (x1, y1, z1) in meters that describe the start point of the ellipse
- `End`: Array of 3 doubles (x1, y1, z1) in meters that describe the end point of the ellipse

### Return Value

True if successfully created, false if not

## VBA Syntax

See [ModelDoc2::ICreateEllipticalArcByCenter](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ICreateEllipticalArcByCenter.html).

## Remarks

The Start and End arguments should be specified in a counter-clockwise (CCW) manner.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::CreateEllipse2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateEllipse2.html)
[IModelDoc2::CreateEllipticalArc2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateEllipticalArc2.html)
[IModelDoc2::CreateEllipticalArcByCenter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateEllipticalArcByCenter.html)
[IModelDoc2::CreateEllipticalArcByCenterVB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateEllipticalArcByCenterVB.html)
[IModelDoc2::ICreateEllipse2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateEllipse2.html)
[IModelDoc2::ICreateEllipticalArc2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateEllipticalArc2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
