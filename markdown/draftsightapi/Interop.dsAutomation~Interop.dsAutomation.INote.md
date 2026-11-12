---
title: "INote Interface"
project: ""
interface: "INote"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.INote.html"
---

# INote Interface

Allows access to a Note.

## Syntax

### Visual Basic

```vb
Public Interface INote
```

### C#

```csharp
public interface INote
```

### JScript

```
public interface INote
```

### Managed Extensions for C++

```
public __gc __interface INote
```

### C++/CLI

```cpp
public interface class INote
```

## Examples

##### COM native C++

If the selected object is an INote object, then get the object.

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

//If selected object is an Note entity
if(dsNoteType == retObjType )
{
INotePtr dsNote( selObj );

strPrint.Format( L"Note\r\n" );
fileOutput.WriteString( strPrint );

//Do dump for Note entity
//See the entity's [Layer](Interop.dsAutomation~Interop.dsAutomation.INote~Layer.html), [LineScale](Interop.dsAutomation~Interop.dsAutomation.INote~LineScale.html), [LineStyle](Interop.dsAutomation~Interop.dsAutomation.INote~LineStyle.html), [LineWeight](Interop.dsAutomation~Interop.dsAutomation.INote~LineWeight.html),
//or [Visible](Interop.dsAutomation~Interop.dsAutomation.INote~Visible.html) property for the DumpGraphicsEntity template
CAddinDumpManager::DumpGraphicsEntity<INotePtr>( dsNote, fileOutput );

...

## Examples

[Insert Notes (C#)](Insert_Notes_Example_CSharp.htm)
[Insert Notes (VB.NET)](Insert_Notes_Example_VBNET.htm)
[Insert Notes (VBA)](Insert_Notes_Example_VBA.htm)
[Insert Notes with Parameters (C#)](Insert_Notes_with_Parameters_Example_CSharp.htm)
[Insert Notes with Parameters (VB.NET)](Insert_Notes_with_Parameters_Example_VBNET.htm)
[Insert Notes with Parameters (VBA)](Insert_Notes_with_Parameters_Example_VBA.htm)
[Insert Block, Notes, and Sketch Entities (JavaScript)](Insert_Block_Notes_and_Sketch_Entitites_Example_JS.htm)

## Accessors

[IDocument::GetObjectByHandle](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetObjectByHandle.html)

[ILeader::GetNoteAnnotation](Interop.dsAutomation~Interop.dsAutomation.ILeader~GetNoteAnnotation.html)

[ISelectionManager::GetSelectedObject](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)

[ISelectionManager::GetSelectedObjects](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObjects.html)

[ISketchManager::GetEntities](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~GetEntities.html)

[ISketchManager::InsertNote](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertNote.html)

[ISketchManager::InsertNoteWithParameters](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertNoteWithParameters.html)

## Access Diagram

DSObjectModel.pdf#Note

[Note](DSObjectModel.pdf#Note)

## See Also

[INote Members](Interop.dsAutomation~Interop.dsAutomation.INote_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[ISimpleNote Interface](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote.html)
[ITextStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITextStyle.html)
