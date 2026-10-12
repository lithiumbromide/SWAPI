---
title: "VMax Property (ISurfaceParameterizationData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceParameterizationData"
member: "VMax"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData~VMax.html"
---

# VMax Property (ISurfaceParameterizationData)

Gets the highest value in the V parameter range.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property VMax As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceParameterizationData
Dim value As System.Double

value = instance.VMax
```

### C#

```csharp
System.double VMax {get;}
```

### C++/CLI

```cpp
property System.double VMax {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Highest V parameter value

## VBA Syntax

See [SurfaceParameterizationData::VMax](ms-its:sldworksapivb6.chm::/sldworks~SurfaceParameterizationData~VMax.html).

## Examples

[Get B-Spline Surface Parameterization Data (C#)](Get_B-Spline_Surface_Parameterization_Data_Example_CSharp.htm)
[Get B-Spline Surface Parameterization Data (VB.NET)](Get_B-Spline_Surface_Parameterization_Data_Example_VBNET.htm)
[Get B-Spline Surface Parameterization Data (VBA)](Get_B-Spline_Surface_Parameterization_Data_Example_VB.htm)

## See Also

[ISurfaceParameterizationData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData.html)
[ISurfaceParameterizationData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData_members.html)
[ISurfaceParameterizationData::VMaxBoundType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData~VMaxBoundType.html)
[ISurfaceParameterizationData::VMin Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData~VMin.html)
[ISurfaceParameterizationData::VProperties Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData~VProperties.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
