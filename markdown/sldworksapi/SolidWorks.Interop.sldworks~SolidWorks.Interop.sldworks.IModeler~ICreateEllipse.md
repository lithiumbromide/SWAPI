---
title: "ICreateEllipse Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ICreateEllipse"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateEllipse.html"
---

# ICreateEllipse Method (IModeler)

Creates a temporary elliptical curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateEllipse( _
   ByRef Center As System.Double, _
   ByVal MajorRadius As System.Double, _
   ByVal MinorRadius As System.Double, _
   ByRef MajorAxis As System.Double, _
   ByRef MinorAxis As System.Double _
) As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim Center As System.Double
Dim MajorRadius As System.Double
Dim MinorRadius As System.Double
Dim MajorAxis As System.Double
Dim MinorAxis As System.Double
Dim value As Curve

value = instance.ICreateEllipse(Center, MajorRadius, MinorRadius, MajorAxis, MinorAxis)
```

### C#

```csharp
Curve ICreateEllipse(
   ref System.double Center,
   System.double MajorRadius,
   System.double MinorRadius,
   ref System.double MajorAxis,
   ref System.double MinorAxis
)
```

### C++/CLI

```cpp
Curve^ ICreateEllipse(
   System.double% Center,
   System.double MajorRadius,
   System.double MinorRadius,
   System.double% MajorAxis,
   System.double% MinorAxis
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Center`: - in-process, unmanaged C++: Pointer to an array of 3 doubles describing the location of the center of the ellipse

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `MajorRadius`: Major radius of ellipse
- `MinorRadius`: Minor radius of ellipse
- `MajorAxis`: - in-process, unmanaged C++: Pointer to an array of 3 doubles describing the major axis of the ellipse

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `MinorAxis`: - in-process, unmanaged C++: Pointer to an array of 3 doubles describing the minor axis of the ellipse
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

[Curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::CreateEllipse Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateEllipse.html)
[IModeler::CreateArc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateArc.html)
[IModeler::ICreateArc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateArc.html)
[IModeler::CreateLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateLine.html)
[IModeler::ICreateLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateLine.html)
[IModeler::CreateExtrudedBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateExtrudedBody.html)

## Availability

SOLIDWORKS 2012 SP01, Revision Number 20.1
