---
title: "ILine Interface"
project: ""
interface: "ILine"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILine.html"
---

# ILine Interface

Allows access to a Line.

## Syntax

### Visual Basic

```vb
Public Interface ILine
```

### C#

```csharp
public interface ILine
```

### JScript

```
public interface ILine
```

### Managed Extensions for C++

```
public __gc __interface ILine
```

### C++/CLI

```cpp
public interface class ILine
```

## Examples

##### COM native C++

If the selected object is an ILine object, then get the object.

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

//If selected object is Line entity
if( dsLineType == retObjType )
{
ILinePtr dsLine( selObj );

strPrint.Format( L"Line\r\n" );
fileOutput.WriteString( strPrint );

//Do dump for Line entity
//See the entity's [Layer](Interop.dsAutomation~Interop.dsAutomation.ILine~Layer.html), [LineScale](Interop.dsAutomation~Interop.dsAutomation.ILine~LineScale.html), [LineStyle](Interop.dsAutomation~Interop.dsAutomation.ILine~LineStyle.html), [LineWeight](Interop.dsAutomation~Interop.dsAutomation.ILine~LineWeight.html),
//or [Visible](Interop.dsAutomation~Interop.dsAutomation.ILine~Visible.html) property for the DumpGraphicsEntity template
CAddinDumpManager::DumpGraphicsEntity<ILinePtr>( dsLine, fileOutput );

...

## Examples

[Construct Line (C#)](Construct_Line_Example_CSharp.htm)
[Construct Line (VB.NET)](Construct_Line_Example_VBNET.htm)
[Construct Line (VBA)](Construct_Line_Example_VBA.htm)
[Insert and Dimension Sketch (JavaScript)](Insert_and_Dimension_Sketch_Example_JS.htm)
[Insert Lines and Angular Dimension (JavaScript)](Insert_Lines_and_Angular_Dimension_Example_JS.htm)

## Accessors

[IDocument::GetObjectByHandle](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetObjectByHandle.html)

[ISelectionManager::GetSelectedObject](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)

[ISelectionManager::GetSelectedObjects](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObjects.html)

[ISketchManager::GetEntities](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~GetEntities.html)

[ISketchManager::InsertLine](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertLine.html)

## Access Diagram

DSObjectModel.pdf#Line

[Line](DSObjectModel.pdf#Line)

## See Also

[ILine Members](Interop.dsAutomation~Interop.dsAutomation.ILine_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IInfiniteLine Interface](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine.html)
[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IRay Interface](Interop.dsAutomation~Interop.dsAutomation.IRay.html)
[IPolyLine3D Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D.html)
[ILineStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ILineStyle.html)
[ILineStyleManager Interface](Interop.dsAutomation~Interop.dsAutomation.ILineStyleManager.html)
[ITrace Interface](Interop.dsAutomation~Interop.dsAutomation.ITrace.html)
