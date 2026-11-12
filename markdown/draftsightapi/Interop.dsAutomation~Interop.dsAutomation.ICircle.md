---
title: "ICircle Interface"
project: ""
interface: "ICircle"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICircle.html"
---

# ICircle Interface

Allows access to a Circle.

## Syntax

### Visual Basic

```vb
Public Interface ICircle
```

### C#

```csharp
public interface ICircle
```

### JScript

```
public interface ICircle
```

### Managed Extensions for C++

```
public __gc __interface ICircle
```

### C++/CLI

```cpp
public interface class ICircle
```

## Examples

##### COM native C++

If the selected object is an ICircle object, then get the object.

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

//If selected object is Circle entity
if(dsCircleType == retObjType )
{
ICirclePtr dsCircle( selObj );

strPrint.Format( L"Circle\r\n" );
fileOutput.WriteString( strPrint );

//Do dump for Circle entity

//See the entity's [Layer](Interop.dsAutomation~Interop.dsAutomation.ICircle~Layer.html), [LineScale](Interop.dsAutomation~Interop.dsAutomation.ICircle~LineScale.html), [LineStyle](Interop.dsAutomation~Interop.dsAutomation.ICircle~LineStyle.html), [LineWeight](Interop.dsAutomation~Interop.dsAutomation.ICircle~LineWeight.html),
//or [Visible](Interop.dsAutomation~Interop.dsAutomation.ICircle~Visible.html) property for the DumpGraphicsEntity template
CAddinDumpManager::DumpGraphicsEntity<ICirclePtr>( dsCircle, fileOutput );

...

## Examples

[Construct Circle (C#)](Construct_Circle_Example_CSharp.htm)
[Construct Circle (VB.NET)](Construct_Circle_Example_VBNET.htm)
[Construct Circle (VBA)](Construct_Circle_Example_VBA.htm)
[Add, Modify, and Remove Custom Data (C#)](Add_Modify_Remove_Custom_Data_Example_CSharp.htm)
[Add, Modify, and Remove Custom Data (VB.NET)](Add_Modify_Remove_Custom_Data_Example_VBNET.htm)
[Add, Modify, and Remove Custom Data (VBA)](Add_Modify_Remove_Custom_Data_Example_VBA.htm)
[Create Linear Pattern (C#)](Create_Linear_Pattern_Example_CSharp.htm)
[Create Linear Pattern (VB.NET)](Create_Linear_Pattern_Example_VBNET.htm)
[Create Linear Pattern (VBA)](Create_Linear_Pattern_Example_VBA.htm)
[Create Circles on Different Layers (JavaScript)](Create_Circles_on_Different_Layers_Example_JS.htm)
[Insert Block, Notes, and Sketch Entities (JavaScript)](Insert_Block_Notes_and_Sketch_Entitites_Example_JS.htm)
[Add and Modify Custom Data (JavaScript)](Add_and_Modify_Custom_Data_Example_JS.htm)

## Accessors

[IDocument::GetObjectByHandle](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetObjectByHandle.html)

[ISelectionManager::GetSelectedObject](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)

[ISelectionManager::GetSelectedObjects](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObjects.html)

[ISketchManager::GetEntities](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~GetEntities.html)

[ISketchManager::InsertCircle](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertCircle.html)

[ISketchManager::InsertCircleBy3Points](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertCircleBy3Points.html)

[ISketchManager::InsertCircleByDiameter](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertCircleByDiameter.html)

[IVewport::GetClippedObject](Interop.dsAutomation~Interop.dsAutomation.IViewport~GetClippedObject.html)

## Access Diagram

DSObjectModel.pdf#Circle

[Circle](DSObjectModel.pdf#Circle)

## See Also

[ICircle Members](Interop.dsAutomation~Interop.dsAutomation.ICircle_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IDiameterDimension Interface](Interop.dsAutomation~Interop.dsAutomation.IDiameterDimension.html)
[IRadialDimension Interface](Interop.dsAutomation~Interop.dsAutomation.IRadialDimension.html)
[IArcLengthDimension Interface](Interop.dsAutomation~Interop.dsAutomation.IArcLengthDimension.html)
[ICircleArc Interface](Interop.dsAutomation~Interop.dsAutomation.ICircleArc.html)
[IRegion Interface](Interop.dsAutomation~Interop.dsAutomation.IRegion.html)
