---
title: "VPropertyNumber Property (ISurfaceParameterizationData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceParameterizationData"
member: "VPropertyNumber"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData~VPropertyNumber.html"
---

# VPropertyNumber Property (ISurfaceParameterizationData)

Gets the number of V properties.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property VPropertyNumber As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceParameterizationData
Dim value As System.Integer

value = instance.VPropertyNumber
```

### C#

```csharp
System.int VPropertyNumber {get;}
```

### C++/CLI

```cpp
property System.int VPropertyNumber {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of properties returned by [ISurfaceParameterizationData::VProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceParameterizationData~VProperties.html)

## VBA Syntax

See [SurfaceParameterizationData::VPropertyNumber](ms-its:sldworksapivb6.chm::/sldworks~SurfaceParameterizationData~VPropertyNumber.html).

## Examples

[Get B-Spline Surface Parameterization Data (C#)](Get_B-Spline_Surface_Parameterization_Data_Example_CSharp.htm)
[Get B-Spline Surface Parameterization Data (VB.NET)](Get_B-Spline_Surface_Parameterization_Data_Example_VBNET.htm)
[Get B-Spline Surface Parameterization Data (VBA)](Get_B-Spline_Surface_Parameterization_Data_Example_VB.htm)

## See Also

[ISurfaceParameterizationData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData.html)
[ISurfaceParameterizationData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
