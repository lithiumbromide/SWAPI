---
title: "SketchRectangle Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SketchRectangle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchRectangle.html"
---

# SketchRectangle Method (IModelDoc2)

Obsolete. Superseded by [ISketchManager::CreateCornerRectangle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~CreateCornerRectangle.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SketchRectangle( _
   ByVal Val1 As System.Double, _
   ByVal Val2 As System.Double, _
   ByVal Z1 As System.Double, _
   ByVal Val3 As System.Double, _
   ByVal Val4 As System.Double, _
   ByVal Z2 As System.Double, _
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
Dim Val5 As System.Boolean

instance.SketchRectangle(Val1, Val2, Z1, Val3, Val4, Z2, Val5)
```

### C#

```csharp
void SketchRectangle(
   System.double Val1,
   System.double Val2,
   System.double Z1,
   System.double Val3,
   System.double Val4,
   System.double Z2,
   System.bool Val5
)
```

### C++/CLI

```cpp
void SketchRectangle(
   System.double Val1,
   System.double Val2,
   System.double Z1,
   System.double Val3,
   System.double Val4,
   System.double Z2,
   System.bool Val5
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Val1`: Upper-left x value in meters
- `Val2`: Upper-left y value in meters
- `Z1`: Upper-left z value in meters
- `Val3`: Lower-right x value in meters
- `Val4`: Lower-right y value in meters
- `Z2`: Lower-right z value in meters
- `Val5`: Not used

## VBA Syntax

See [ModelDoc2::SketchRectangle](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SketchRectangle.html).

## Examples

[Create Revolve Features (VBA)](Create_Revolve_Features_Example_VB.htm)
[Connect to SOLIDWORKS Session (C#)](Connect_to_SOLIDWORKS_Session_CSharp.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::SketchRectangleAtAnyAngle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchRectangleAtAnyAngle.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
