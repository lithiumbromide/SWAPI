---
title: "ISimpleNote Interface"
project: ""
interface: "ISimpleNote"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISimpleNote.html"
---

# ISimpleNote Interface

Allows access to a SimpleNote.

## Syntax

### Visual Basic

```vb
Public Interface ISimpleNote
```

### C#

```csharp
public interface ISimpleNote
```

### JScript

```
public interface ISimpleNote
```

### Managed Extensions for C++

```
public __gc __interface ISimpleNote
```

### C++/CLI

```cpp
public interface class ISimpleNote
```

## Examples

##### COM native C++

If the selected object is an ISimpleNote object, then get the object.

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

//If selected object is an SimpleNote entity
if(dsSimpleNoteType == retObjType )
{
ISimpleNotePtr dsSimpleNote( selObj );

strPrint.Format( L"SimpleNote\r\n" );
fileOutput.WriteString( strPrint );

//Do dump for SimpleNote entity
//See the entity's [Layer](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~Layer.html), [LineScale](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~LineScale.html), [LineStyle](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~LineStyle.html), [LineWeight](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~LineWeight.html),
//or [Visible](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~Visible.html) property for the DumpGraphicsEntity template
CAddinDumpManager::DumpGraphicsEntity<ISimpleNotePtr>( dsSimpleNote, fileOutput );

...

## Examples

[Insert SimpleNote (C#)](Insert_SimpleNote_Example_CSharp.htm)
[Insert SimpleNote (VB.NET)](Insert_SimpleNote_Example_VBNET.htm)
[Insert SimpleNote (VBA)](Insert_SimpleNote_Example_VBA.htm)

## Accessors

[IDocument::GetObjectByHandle](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetObjectByHandle.html)

[ISelectionManager::GetSelectedObject](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)

[ISelectionManager::GetSelectedObjects](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObjects.html)

[ISketchManager::GetEntities](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~GetEntities.html)

[ISketchManager::InsertSimpleNote](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertSimpleNote.html)

## Access Diagram

DSObjectModel.pdf#SimpleNote

[SimpleNote](DSObjectModel.pdf#SimpleNote)

## See Also

[ISimpleNote Members](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[INote Interface](Interop.dsAutomation~Interop.dsAutomation.INote.html)
[ITextStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITextStyle.html)
