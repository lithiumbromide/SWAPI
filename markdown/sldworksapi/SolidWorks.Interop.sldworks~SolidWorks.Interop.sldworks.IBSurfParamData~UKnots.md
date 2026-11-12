---
title: "UKnots Property (IBSurfParamData)"
project: "SOLIDWORKS API Help"
interface: "IBSurfParamData"
member: "UKnots"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~UKnots.html"
---

# UKnots Property (IBSurfParamData)

Gets the knot vector in the U direction.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property UKnots As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBSurfParamData
Dim value As System.Object

value = instance.UKnots
```

### C#

```csharp
System.object UKnots {get;}
```

### C++/CLI

```cpp
property System.Object^ UKnots {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of knot doubles

## VBA Syntax

See [BSurfParamData::UKnots](ms-its:sldworksapivb6.chm::/sldworks~BSurfParamData~UKnots.html).

## Examples

[Get B-Spline Surface Parameterization Data (C#)](Get_B-Spline_Surface_Parameterization_Data_Example_CSharp.htm)
[Get B-Spline Surface Parameterization Data (VB.NET)](Get_B-Spline_Surface_Parameterization_Data_Example_VBNET.htm)
[Get B-Spline Surface Parameterization Data (VBA)](Get_B-Spline_Surface_Parameterization_Data_Example_VB.htm)

## Remarks

Returned array contains ([control-point column count](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBSurfParamData~ControlPointColumnCount.html) + [U order](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBSurfParamData~UOrder.html)) knot values. If the surface is periodic in the U direction, then data is converted and returned in a non-periodic form with additional knots added to the surface ends.

## See Also

[IBSurfParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData.html)
[IBSurfParamData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData_members.html)
[IBSurfParamData::VKnots Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~VKnots.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
