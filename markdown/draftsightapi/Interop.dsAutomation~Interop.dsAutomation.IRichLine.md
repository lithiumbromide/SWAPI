---
title: "IRichLine Interface"
project: ""
interface: "IRichLine"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRichLine.html"
---

# IRichLine Interface

Allows access to the RichLine.

## Syntax

### Visual Basic

```vb
Public Interface IRichLine
```

### C#

```csharp
public interface IRichLine
```

### JScript

```
public interface IRichLine
```

### Managed Extensions for C++

```
public __gc __interface IRichLine
```

### C++/CLI

```cpp
public interface class IRichLine
```

## Examples

##### COM native C++

If the selected object is an IRichLine object, then get the object.

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

//If selected object is RichLine entity
if(dsRichLineType == retObjType )
{
IRichLinePtr dsRichLine( selObj );

strPrint.Format( L"RichLine\r\n" );
fileOutput.WriteString( strPrint );

//Do dump for RichLine entity

//See the entity's [Layer](Interop.dsAutomation~Interop.dsAutomation.ICircle~Layer.html), [LineScale](Interop.dsAutomation~Interop.dsAutomation.ICircle~LineScale.html), [LineStyle](Interop.dsAutomation~Interop.dsAutomation.ICircle~LineStyle.html), [LineWeight](Interop.dsAutomation~Interop.dsAutomation.ICircle~LineWeight.html),
//or [Visible](Interop.dsAutomation~Interop.dsAutomation.ICircle~Visible.html) property for the DumpGraphicsEntity template
CAddinDumpManager::DumpGraphicsEntity<IRichLinePtr>( dsRichLine, fileOutput );

...

## Examples

[Construct RichLine (C#)](Construct_RichLine_Example_CSharp.htm)
[Construct RichLine (VB.NET)](Construct_RichLine_Example_VBNET.htm)
[Construct RichLine (VBA)](Construct_RichLine_Example_VBA.htm)

## Accessors

[IDocument::GetObjectByHandle](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetObjectByHandle.html)

[ISelectionManager::GetSelectedObject](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)

[ISelectionManager::GetSelectedObjects](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObjects.html)

[ISketchManager::GetEntities](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~GetEntities.html)

[ISketchManager::InsertRichLine](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertRichLine.html)

## Access Diagram

DSObjectModel.pdf#RichLine

[RichLine](DSObjectModel.pdf#RichLine)

## See Also

[IRichLine Members](Interop.dsAutomation~Interop.dsAutomation.IRichLine_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IRichLineStyleManager Interface](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyleManager.html)
[IRichLineStyle Interface](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle.html)
