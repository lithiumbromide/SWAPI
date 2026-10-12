---
title: "InsertRefPlane Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertRefPlane"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertRefPlane.html"
---

# InsertRefPlane Method (IFeatureManager)

Inserts a constraint-based reference plane using the selected reference entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertRefPlane( _
   ByVal FirstConstraint As System.Integer, _
   ByVal FirstConstraintAngleOrDistance As System.Double, _
   ByVal SecondConstraint As System.Integer, _
   ByVal SecondConstraintAngleOrDistance As System.Double, _
   ByVal ThirdConstraint As System.Integer, _
   ByVal ThirdConstraintAngleOrDistance As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim FirstConstraint As System.Integer
Dim FirstConstraintAngleOrDistance As System.Double
Dim SecondConstraint As System.Integer
Dim SecondConstraintAngleOrDistance As System.Double
Dim ThirdConstraint As System.Integer
Dim ThirdConstraintAngleOrDistance As System.Double
Dim value As System.Object

value = instance.InsertRefPlane(FirstConstraint, FirstConstraintAngleOrDistance, SecondConstraint, SecondConstraintAngleOrDistance, ThirdConstraint, ThirdConstraintAngleOrDistance)
```

### C#

```csharp
System.object InsertRefPlane(
   System.int FirstConstraint,
   System.double FirstConstraintAngleOrDistance,
   System.int SecondConstraint,
   System.double SecondConstraintAngleOrDistance,
   System.int ThirdConstraint,
   System.double ThirdConstraintAngleOrDistance
)
```

### C++/CLI

```cpp
System.Object^ InsertRefPlane(
   System.int FirstConstraint,
   System.double FirstConstraintAngleOrDistance,
   System.int SecondConstraint,
   System.double SecondConstraintAngleOrDistance,
   System.int ThirdConstraint,
   System.double ThirdConstraintAngleOrDistance
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FirstConstraint`: First constraint as defined in [swRefPlaneReferenceConstraints_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRefPlaneReferenceConstraints_e.html)
- `FirstConstraintAngleOrDistance`: Angle or distance of the first constraint
- `SecondConstraint`: Second constraint as defined in [swRefPlaneReferenceConstraints_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRefPlaneReferenceConstraints_e.html)
- `SecondConstraintAngleOrDistance`: Angle or distance of the second constraint
- `ThirdConstraint`: Third constraint as defined in [swRefPlaneReferenceConstraints_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRefPlaneReferenceConstraints_e.html)
- `ThirdConstraintAngleOrDistance`: Angle or distance of the third constraint

### Return Value

[Reference plane](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlane.html)

## VBA Syntax

See [FeatureManager::InsertRefPlane](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertRefPlane.html).

## Examples

[Insert Reference Plane (C#)](Insert_Reference_Plane_Example_CSharp.htm)
[Insert Reference Plane (VB.NET)](Insert_Reference_Plane_Example_VBNET.htm)
[Insert Reference Plane (VBA)](Insert_Reference_Plane_Example_VB.htm)
[Insert Fill-surface Feature (C#)](Insert_Fill-surface_Feature_Example_CSharp.htm)
[Insert Fill-surface Feature (VB.NET)](Insert_Fill-surface_Feature_Example_VBNET.htm)
[Insert Fill-surface Feature (VBA)](Insert_Fill-surface_Feature_Example_VB.htm)

## Remarks

Before calling this method, you must have selected the reference entities using these marks with [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html):

- 0 = First reference entity
- 1 = Second reference entity
- 2 = Third reference entity

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IRefPlane Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html)
[IRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
