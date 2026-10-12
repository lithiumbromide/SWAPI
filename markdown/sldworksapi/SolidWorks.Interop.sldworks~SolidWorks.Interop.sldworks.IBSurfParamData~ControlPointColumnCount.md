---
title: "ControlPointColumnCount Property (IBSurfParamData)"
project: "SOLIDWORKS API Help"
interface: "IBSurfParamData"
member: "ControlPointColumnCount"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~ControlPointColumnCount.html"
---

# ControlPointColumnCount Property (IBSurfParamData)

Gets the number of control point columns.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ControlPointColumnCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBSurfParamData
Dim value As System.Integer

value = instance.ControlPointColumnCount
```

### C#

```csharp
System.int ControlPointColumnCount {get;}
```

### C++/CLI

```cpp
property System.int ControlPointColumnCount {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of control point columns

## VBA Syntax

See [BSurfParamData::ControlPointColumnCount](ms-its:sldworksapivb6.chm::/sldworks~BSurfParamData~ControlPointColumnCount.html).

## Examples

[Get B-Spline Surface Parameterization Data (C#)](Get_B-Spline_Surface_Parameterization_Data_Example_CSharp.htm)
[Get B-Spline Surface Parameterization Data (VB.NET)](Get_B-Spline_Surface_Parameterization_Data_Example_VBNET.htm)
[Get B-Spline Surface Parameterization Data (VBA)](Get_B-Spline_Surface_Parameterization_Data_Example_VB.htm)

## See Also

[IBSurfParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData.html)
[IBSurfParamData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData_members.html)
[IBSurfParamData::GetControlPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~GetControlPoints.html)
[IBSurfParamData::IGetControlPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~IGetControlPoints.html)
[IBSurfParamData::ControlPointRowCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~ControlPointRowCount.html)
[IBSurfParamData::UKnots Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~UKnots.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
