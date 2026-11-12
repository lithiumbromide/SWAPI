---
title: "CreateTransformRotateAxis Method (IMathUtility)"
project: "SOLIDWORKS API Help"
interface: "IMathUtility"
member: "CreateTransformRotateAxis"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~CreateTransformRotateAxis.html"
---

# CreateTransformRotateAxis Method (IMathUtility)

Creates a new math transform matrix that represents the rotation by an angle about a vector positioned at a point.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateTransformRotateAxis( _
   ByVal PointObjIn As System.Object, _
   ByVal VectorObjIn As System.Object, _
   ByVal Angle As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMathUtility
Dim PointObjIn As System.Object
Dim VectorObjIn As System.Object
Dim Angle As System.Double
Dim value As System.Object

value = instance.CreateTransformRotateAxis(PointObjIn, VectorObjIn, Angle)
```

### C#

```csharp
System.object CreateTransformRotateAxis(
   System.object PointObjIn,
   System.object VectorObjIn,
   System.double Angle
)
```

### C++/CLI

```cpp
System.Object^ CreateTransformRotateAxis(
   System.Object^ PointObjIn,
   System.Object^ VectorObjIn,
   System.double Angle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PointObjIn`: Center [point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html) of the axis of the transform
- `VectorObjIn`: Axis [vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) of the transform
- `Angle`: Angle of rotation about the X axis vector

### Return Value

Newly created [math transform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html) or null or nothing if the operation fails

## VBA Syntax

See [MathUtility::CreateTransformRotateAxis](ms-its:sldworksapivb6.chm::/sldworks~MathUtility~CreateTransformRotateAxis.html).

## Examples

[Rotate Assembly Component on Axis Using IDragOperator::Drag (VBA)](Rotate_Assembly_Component_on_Axis_Example_VB.htm)
[Rotate Assembly Component on Axis Using IDragOperator::Drag (VB.NET)](Rotate_Assembly_Component_on_Axis_Example_VBNET.htm)
[Rotate Assembly Component on Axis Using IDragOperator::Drag (C#)](Rotate_Assembly_Component_on_Axis_Example_CSharp.htm)
[Rotate Assembly Component on Axis Using IDragOperator::DragAsUI (VBA)](Rotate_Assembly_Component_on_Axis_Example2_VB.htm)
[Rotate Assembly Component on Axis Using IDragOperator::DragAsUI (VB.NET)](Rotate_Assembly_Component_on_Axis_Example2_VBNET.htm)
[Rotate Assembly Component on Axis Using IDragOperator::DragAsUI (C#)](Rotate_Assembly_Component_on_Axis_Example2_CSharp.htm)

## See Also

[IMathUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility.html)
[IMathUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility_members.html)
[IMathUtility::ComposeTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~ComposeTransform.html)
[IMathUtility::CreateTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~CreateTransform.html)
[IMathUtility::ICreateTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~ICreateTransform.html)
[IMathUtility::ICreateTransformRotateAxis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~ICreateTransformRotateAxis.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
