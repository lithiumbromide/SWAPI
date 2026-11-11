---
title: "GetSelectedObjectCount Method (ISelectionManager)"
project: ""
interface: "ISelectionManager"
member: "GetSelectedObjectCount"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObjectCount.html"
---

# GetSelectedObjectCount Method (ISelectionManager)

Gets the number of selected entities in the current selection set.

## Syntax

### Visual Basic

```vb
Function GetSelectedObjectCount( _
   ByVal SSType As dsSelectionSetType_e _
) As System.Integer
```

### C#

```csharp
System.int GetSelectedObjectCount(
   dsSelectionSetType_e SSType
)
```

### JScript

```
function GetSelectedObjectCount(
   SSType : dsSelectionSetType_e
) : System.int;
```

### Managed Extensions for C++

```
System.int GetSelectedObjectCount(
   dsSelectionSetType_e SSType
)
```

### C++/CLI

```cpp
System.int GetSelectedObjectCount(
   dsSelectionSetType_e SSType
)
```

### Parameters

- `SSType`: Type of selection as defined in [dsSelectionSetType_e](Interop.dsAutomation~Interop.dsAutomation.dsSelectionSetType_e.html)

### Return Value

Number of selected entities

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

[Rotate and Copy Entities (C#)](Rotate_and_Copy_Entities_Example_CSharp.htm)
[Rotate and Copy Entities (VB.NET)](Rotate_and_Copy_Entities_Example_VBNET.htm)
[Rotate and Copy Entities (VBA)](Rotate_and_Copy_Entities_Example_VBA.htm)
[Insert Hatch (JavaScript)](Insert_Hatch_Example_JS.htm)

## Remarks

You can also use this method to determine if a valid selection was made.

## See Also

[ISelectionManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager.html)
[ISelectionManager Members](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager_members.html)
[ISelectionManager::GetSelectedObject Method](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)
[ISelectionManager::GetSelectedObjects Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObjects.html)

## Availability

DraftSight V1R1
