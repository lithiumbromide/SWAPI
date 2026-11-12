---
title: "IPolyLine Interface"
project: ""
interface: "IPolyLine"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html"
---

# IPolyLine Interface

Allows access to a 2D PolyLine.

## Syntax

### Visual Basic

```vb
Public Interface IPolyLine
```

### C#

```csharp
public interface IPolyLine
```

### JScript

```
public interface IPolyLine
```

### Managed Extensions for C++

```
public __gc __interface IPolyLine
```

### C++/CLI

```cpp
public interface class IPolyLine
```

## Examples

##### COM native C++

If the selected object is an IPolyLine object, then get the object.

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

//If selected object is an 2D PolyLine entity
if(dsPolyLineType == retObjType )
{
IPolyLinePtr dsPolyLine( selObj );

strPrint.Format( L"2D PolyLine\r\n" );
fileOutput.WriteString( strPrint );

//Do dump for 2D PolyLine entity

//See the entity's [Layer](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Layer.html), [LineScale](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~LineScale.html), [LineStyle](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~LineStyle.html), [LineWeight](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~LineWeight.html),
//or [Visible](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Visible.html) property for the DumpGraphicsEntity template
CAddinDumpManager::DumpGraphicsEntity<IPolyLinePtr>( dsPolyLine, fileOutput );

...

## Examples

[Construct 2D PolyLine (C#)](Construct_2D_PolyLine_Example_CSharp.htm)
[Construct 2D PolyLine (VB.NET)](Construct_2D_PolyLine_Example_VBNET.htm)
[Construct 2D PolyLine (VBA)](Construct_2D_PolyLine_Example_VBA.htm)
[Create Aligned Linear and Ordinate Dimenions (C#)](Create_Aligned_Linear_And_Ordinate_Dimensions_Example_CSharp.htm)
[Create Aligned Linear and Ordinate Dimensions (VB.NET)](Create_Aligned_Linear_And_Ordinate_Dimensions_Example_VBNET.htm)
[Create Aligned Linear and Ordinate Dimensions (VBA)](Create_Aligned_Linear_And_Ordinate_Dimensions_Example_VBA.htm)
[Create Linear Pattern (C#)](Create_Linear_Pattern_Example_CSharp.htm)
[Create Linear Pattern (VB.NET)](Create_Linear_Pattern_Example_VBNET.htm)
[Create Linear Pattern (VBA)](Create_Linear_Pattern_Example_VBA.htm)
[Insert Block, Notes, and Sketch Entities (JavaScript)](Insert_Block_Notes_and_Sketch_Entitites_Example_JS.htm)
[Mirror Entities (JavaScript)](Mirror_Entities_Example_JS.htm)

## Accessors

[IDocument::GetObjectByHandle](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetObjectByHandle.html)

[IPolyLine::Split](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Split.html)

[ISelectionManager::GetSelectedObject](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)

[ISelectionManager::GetSelectedObjects](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObjects.html)

[ISketchManager::GetEntities](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~GetEntities.html)

[ISketchManager::InsertPolyLine2D](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertPolyline2D.html)

[IViewport::GetClippedObject](Interop.dsAutomation~Interop.dsAutomation.IViewport~GetClippedObject.html)

## Access Diagram

DSObjectModel.pdf#PolyLine

[PolyLine](DSObjectModel.pdf#PolyLine)

## See Also

[IPolyLine Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IInfiniteLine Interface](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine.html)
[ILine Interface](Interop.dsAutomation~Interop.dsAutomation.ILine.html)
[IRay Interface](Interop.dsAutomation~Interop.dsAutomation.IRay.html)
[IPolyLine3D Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D.html)
[IRegion Interface](Interop.dsAutomation~Interop.dsAutomation.IRegion.html)
[ITrace Interface](Interop.dsAutomation~Interop.dsAutomation.ITrace.html)
[ISketchManager::ChamferPolyLine ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ChamferPolyLine.html)
[ISketchManager::FilletPolyLine Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~FilletPolyLine.html)
