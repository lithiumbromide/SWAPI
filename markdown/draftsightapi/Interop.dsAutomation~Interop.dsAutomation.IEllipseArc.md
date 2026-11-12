---
title: "IEllipseArc Interface"
project: ""
interface: "IEllipseArc"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEllipseArc.html"
---

# IEllipseArc Interface

Allows access to an Ellipse or an elliptical Arc.

## Syntax

### Visual Basic

```vb
Public Interface IEllipseArc
```

### C#

```csharp
public interface IEllipseArc
```

### JScript

```
public interface IEllipseArc
```

### Managed Extensions for C++

```
public __gc __interface IEllipseArc
```

### C++/CLI

```cpp
public interface class IEllipseArc
```

## Examples

[Construct Ellipses and Elliptical Arcs (C#)](Construct_Ellipses_and_Elliptical_Arcs_Example_CSharp.htm)
[Construct Ellipses and Elliptical Arcs (VB.NET)](Construct_Ellipses_and_Elliptical_Arcs_Example_VBNET.htm)
[Construct Ellipses and Elliptical Arcs (VBA)](Construct_Ellipses_and_Elliptical_Arcs_Example_VBA.htm)

## Remarks

##### COM native C++

If the selected object is an IEllipseArc object, then get the object.

...

//Write number of selected objects to output file
long selCount = dsSelManager->GetSelectedObjectCount( dsSelectionSetType_Current );
strPrint.Format( L"Selected objects: (%d):\r\n", selCount );
fileOutput.WriteString( strPrint );

if( selCount > 0 )
{
for( long i = 0; i < selCount; ++i )
{
//Get selected object type
dsObjectType_e retObjType;
IDispatchPtr selObj = dsSelManager->GetSelectedObject( dsSelectionSetType_Current, i, &retObjType );

//If selected object is an elliptical Arc entity
if(dsEllipseArcType == retObjType )
{
IEllipseArcPtr dsEllipseArc( selObj );

strPrint.Format( L"Elliptical Arc\r\n" );
fileOutput.WriteString( strPrint );

//Do dump for elliptical Arc entity

//See the entity's [Layer](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~Layer.html), [LineScale](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~LineScale.html), [LineStyle](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~LineStyle.html), [LineWeight](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~LineWeight.html),
//or [Visible](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~Visible.html) property for the DumpGraphicsEntity template
CAddinDumpManager::DumpGraphicsEntity<IEllipseArcPtr>( dsEllipseArc, fileOutput );

...

## Accessors

[IDocument::GetObjectByHandle](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetObjectByHandle.html)

[ISelectionManager::GetSelectedObject](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)

[ISelectionManager::GetSelectedObjects](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObjects.html)

[ISketchManager::GetEntities](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~GetEntities.html)

[ISketchManager::InsertEllipseArcDistanceToOtherAxis](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertEllipseArcDistanceToOtherAxis.html)

[ISketchManager::InsertEllipseArcRotation](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertEllipseArcRotation.html)

[ISketchManager::InsertEllipseDistanceToOtherAxis](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertEllipseDistanceToOtherAxis.html)

[ISketchManager::InsertEllipseRotation](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertEllipseRotation.html)

[IViewport::GetClippedObject](Interop.dsAutomation~Interop.dsAutomation.IViewport~GetClippedObject.html)

## Access Diagram

DSObjectModel.pdf#EllipseArc

[EllipseArc](DSObjectModel.pdf#EllipseArc)

## See Also

[IEllipseArc Members](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IRegion Interface](Interop.dsAutomation~Interop.dsAutomation.IRegion.html)
