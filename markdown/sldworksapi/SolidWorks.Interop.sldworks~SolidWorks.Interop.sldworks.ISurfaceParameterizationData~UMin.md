---
title: "UMin Property (ISurfaceParameterizationData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceParameterizationData"
member: "UMin"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData~UMin.html"
---

# UMin Property (ISurfaceParameterizationData)

Gets the lowest value in the U parameter range.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property UMin As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceParameterizationData
Dim value As System.Double

value = instance.UMin
```

### C#

```csharp
System.double UMin {get;}
```

### C++/CLI

```cpp
property System.double UMin {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Lowest U parameter value

## VBA Syntax

See [SurfaceParameterizationData::UMin](ms-its:sldworksapivb6.chm::/sldworks~SurfaceParameterizationData~UMin.html).

## Examples

[Get B-Spline Surface Parameterization Data (C#)](Get_B-Spline_Surface_Parameterization_Data_Example_CSharp.htm)
[Get B-Spline Surface Parameterization Data (VB.NET)](Get_B-Spline_Surface_Parameterization_Data_Example_VBNET.htm)
[Get B-Spline Surface Parameterization Data (VBA)](Get_B-Spline_Surface_Parameterization_Data_Example_VB.htm)

## See Also

[ISurfaceParameterizationData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData.html)
[ISurfaceParameterizationData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData_members.html)
[ISurfaceParameterizationData::UMinBoundType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData~UMinBoundType.html)
[ISurfaceParameterizationData::UProperties Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData~UProperties.html)
[ISurfaceParameterizationData::UMax Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData~UMax.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
