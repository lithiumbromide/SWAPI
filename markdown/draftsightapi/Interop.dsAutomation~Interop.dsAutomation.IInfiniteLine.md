---
title: "IInfiniteLine Interface"
project: ""
interface: "IInfiniteLine"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine.html"
---

# IInfiniteLine Interface

Allows access to an InfiniteLine.

## Syntax

### Visual Basic

```vb
Public Interface IInfiniteLine
```

### C#

```csharp
public interface IInfiniteLine
```

### JScript

```
public interface IInfiniteLine
```

### Managed Extensions for C++

```
public __gc __interface IInfiniteLine
```

### C++/CLI

```cpp
public interface class IInfiniteLine
```

## Examples

##### COM native C++

If the selected object is an IInfiniteLine object, then get the object.

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

//If selected object is an InfiniteLine entity
if(dsInfiniteLineType == retObjType )
{
IInfiniteLinePtr dsInfiniteLine( selObj );

strPrint.Format( L"InfiniteLine\r\n" );
fileOutput.WriteString( strPrint );

//Do dump for InfiniteLine entity

//See the entity's [Layer](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~Layer.html), [LineScale](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~LineScale.html), [LineStyle](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~LineStyle.html), [LineWeight](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~LineWeight.html),
//or [Visible](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~Visible.html) property for the DumpGraphicsEntity template
CAddinDumpManager::DumpGraphicsEntity<IInfiniteLinePtr>( dsInfiniteLine, fileOutput );

...

## Examples

[Construct InfiniteLine (C#)](Construct_InfiniteLine_Example_CSharp.htm)
[Construct InfiniteLine (VB.NET)](Construct_InfiniteLine_Example_VBNET.htm)
[Construct InfiniteLine (VBA)](Construct_InfiniteLine_Example_VBA.htm)

## Accessors

[IDocument::GetObjectByHandle](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetObjectByHandle.html)

[ISelectionManager::GetSelectedObject](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)

[ISelectionManager::GetSelectedObjects](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObjects.html)

[ISketchManager::GetEntities](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~GetEntities.html)

[ISketchManager::InsertInfiniteLine](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertInfiniteLine.html)

## Access Diagram

DSObjectModel.pdf#InfiniteLine

[InfiniteLine](DSObjectModel.pdf#InfiniteLine)

## See Also

[IInfiniteLine Members](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[ILine Interface](Interop.dsAutomation~Interop.dsAutomation.ILine.html)
[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IRay Interface](Interop.dsAutomation~Interop.dsAutomation.IRay.html)
[IPolyLine3D Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D.html)
[ITrace Interface](Interop.dsAutomation~Interop.dsAutomation.ITrace.html)
