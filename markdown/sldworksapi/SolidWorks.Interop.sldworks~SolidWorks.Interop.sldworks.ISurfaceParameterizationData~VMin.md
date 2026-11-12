---
title: "VMin Property (ISurfaceParameterizationData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceParameterizationData"
member: "VMin"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData~VMin.html"
---

# VMin Property (ISurfaceParameterizationData)

Gets the lowest value in the V parameter range.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property VMin As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceParameterizationData
Dim value As System.Double

value = instance.VMin
```

### C#

```csharp
System.double VMin {get;}
```

### C++/CLI

```cpp
property System.double VMin {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Lowest V parameter value

## VBA Syntax

See [SurfaceParameterizationData::VMin](ms-its:sldworksapivb6.chm::/sldworks~SurfaceParameterizationData~VMin.html).

## Examples

[Get B-Spline Surface Parameterization Data (C#)](Get_B-Spline_Surface_Parameterization_Data_Example_CSharp.htm)
[Get B-Spline Surface Parameterization Data (VB.NET)](Get_B-Spline_Surface_Parameterization_Data_Example_VBNET.htm)
[Get B-Spline Surface Parameterization Data (VBA)](Get_B-Spline_Surface_Parameterization_Data_Example_VB.htm)

## See Also

[ISurfaceParameterizationData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData.html)
[ISurfaceParameterizationData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData_members.html)
[ISurfaceParameterizationData::VMinBoundType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData~VMinBoundType.html)
[ISurfaceParameterizationData::VMax Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData~VMax.html)
[ISurfaceParameterizationData::VProperties Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData~VProperties.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
