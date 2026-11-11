---
title: "IPoint Interface"
project: ""
interface: "IPoint"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPoint.html"
---

# IPoint Interface

Allows access to a point.

## Syntax

### Visual Basic

```vb
Public Interface IPoint
```

### C#

```csharp
public interface IPoint
```

### JScript

```
public interface IPoint
```

### Managed Extensions for C++

```
public __gc __interface IPoint
```

### C++/CLI

```cpp
public interface class IPoint
```

## Examples

##### COM native C++

If the selected object is an IPoint object, then get the object.

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

//If selected object is point entity
if( dsPointType == retObjType )
{
IPointPtr dsPoint( selObj );

fileOutput.WriteString( L"Point\r\n" );

//Do dump for point entity
//See the entity's [Layer](Interop.dsAutomation~Interop.dsAutomation.IPoint~Layer.html), [LineScale](Interop.dsAutomation~Interop.dsAutomation.IPoint~LineScale.html), [LineStyle](Interop.dsAutomation~Interop.dsAutomation.IPoint~LineStyle.html), [LineWeight](Interop.dsAutomation~Interop.dsAutomation.IPoint~LineWeight.html),
//or [Visible](Interop.dsAutomation~Interop.dsAutomation.IPoint~Visible.html) property for the DumpGraphicsEntity template
CAddinDumpManager::DumpGraphicsEntity<IPointPtr>( dsPoint, fileOutput );

...

## Examples

[Insert Point (C#)](Insert_Point_Example_CSharp.htm)
[Insert Point (VB.NET)](Insert_Point_Example_VBNET.htm)
[Insert Point (VBA)](Insert_Point_Example_VBA.htm)

## Accessors

[IDocument::GetObjectByHandle](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetObjectByHandle.html)

[ISelectionManager::GetSelectedObject](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)

[ISelectionManager::GetSelectedObjects](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObjects.html)

[ISketchManager::GetEntities](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~GetEntities.html)

[ISketchManager::InsertPoint](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertPoint.html)

## Access Diagram

DSObjectModel.pdf#Point

[Point](DSObjectModel.pdf#Point)

## See Also

[IPoint Members](Interop.dsAutomation~Interop.dsAutomation.IPoint_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
