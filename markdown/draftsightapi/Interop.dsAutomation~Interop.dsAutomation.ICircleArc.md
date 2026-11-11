---
title: "ICircleArc Interface"
project: ""
interface: "ICircleArc"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICircleArc.html"
---

# ICircleArc Interface

Allows access to an Arc.

## Syntax

### Visual Basic

```vb
Public Interface ICircleArc
```

### C#

```csharp
public interface ICircleArc
```

### JScript

```
public interface ICircleArc
```

### Managed Extensions for C++

```
public __gc __interface ICircleArc
```

### C++/CLI

```cpp
public interface class ICircleArc
```

## Examples

##### COM native C++

If the selected object is an ICircleArc object, then get the selected object.

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

//If selected object is Arc entity
if(dsCircleArcType == retObjType )
{
ICircleArcPtr dsCircleArc( selObj );

strPrint.Format(L"Arc\r\n");
fileOutput.WriteString(strPrint);

//Do dump for Arc entity

//See the entity's [Layer](Interop.dsAutomation~Interop.dsAutomation.ICircleArc~Layer.html), [LineScale](Interop.dsAutomation~Interop.dsAutomation.ICircleArc~LineScale.html), [LineStyle](Interop.dsAutomation~Interop.dsAutomation.ICircleArc~LineStyle.html), [LineWeight](Interop.dsAutomation~Interop.dsAutomation.ICircleArc~LineWeight.html),
//or [Visible](Interop.dsAutomation~Interop.dsAutomation.ICircleArc~Visible.html) property for the DumpGraphicsEntity template
CAddinDumpManager::DumpGraphicsEntity<ICircleArcPtr>( dsCircleArc, fileOutput );

...

## Examples

[Construct Arc (C#)](Construct_Arc_Example_CSharp.htm)
[Construct Arc (VB.NET)](Construct_Arc_Example_VBNET.htm)
[Construct Arc (VBA)](Construct_Arc_Example_VBA.htm)
[Insert and Dimension Sketch (JavaScript)](Insert_and_Dimension_Sketch_Example_JS.htm)
[Mirror Entiites (JavaScript)](Mirror_Entities_Example_JS.htm)

## Accessors

[IDocument::GetObjectByHandle](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetObjectByHandle.html)

[ISelectionManager::GetSelectedObject](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)

[ISelectionManager::GetSelectedObjects](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObjects.html)

[ISketchManager::GetEntities](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~GetEntities.html)

[ISketchManager::InsertArc](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertArc.html)

[ISketchManager::InsertArcBy3Points](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertArcBy3Points.html)

[ISketchManager::InsertArcByCenter2Points2](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertArcByCenter2Points2.html)

## Access Diagram

DSObjectModel.pdf#CircleArc

[CircleArc](DSObjectModel.pdf#CircleArc)

## See Also

[ICircleArc Members](Interop.dsAutomation~Interop.dsAutomation.ICircleArc_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IDiameterDimension Interface](Interop.dsAutomation~Interop.dsAutomation.IDiameterDimension.html)
[IRadialDimension Interface](Interop.dsAutomation~Interop.dsAutomation.IRadialDimension.html)
[ICircle Interface](Interop.dsAutomation~Interop.dsAutomation.ICircle.html)
[IMathCircArc Interface](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc.html)
