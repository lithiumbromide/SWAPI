---
title: "IRefPlaneFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "IRefPlaneFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.html"
---

# IRefPlaneFeatureData Interface

Allows access to reference plane feature data.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IRefPlaneFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As IRefPlaneFeatureData
```

### C#

```csharp
public interface IRefPlaneFeatureData
```

### C++/CLI

```cpp
public interface class IRefPlaneFeatureData
```

## VBA Syntax

See [RefPlaneFeatureData](ms-its:sldworksapivb6.chm::/sldworks~RefPlaneFeatureData.html).

## Examples

[Insert Reference Plane (VBA)](Insert_Reference_Plane_Example_VB.htm)
[Insert Reference Plane (VB.NET)](Insert_Reference_Plane_Example_VBNET.htm)
[Insert Reference Plane (C#)](Insert_Reference_Plane_Example_CSharp.htm)

## Remarks

Before calling any of the methods and properties on this interface, you should determine the reference plane's type because some IRefPlaneFeatureData methods and properties only work with constraint-based reference planes and some only work with non-constrained reference planes. Use [IRefPlaneFeatureData::Type2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlaneFeatureData~Type2.html) to determine the type of reference plane.

If IRefPlaneFeatureData::Type2 returns swRefPlaneConstraintBase, then the reference plane is constraint based. To determine if a constraint-based reference plane has angle or offset distances references, call [IRefPlaneFeatureData::Type](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlaneFeatureData~Type.html):

- swRefPlaneAngle is returned for angle references.
- swRefPlaneDistance is returned for offset distance references.

Otherwise, the reference plane is not constraint based. Call [IRefPlaneFeatureData::Type](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlaneFeatureData~Type.html) to determine its type.

**NOTE:** Reference planes created in SOLIDWORKS 2010 or later are constraint based; reference planes created in SOLIDWORKS 2009 or earlier are not.

The following table shows which IRefPlaneFeatureData methods and properties to use with which types of reference planes.

| Method or property | Constraint-based | Constraint-based with angle or offset distance references | Not constraint-based |
| --- | --- | --- | --- |
| AccessSelections | ? | ? | ? |
| GetSelectionsCount | ? | ? | ? |
| IAccessSelections | ? | ? | ? |
| IGetSelections | ? | ? | ? |
| ISetSelections | X | ? | ? |
| ReleaseSelectionAccess | ? | ? | ? |
| Angle | X | ? | ? |
| AngleOrDistance | ? | ? | X |
| AutoSize | X | ? | ? |
| Constraint | ? | ? | X |
| Distance | X | ? | ? |
| OriginOnCurve | X | ? | ? |
| ProjectionType | X | ? | ? |
| Reference | ? | ? | X |
| ReverseDirection | X | ? | ? |
| Selections | ? (get only) | ? | ? |
| SolutionIndex | X | ? | ? |
| Type | X | ? | ? |
| Type2 | ? | ? | X |
| UseNormalPlane | X | ? | ? |

? = Yes
X = No

## Accessors

[IFeature::GetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetDefinition.html) and [IFeature::IGetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetDefinition.html)

## Access Diagram

[RefPlaneFeatureData](SWObjectModel.pdf#RefPlaneFeatureData)

## See Also

[IRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IRefPlane Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html)
