---
title: "SketchRectangleAtAnyAngle Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SketchRectangleAtAnyAngle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchRectangleAtAnyAngle.html"
---

# SketchRectangleAtAnyAngle Method (IModelDoc2)

Obsolete. Superseded by [ISketchManager::Create3PointCornerRectangle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~Create3PointCornerRectangle.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SketchRectangleAtAnyAngle( _
   ByVal Val1 As System.Double, _
   ByVal Val2 As System.Double, _
   ByVal Z1 As System.Double, _
   ByVal Val3 As System.Double, _
   ByVal Val4 As System.Double, _
   ByVal Z2 As System.Double, _
   ByVal Val3x As System.Double, _
   ByVal Val3y As System.Double, _
   ByVal Z3 As System.Double, _
   ByVal Val5 As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Val1 As System.Double
Dim Val2 As System.Double
Dim Z1 As System.Double
Dim Val3 As System.Double
Dim Val4 As System.Double
Dim Z2 As System.Double
Dim Val3x As System.Double
Dim Val3y As System.Double
Dim Z3 As System.Double
Dim Val5 As System.Boolean

instance.SketchRectangleAtAnyAngle(Val1, Val2, Z1, Val3, Val4, Z2, Val3x, Val3y, Z3, Val5)
```

### C#

```csharp
void SketchRectangleAtAnyAngle(
   System.double Val1,
   System.double Val2,
   System.double Z1,
   System.double Val3,
   System.double Val4,
   System.double Z2,
   System.double Val3x,
   System.double Val3y,
   System.double Z3,
   System.bool Val5
)
```

### C++/CLI

```cpp
void SketchRectangleAtAnyAngle(
   System.double Val1,
   System.double Val2,
   System.double Z1,
   System.double Val3,
   System.double Val4,
   System.double Z2,
   System.double Val3x,
   System.double Val3y,
   System.double Z3,
   System.bool Val5
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Val1`: X value of corner 1
- `Val2`: Y value of corner 1
- `Z1`: Z value of corner 1
- `Val3`: X value of corner 2 defining the bottom line from corner 1
- `Val4`: Y value of corner 2 defining the bottom line from corner 1
- `Z2`: Z value of corner 2 defining the bottom line from corner 1
- `Val3x`: X value of corner 3; diagonal to corner 1
- `Val3y`: Y value of corner 3; diagonal to corner 1
- `Z3`: Z value of corner 3; diagonal to corner 1
- `Val5`: True to add automatic constraints to the rectangle geometry, false to not

## VBA Syntax

See [ModelDoc2::SketchRectangleAtAnyAngle](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SketchRectangleAtAnyAngle.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::SketchRectangle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchRectangle.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
