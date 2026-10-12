---
title: "UMinBoundType Property (ISurfaceParameterizationData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceParameterizationData"
member: "UMinBoundType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData~UMinBoundType.html"
---

# UMinBoundType Property (ISurfaceParameterizationData)

Gets the behavior at the start of the U range.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property UMinBoundType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceParameterizationData
Dim value As System.Integer

value = instance.UMinBoundType
```

### C#

```csharp
System.int UMinBoundType {get;}
```

### C++/CLI

```cpp
property System.int UMinBoundType {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of behavior as defined in [swBoundType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBoundType_e.html)

## VBA Syntax

See [SurfaceParameterizationData::UMinBoundType](ms-its:sldworksapivb6.chm::/sldworks~SurfaceParameterizationData~UMinBoundType.html).

## Examples

[Get B-Spline Surface Parameterization Data (C#)](Get_B-Spline_Surface_Parameterization_Data_Example_CSharp.htm)
[Get B-Spline Surface Parameterization Data (VB.NET)](Get_B-Spline_Surface_Parameterization_Data_Example_VBNET.htm)
[Get B-Spline Surface Parameterization Data (VBA)](Get_B-Spline_Surface_Parameterization_Data_Example_VB.htm)

## See Also

[ISurfaceParameterizationData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData.html)
[ISurfaceParameterizationData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData_members.html)
[ISurfaceParameterizationData::UMin Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData~UMin.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
