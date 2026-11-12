---
title: "ICustomData Interface"
project: ""
interface: "ICustomData"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomData.html"
---

# ICustomData Interface

Allows access to custom data.

## Syntax

### Visual Basic

```vb
Public Interface ICustomData
```

### C#

```csharp
public interface ICustomData
```

### JScript

```
public interface ICustomData
```

### Managed Extensions for C++

```
public __gc __interface ICustomData
```

### C++/CLI

```cpp
public interface class ICustomData
```

## Examples

[Add, Modify, and Remove Custom Data (C#)](Add_Modify_Remove_Custom_Data_Example_CSharp.htm)
[Add, Modify, and Remove Custom Data (VB.NET)](Add_Modify_Remove_Custom_Data_Example_VBNET.htm)
[Add, Modify, and Remove Custom Data (VBA)](Add_Modify_Remove_Custom_Data_Example_VBA.htm)
[Add and Modify Custom Data (JavaScript)](Add_and_Modify_Custom_Data_Example_JS.htm)

## Remarks

Custom data is non-graphical information that you can add to an entity in a drawing to supplement the data available via the entity's interface.

Custom data is made up of:

- Markers, which are stored as integers and which help identify the data type of the custom data. Valid values for markers are shown in the following table.
- Data, which are variable data types such as strings, doubles, integers, etc.

| Marker | Data | Data type |
| --- | --- | --- |
| 1000 | Text | String |
| 1003 | Layer name | String |
| 1004 | Binary chunk | Variable-length binary array; maximum of 127 bytes |
| 1005 | Handle of an entity | String |
| 1010 − 1013 | Point | Three numbers |
| 1020 − 1059 | Double | Double |
| 1060 − 1070 | Integer | Signed 16-bit integer, also called Int16 |
| 1071 | Integer | Signed 32-bit integer, also called Int32 |

Custom data is stored in an entity using markers.

Because multiple applications can add custom data to an entity, use unique names to differentiate your custom data from that of other applications. Custom data names are stored in a [drawing document's list of registered applications](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetRegisteredApplications.html), which you can search to determine a unique name for your custom data.

After determining a unique name for your custom data, use an entity's:

- GetCustomData method to create the entity's CustomData object. Use the ICustomData methods to add data to the entity's CustomData object.
- SetCustomData method to change an entity's CustomData object.
- DeleteCustomData method to delete an entity's CustomData object.
- Handle property to get the entity's CustomData object's handle. Because entities can reference other entities by saving the handles of other entities in their custom data, handles do not have to be unique.

## Accessors

[IArcAlignedText::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText~GetCustomData.html)

[IAttributeDefinition::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~GetCustomData.html)

[IAttributeInstance::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~GetCustomData.html)

[IBlockDefinition::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~GetCustomData.html)

[IBlockInstance::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance~GetCustomData.html)

[ICircle::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.ICircle~GetCustomData.html)

[ICircleArc::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.ICircleArc~GetCustomData.html)

[ICustomData::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetCustomData.html)

[ICustomData::InsertCustomData](Interop.dsAutomation~Interop.dsAutomation.ICustomData~InsertCustomData.html)

[IDgnDefinition::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition~GetCustomData.html)

[IDgnReference::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IDgnReference~GetCustomData.html)

[IDictionary::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IDictionary~GetCustomData.html)

[IDimensionStyle::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~GetCustomData.html)

[IEllipseArc::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~GetCustomData.html)

[IEmbeddedObject::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject~GetCustomData.html)

[IEntityHelper::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~GetCustomData.html)

[IExtrudedSurface::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IExtrudedSurface~GetCustomData.html)

[IExtrusion::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IExtrusion~GetCustomData.html)

[IFace::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IFace~GetCustomData.html)

[IGeneralDimension::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension~GetCustomData.html)

[IHatch::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IHatch~GetCustomData.html)

[IImageDefinition::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IImageDefinition~GetCustomData.html)

[IInfiniteLine::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~GetCustomData.html)

[ILayer::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.ILayer~GetCustomData.html)

[ILeader::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.ILeader~GetCustomData.html)

[ILine::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.ILine~GetCustomData.html)

[ILineStyle::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.ILineStyle~GetCustomData.html)

[ILoft::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.ILoft~GetCustomData.html)

[ILoftedSurface::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.ILoftedSurface~GetCustomData.html)

[IModel::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IModel~GetCustomData.html)

[INote::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.INote~GetCustomData.html)

[IPdfDefinition::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IPdfDefinition~GetCustomData.html)

[IPdfReference::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IPdfReference~GetCustomData.html)

[IPoint::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IPoint~GetCustomData.html)

[IPolyFaceMesh::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~GetCustomData.html)

[IPolygonMesh::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh~GetCustomData.html)

[IPolyLine::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetCustomData.html)

[IPolyLine3D::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~GetCustomData.html)

[IRay::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IRay~GetCustomData.html)

[IReferenceImage::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage~GetCustomData.html)

[IRegion::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IRegion~GetCustomData.html)

[IRevolve::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IRevolve~GetCustomData.html)

[IRevolvedSurface::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IRevolvedSurface~GetCustomData.html)

[IRichLine::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IRichLine~GetCustomData.html)

[IRichLineStyle::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~GetCustomData.html)

[IShape::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IShape~GetCustomData.html)

[ISheet::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.ISheet~GetCustomData.html)

[ISimpleNote::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~GetCustomData.html)

[ISolid::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.ISolid~GetCustomData.html)

[ISolid3D::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.ISolid3D~GetCustomData.html)

[ISpline::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.ISpline~GetCustomData.html)

[ISweep::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.ISweep~GetCustomData.html)

[ISweptSurface::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.ISweptSurface~GetCustomData.html)

[ITable::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.ITable~GetCustomData.html)

[ITextStyle::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.ITextStyle~GetCustomData.html)

[ITolerance::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.ITolerance~GetCustomData.html)

[ITrace::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.ITrace~GetCustomData.html)

[IUnknownEntity::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity~GetCustomData.html)

[IViewport::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IViewport~GetCustomData.html)

[IViewTile::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IViewTile~GetCustomData.html)

[IXRecord::GetCustomData](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)

## Access Diagram

DSObjectModel.pdf#CustomData

[CustomData](DSObjectModel.pdf#CustomData)

## See Also

[ICustomData Members](Interop.dsAutomation~Interop.dsAutomation.ICustomData_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IDocument::GetRegisteredApplications Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetRegisteredApplications.html)
