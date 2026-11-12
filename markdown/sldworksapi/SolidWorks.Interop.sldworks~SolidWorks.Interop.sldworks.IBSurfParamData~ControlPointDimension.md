---
title: "ControlPointDimension Property (IBSurfParamData)"
project: "SOLIDWORKS API Help"
interface: "IBSurfParamData"
member: "ControlPointDimension"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~ControlPointDimension.html"
---

# ControlPointDimension Property (IBSurfParamData)

Gets the dimension of the control points.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ControlPointDimension As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBSurfParamData
Dim value As System.Integer

value = instance.ControlPointDimension
```

### C#

```csharp
System.int ControlPointDimension {get;}
```

### C++/CLI

```cpp
property System.int ControlPointDimension {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

3 - non-rational surfaces

4 - rational surfaces

## VBA Syntax

See [BSurfParamData::ControlPointDimension](ms-its:sldworksapivb6.chm::/sldworks~BSurfParamData~ControlPointDimension.html).

## Examples

[Get B-Spline Surface Parameterization Data (C#)](Get_B-Spline_Surface_Parameterization_Data_Example_CSharp.htm)
[Get B-Spline Surface Parameterization Data (VB.NET)](Get_B-Spline_Surface_Parameterization_Data_Example_VBNET.htm)
[Get B-Spline Surface Parameterization Data (VBA)](Get_B-Spline_Surface_Parameterization_Data_Example_VB.htm)

## See Also

[IBSurfParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData.html)
[IBSurfParamData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData_members.html)
[IBSurfParamData::GetControlPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~GetControlPoints.html)
[IBSurfParamData::IGetControlPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~IGetControlPoints.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
