---
title: "UPropertyNumber Property (ISurfaceParameterizationData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceParameterizationData"
member: "UPropertyNumber"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData~UPropertyNumber.html"
---

# UPropertyNumber Property (ISurfaceParameterizationData)

Gets the number of U properties.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property UPropertyNumber As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceParameterizationData
Dim value As System.Integer

value = instance.UPropertyNumber
```

### C#

```csharp
System.int UPropertyNumber {get;}
```

### C++/CLI

```cpp
property System.int UPropertyNumber {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of properties returned by [ISurfaceParameterizationData::UProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceParameterizationData~UProperties.html)

## VBA Syntax

See [SurfaceParameterizationData::UPropertyNumber](ms-its:sldworksapivb6.chm::/sldworks~SurfaceParameterizationData~UPropertyNumber.html).

## Examples

[Get B-Spline Surface Parameterization Data (C#)](Get_B-Spline_Surface_Parameterization_Data_Example_CSharp.htm)
[Get B-Spline Surface Parameterization Data (VB.NET)](Get_B-Spline_Surface_Parameterization_Data_Example_VBNET.htm)
[Get B-Spline Surface Parameterization Data (VBA)](Get_B-Spline_Surface_Parameterization_Data_Example_VB.htm)

## See Also

[ISurfaceParameterizationData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData.html)
[ISurfaceParameterizationData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
