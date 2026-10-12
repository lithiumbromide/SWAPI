---
title: "VMaxBoundType Property (ISurfaceParameterizationData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceParameterizationData"
member: "VMaxBoundType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData~VMaxBoundType.html"
---

# VMaxBoundType Property (ISurfaceParameterizationData)

Gets the behavior at the end of the V range.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property VMaxBoundType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceParameterizationData
Dim value As System.Integer

value = instance.VMaxBoundType
```

### C#

```csharp
System.int VMaxBoundType {get;}
```

### C++/CLI

```cpp
property System.int VMaxBoundType {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of behavior as defined in [swBoundType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBoundType_e.html)

## VBA Syntax

See [SurfaceParameterizationData::VMaxBoundType](ms-its:sldworksapivb6.chm::/sldworks~SurfaceParameterizationData~VMaxBoundType.html).

## Examples

[Get B-Spline Surface Parameterization Data (C#)](Get_B-Spline_Surface_Parameterization_Data_Example_CSharp.htm)
[Get B-Spline Surface Parameterization Data (VB.NET)](Get_B-Spline_Surface_Parameterization_Data_Example_VBNET.htm)
[Get B-Spline Surface Parameterization Data (VBA)](Get_B-Spline_Surface_Parameterization_Data_Example_VB.htm)

## See Also

[ISurfaceParameterizationData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData.html)
[ISurfaceParameterizationData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData_members.html)
[ISurfaceParameterizationData::VMax Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData~VMax.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
