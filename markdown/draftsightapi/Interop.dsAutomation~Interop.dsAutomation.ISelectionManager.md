---
title: "ISelectionManager Interface"
project: ""
interface: "ISelectionManager"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISelectionManager.html"
---

# ISelectionManager Interface

Allows access to a selected entity.

## Syntax

### Visual Basic

```vb
Public Interface ISelectionManager
```

### C#

```csharp
public interface ISelectionManager
```

### JScript

```
public interface ISelectionManager
```

### Managed Extensions for C++

```
public __gc __interface ISelectionManager
```

### C++/CLI

```cpp
public interface class ISelectionManager
```

## Examples

This code snippet shows how to write the names, captions, and values of the selected objects to a file.

##### COM native C++

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

//If selected object is Block instance
if( dsBlockInstanceType == retObjType )
{
IBlockInstancePtr blkIns( selObj );

//Get Block definition name and write it to output file
bstr_t blockName = blkIns->GetBlockDefinition()->GetName();
strPrint.Format( L"Instance of (%s) block definition\r\n", blockName.operator const wchar_t*() );
fileOutput.WriteString( strPrint );
}
else
//If selected object is BlockAttribute definition
if( dsAttributeDefinitionType == retObjType )
{
IAttributeDefinitionPtr AttDefs( selObj );

//Get BlockAttribute definition name
bstr_t AttDefName = AttDefs->GetName();

strPrint.Format( L"Attribute definition (%s) \r\n", AttDefName.operator const wchar_t*() );
fileOutput.WriteString( strPrint );

//Get BlockAttribute definition caption
bstr_t AttDefCaption = AttDefs->GetCaption();

strPrint.Format( L"\tCaption: %s\r\n", AttDefCaption.operator const wchar_t*() );
fileOutput.WriteString( strPrint );

strPrint.Format( L"\tName: %s\r\n", AttDefName.operator const wchar_t*() );
fileOutput.WriteString( strPrint );

//Get BlockAttribute definition value
bstr_t AttDefValue = AttDefs->GetValue();

strPrint.Format( L"\tValue: %s\r\n", AttDefValue.operator const wchar_t*() );
fileOutput.WriteString( strPrint );
}

## Examples

[Insert SimpleNote (C#)](Insert_SimpleNote_Example_CSharp.htm)
[Insert SimpleNote (VB.NET)](Insert_SimpleNote_Example_VBNET.htm)
[Insert SimpleNote (VBA)](Insert_SimpleNote_Example_VBA.htm)
[Insert Hatch (JavaScript)](Insert_Hatch_Example_JS.htm)

## Accessors

[IDocument::GetSelectionManager](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetSelectionManager.html)

## Access Diagram

DSObjectModel.pdf#SelectionManager

[SelectionManager](DSObjectModel.pdf#SelectionManager)

## See Also

[ISelectionManager Members](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[ISelectionManager Event SelectionChangedNotify](Interop.dsAutomation~Interop.dsAutomation._ISelectionManagerEvents_SelectionChangedNotifyEventHandler.html)
[ISelectionManager Event SelectionPreNotifyEventHandler Delegate](Interop.dsAutomation~Interop.dsAutomation._ISelectionManagerEvents_SelectionPreNotifyEventHandler.html)
