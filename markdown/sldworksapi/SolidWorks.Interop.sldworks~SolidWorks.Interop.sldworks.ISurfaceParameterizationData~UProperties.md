---
title: "UProperties Property (ISurfaceParameterizationData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceParameterizationData"
member: "UProperties"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData~UProperties.html"
---

# UProperties Property (ISurfaceParameterizationData)

Gets the U parameterization properties.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property UProperties As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceParameterizationData
Dim value As System.Object

value = instance.UProperties
```

### C#

```csharp
System.object UProperties {get;}
```

### C++/CLI

```cpp
property System.Object^ UProperties {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of properties as defined in [swParameterizationPropertyType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swParameterizationPropertyType_e.html)

## VBA Syntax

See [SurfaceParameterizationData::UProperties](ms-its:sldworksapivb6.chm::/sldworks~SurfaceParameterizationData~UProperties.html).

## Examples

[Get B-Spline Surface Parameterization Data (C#)](Get_B-Spline_Surface_Parameterization_Data_Example_CSharp.htm)
[Get B-Spline Surface Parameterization Data (VB.NET)](Get_B-Spline_Surface_Parameterization_Data_Example_VBNET.htm)
[Get B-Spline Surface Parameterization Data (VBA)](Get_B-Spline_Surface_Parameterization_Data_Example_VB.htm)

## See Also

[ISurfaceParameterizationData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData.html)
[ISurfaceParameterizationData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData_members.html)
[ISurfaceParameterizationData::UPropertyNumber Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData~UPropertyNumber.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
