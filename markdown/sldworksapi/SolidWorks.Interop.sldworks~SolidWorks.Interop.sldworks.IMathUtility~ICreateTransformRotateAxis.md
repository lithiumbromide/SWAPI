---
title: "ICreateTransformRotateAxis Method (IMathUtility)"
project: "SOLIDWORKS API Help"
interface: "IMathUtility"
member: "ICreateTransformRotateAxis"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~ICreateTransformRotateAxis.html"
---

# ICreateTransformRotateAxis Method (IMathUtility)

Creates a new math transform matrix that represents the rotation by an angle about a vector positioned at a point.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateTransformRotateAxis( _
   ByVal PointObjIn As MathPoint, _
   ByVal VectorObjIn As MathVector, _
   ByVal Angle As System.Double _
) As MathTransform
```

### Visual Basic (Usage)

```vb
Dim instance As IMathUtility
Dim PointObjIn As MathPoint
Dim VectorObjIn As MathVector
Dim Angle As System.Double
Dim value As MathTransform

value = instance.ICreateTransformRotateAxis(PointObjIn, VectorObjIn, Angle)
```

### C#

```csharp
MathTransform ICreateTransformRotateAxis(
   MathPoint PointObjIn,
   MathVector VectorObjIn,
   System.double Angle
)
```

### C++/CLI

```cpp
MathTransform^ ICreateTransformRotateAxis(
   MathPoint^ PointObjIn,
   MathVector^ VectorObjIn,
   System.double Angle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PointObjIn`: Center [point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html) of the axis of the transform
- `VectorObjIn`: Axis [vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) of the transform
- `Angle`: Angle of rotation about the X axis vector

### Return Value

Newly created [math transform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html) or NULL if the operation fails

## VBA Syntax

See [MathUtility::ICreateTransformRotateAxis](ms-its:sldworksapivb6.chm::/sldworks~MathUtility~ICreateTransformRotateAxis.html).

## See Also

[IMathUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility.html)
[IMathUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility_members.html)
[IMathUtility::CreateTransformRotateAxis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~CreateTransformRotateAxis.html)
[IMathUtility::ComposeTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~ComposeTransform.html)
[IMathUtility::CreateTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~CreateTransform.html)
[IMathUtility::ICreateTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~ICreateTransform.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
