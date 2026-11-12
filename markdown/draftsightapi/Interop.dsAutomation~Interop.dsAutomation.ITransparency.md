---
title: "ITransparency Interface"
project: ""
interface: "ITransparency"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITransparency.html"
---

# ITransparency Interface

Allows access to transparency of entities on Layers.

## Syntax

### Visual Basic

```vb
Public Interface ITransparency
```

### C#

```csharp
public interface ITransparency
```

### JScript

```
public interface ITransparency
```

### Managed Extensions for C++

```
public __gc __interface ITransparency
```

### C++/CLI

```cpp
public interface class ITransparency
```

## Examples

[Create Table (C#)](Create_Table_Example_CSharp.htm)
[Create Table (VB.NET)](Create_Table_Example_VBNET.htm)
[Create Table (VBA)](Create_Table_Example_VBA.htm)
[Create Table (JavaScript)](Create_Table_Example_JS.htm)

## Remarks

To change the transparency of an entity:

1. Get the entity's transparency object using either [IEntityHelper::GetTransparency](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~GetTransparency.html) or the entity's Transparency property.
2. Determine if the entity's transparency object is by an alpha value, **ByBlock**, or **ByLayer** by calling one of the following methods:

  - [ITransparency::IsByAlpha](Interop.dsAutomation~Interop.dsAutomation.ITransparency~IsByAlpha.html)
  - [ITransparency::IsByBlock](Interop.dsAutomation~Interop.dsAutomation.ITransparency~IsByBlock.html)
  - [ITransparency::IsByLayer](Interop.dsAutomation~Interop.dsAutomation.ITransparency~IsByLayer.html)
3. Call one of the following methods to change the transparency of that instance of the transparency object:

  - [ITransparency::SetByAlpha](Interop.dsAutomation~Interop.dsAutomation.ITransparency~SetByAlpha.html)
  - [ITransparency::SetByBlock](Interop.dsAutomation~Interop.dsAutomation.ITransparency~SetByBlock.html)
  - [ITransparency::SetByLayer](Interop.dsAutomation~Interop.dsAutomation.ITransparency~SetByLayer.html)
4. Update the entity's transparency object using either [IEntityHelper::SetTransparency](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~SetTransparency.html) or the entity's Transparency property.

## Accessors

[IAttributeDefinition::Transparency](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~Transparency.html)

[IAttributeInstance::Transparency](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~Transparency.html)

[IBlockInstance::Transparency](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance~Transparency.html)

[ICircle::Transparency](Interop.dsAutomation~Interop.dsAutomation.ICircle~Transparency.html)

[ICircleArc::Transparency](Interop.dsAutomation~Interop.dsAutomation.ICircleArc~Transparency.html)

[IDgnReference::Transparency](Interop.dsAutomation~Interop.dsAutomation.IDgnReference~Transparency.html)

[IEllipseArc::Transparency](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~Transparency.html)

[IEmbeddedObject::Transparency](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject~Transparency.html)

[IEntityHelper::GetTransparency](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~GetTransparency.html)

[IExtrudedSurface::Transparency](Interop.dsAutomation~Interop.dsAutomation.IExtrudedSurface~Transparency.html)

[IExtrusion::Transparency](Interop.dsAutomation~Interop.dsAutomation.IExtrusion~Transparency.html)

[IFace::Transparency](Interop.dsAutomation~Interop.dsAutomation.IFace~Transparency.html)

[IGeneralDimension::Transparency](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension~Transparency.html)

[IHatch::Transparency](Interop.dsAutomation~Interop.dsAutomation.IHatch~Transparency.html)

[IInfiniteLine::Transparency](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~Transparency.html)

[ILayerProperties::Transparency](Interop.dsAutomation~Interop.dsAutomation.ILayerProperties~Transparency.html)

[ILeader::Transparency](Interop.dsAutomation~Interop.dsAutomation.ILeader~Transparency.html)

[ILine::Transparency](Interop.dsAutomation~Interop.dsAutomation.ILine~Transparency.html)

[ILoft::Transparency](Interop.dsAutomation~Interop.dsAutomation.ILoft~Transparency.html)

[ILoftedSurface::Transparency](Interop.dsAutomation~Interop.dsAutomation.ILoftedSurface~Transparency.html)

[INote::Transparency](Interop.dsAutomation~Interop.dsAutomation.INote~Transparency.html)

[IPdfReference::Transparency](Interop.dsAutomation~Interop.dsAutomation.IPdfReference~Transparency.html)

[IPoint::Transparency](Interop.dsAutomation~Interop.dsAutomation.IPoint~Transparency.html)

[IPolyFaceMesh::Transparency](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~Transparency.html)

[IPolygonMesh::Transparency](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh~Transparency.html)

[IPolyLine::Transparency](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Transparency.html)

[IPolyLine3D::Transparency](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~Transparency.html)

[IRay::Transparency](Interop.dsAutomation~Interop.dsAutomation.IRay~Transparency.html)

[IRegion::Transparency](Interop.dsAutomation~Interop.dsAutomation.IRegion~Transparency.html)

[IRevolve::Transparency](Interop.dsAutomation~Interop.dsAutomation.IRevolve~Transparency.html)

[IRevolvedSurface::Transparency](Interop.dsAutomation~Interop.dsAutomation.IRevolvedSurface~Transparency.html)

[IRichLine::Transparency](Interop.dsAutomation~Interop.dsAutomation.IRichLine~Transparency.html)

[IShape::Transparency](Interop.dsAutomation~Interop.dsAutomation.IShape~Transparency.html)

[ISimpleNote::Transparency](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~Transparency.html)

[ISolid::Transparency](Interop.dsAutomation~Interop.dsAutomation.ISolid~Transparency.html)

[ISolid3D::Transparency](Interop.dsAutomation~Interop.dsAutomation.ISolid3D~Transparency.html)

[ISpline::Transparency](Interop.dsAutomation~Interop.dsAutomation.ISpline~Transparency.html)

[ISweep::Transparency](Interop.dsAutomation~Interop.dsAutomation.ISweep~Transparency.html)

[ISweptSurface::Transparency](Interop.dsAutomation~Interop.dsAutomation.ISweptSurface~Transparency.html)

[ITable::Transparency](Interop.dsAutomation~Interop.dsAutomation.ITable~Transparency.html)

[ITolerance::Transparency](Interop.dsAutomation~Interop.dsAutomation.ITolerance~Transparency.html)

[ITrace::Transparency](Interop.dsAutomation~Interop.dsAutomation.ITrace~Transparency.html)

[IUnknownEntity::Transparency](Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity~Transparency.html)

[IViewport::Transparency](Interop.dsAutomation~Interop.dsAutomation.IViewport~Transparency.html)

## Access Diagram

DSObjectModel.pdf#Transparency

[Transparency](DSObjectModel.pdf#Transparency)

## See Also

[ITransparency Members](Interop.dsAutomation~Interop.dsAutomation.ITransparency_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
