---
title: "UMax Property (ISurfaceParameterizationData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceParameterizationData"
member: "UMax"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData~UMax.html"
---

# UMax Property (ISurfaceParameterizationData)

Gets the highest value in the U parameter range.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property UMax As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceParameterizationData
Dim value As System.Double

value = instance.UMax
```

### C#

```csharp
System.double UMax {get;}
```

### C++/CLI

```cpp
property System.double UMax {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Highest U parameter value

## VBA Syntax

See [SurfaceParameterizationData::UMax](ms-its:sldworksapivb6.chm::/sldworks~SurfaceParameterizationData~UMax.html).

## Examples

[Get B-Spline Surface Parameterization Data (C#)](Get_B-Spline_Surface_Parameterization_Data_Example_CSharp.htm)
[Get B-Spline Surface Parameterization Data (VB.NET)](Get_B-Spline_Surface_Parameterization_Data_Example_VBNET.htm)
[Get B-Spline Surface Parameterization Data (VBA)](Get_B-Spline_Surface_Parameterization_Data_Example_VB.htm)

## See Also

[ISurfaceParameterizationData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData.html)
[ISurfaceParameterizationData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData_members.html)
[ISurfaceParameterizationData::UMaxBoundType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData~UMaxBoundType.html)
[ISurfaceParameterizationData::UMin Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData~UMin.html)
[ISurfaceParameterization::UProperties Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData~UProperties.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
