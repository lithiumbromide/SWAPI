---
title: "ISurfaceParameterizationData Interface"
project: "SOLIDWORKS API Help"
interface: "ISurfaceParameterizationData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData.html"
---

# ISurfaceParameterizationData Interface

Allows access to the parameterization data of a surface.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISurfaceParameterizationData
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceParameterizationData
```

### C#

```csharp
public interface ISurfaceParameterizationData
```

### C++/CLI

```cpp
public interface class ISurfaceParameterizationData
```

## VBA Syntax

See [SurfaceParameterizationData](ms-its:sldworksapivb6.chm::/sldworks~SurfaceParameterizationData.html).

## Examples

[Get B-Spline Surface Parameterization Data (C#)](Get_B-Spline_Surface_Parameterization_Data_Example_CSharp.htm)
[Get B-Spline Surface Parameterization Data (VB.NET)](Get_B-Spline_Surface_Parameterization_Data_Example_VBNET.htm)
[Get B-Spline Surface Parameterization Data (VBA)](Get_B-Spline_Surface_Parameterization_Data_Example_VB.htm)

## Remarks

If a surface is periodic in one direction (cylinder, cone, torus, sphere), then U is the periodic direction.

The -10000 to 10000 parameter range is the modeling limit for the modeler. This means that the values are effectively infinite in size. To get the parameter range from a given face, use [IFace2::GetBox](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetBox.html) or [IFace2::IGetBox](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetBox.html), [ISurface::GetClosestPointOn](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~GetClosestPointOn.html) or [ISurface::IGetClosestPointOn](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~IGetClosestPointOn.html), and [ISurface::ReverseEvaluate](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~ReverseEvaluate.html) or [ISurface::IReverseEvaluate](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~IReverseEvaluate.html). These methods provide a true parameter range that the face is using on the surface.

## Accessors

[ISurface::Parameterization2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~Parameterization2.html)

## Access Diagram

[SurfaceParameterizationData](SWObjectModel.pdf#SurfaceParameterizationData)

## See Also

[ISurfaceParameterizationData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IBSurfParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData.html)
[ISurface::GetBSurfParams3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetBSurfParams3.html)
