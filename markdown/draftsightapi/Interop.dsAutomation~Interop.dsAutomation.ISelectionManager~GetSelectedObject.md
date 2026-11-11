---
title: "GetSelectedObject Method (ISelectionManager)"
project: ""
interface: "ISelectionManager"
member: "GetSelectedObject"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html"
---

# GetSelectedObject Method (ISelectionManager)

Gets the selected entity.

## Syntax

### Visual Basic

```vb
Function GetSelectedObject( _
   ByVal SSType As dsSelectionSetType_e, _
   ByVal AtIndex As System.Integer, _
   ByRef ObjType As dsObjectType_e _
) As System.Object
```

### C#

```csharp
System.object GetSelectedObject(
   dsSelectionSetType_e SSType,
   System.int AtIndex,
   out dsObjectType_e ObjType
)
```

### JScript

```
function GetSelectedObject(
   SSType : dsSelectionSetType_e,
   AtIndex : System.int,
   ObjType : dsObjectType_e
) : System.Object;
```

### Managed Extensions for C++

```
System.Object* GetSelectedObject(
   dsSelectionSetType_e SSType,
   System.int AtIndex,
   [PARAMFLAG::Out] dsObjectType_e ObjType
)
```

### C++/CLI

```cpp
System.Object^ GetSelectedObject(
   dsSelectionSetType_e SSType,
   System.int AtIndex,
   [Out] dsObjectType_e ObjType
)
```

### Parameters

- `SSType`: Type of selection as defined in [dsSelectionSetType_e](Interop.dsAutomation~Interop.dsAutomation.dsSelectionSetType_e.html)
- `AtIndex`: Index position within the current selection set, where index ranges from 0 to [ISelectionManager::GetSelectedObjectCount](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObjectCount.html)
- `ObjType`: Selected entity as defined in [dsObjectType_e](Interop.dsAutomation~Interop.dsAutomation.dsObjectType_e.html); null might be returned if the selected entity is not supported of if nothing is selected

### Return Value

Selected entity

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

[Get Hatch and Hatch Boundary Loop Data (C#)](Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_CSharp.htm)
[Get Hatch and Hatch Boundary Loop Data (VB.NET)](Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_VBNET.htm)
[Get Hatch and Hatch Boundary Loop Data (VBA)](Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_VBA.htm)
[Rotate and Copy Entities (C#)](Rotate_and_Copy_Entities_Example_CSharp.htm)
[Rotate and Copy Entities (VB.NET)](Rotate_and_Copy_Entities_Example_VBNET.htm)
[Rotate and Copy Entities (VBA)](Rotate_and_Copy_Entities_Example_VBA.htm)
[Insert Hatch (JavaScript)](Insert_Hatch_Example_JS.htm)

## See Also

[ISelectionManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager.html)
[ISelectionManager Members](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager_members.html)
[ISketchManager::GetEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~GetEntities.html)
[ISelectionManager::GetSelectedObjects Method](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObjects.html)

## Availability

DraftSight V1R1
