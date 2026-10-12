---
title: "EndPoint Property (ICurveParamData)"
project: "SOLIDWORKS API Help"
interface: "ICurveParamData"
member: "EndPoint"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveParamData~EndPoint.html"
---

# EndPoint Property (ICurveParamData)

Gets the x, y, and z coordinates for the end point of this curve.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property EndPoint As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveParamData
Dim value As System.Object

value = instance.EndPoint
```

### C#

```csharp
System.object EndPoint {get;}
```

### C++/CLI

```cpp
property System.Object^ EndPoint {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of three doubles

## VBA Syntax

See [CurveParamData::EndPoint](ms-its:sldworksapivb6.chm::/sldworks~CurveParamData~EndPoint.html).

## Examples

If [ICurveParamData::Sense](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurveParamData~Sense.html) returns false, then the curve and edge are in opposite directions. In that case, [ICurveParamData::StartPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurveParamData~StartPoint.html) corresponds to the end of the edge, and end point corresponds to the start of the edge.

## Examples

[Get Edge Curve Parameterization (C#)](Get_Edge_Curve_Parameterization_Example_CSharp.htm)
[Get Edge Curve Parameterization (VB.NET)](Get_Edge_Curve_Parameterization_Example_VBNET.htm)
[Get Edge Curve Parameterization (VBA)](Get_Edge_Curve_Parameterization_Example_VB.htm)

## See Also

[ICurveParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveParamData.html)
[ICurveParamData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveParamData_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
