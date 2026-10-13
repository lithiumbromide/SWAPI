---
title: "CreateEllipse Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "CreateEllipse"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateEllipse.html"
---

# CreateEllipse Method (IModeler)

Creates a temporary elliptical curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateEllipse( _
   ByVal Center As System.Object, _
   ByVal MajorRadius As System.Double, _
   ByVal MinorRadius As System.Double, _
   ByVal MajorAxis As System.Object, _
   ByVal MinorAxis As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim Center As System.Object
Dim MajorRadius As System.Double
Dim MinorRadius As System.Double
Dim MajorAxis As System.Object
Dim MinorAxis As System.Object
Dim value As System.Object

value = instance.CreateEllipse(Center, MajorRadius, MinorRadius, MajorAxis, MinorAxis)
```

### C#

```csharp
System.object CreateEllipse(
   System.object Center,
   System.double MajorRadius,
   System.double MinorRadius,
   System.object MajorAxis,
   System.object MinorAxis
)
```

### C++/CLI

```cpp
System.Object^ CreateEllipse(
   System.Object^ Center,
   System.double MajorRadius,
   System.double MinorRadius,
   System.Object^ MajorAxis,
   System.Object^ MinorAxis
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Center`: Array of 3 doubles describing the center of the ellipse
- `MajorRadius`: Major radius of ellipse
- `MinorRadius`: Minor radius of ellipse
- `MajorAxis`: Array of 3 doubles describing the major axis of the ellipse
- `MinorAxis`: Array of 3 doubles describing the minor axis of the ellipse

### Return Value

[Curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)

## VBA Syntax

See [Modeler::CreateEllipse](ms-its:sldworksapivb6.chm::/sldworks~Modeler~CreateEllipse.html).

## Examples

[Create Temporary Elliptical Extrusion (VBA)](Create_Temporary_Elliptical_Extrusion_Example_VB.htm)
[Create Temporary Elliptical Extrusion (VB.NET)](Create_Temporary_Elliptical_Extrusion_VBNET.htm)
[Create Temporary Elliptical Extrusion (C#)](Create_Temporary_Elliptical_Extrusion_CSharp.htm)

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::CreateArc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateArc.html)
[IModeler::ICreateArc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateArc.html)
[IModeler::CreateLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateLine.html)
[IModeler::ICreateLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateLine.html)
[IModeler::ICreateEllipse Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateEllipse.html)
[IModeler::CreateExtrudedBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateExtrudedBody.html)

## Availability

SOLIDWORKS 2012 SP01, Revision Number 20.1
