---
title: "GetWorkingSpace Method (IBlockInstance)"
project: ""
interface: "IBlockInstance"
member: "GetWorkingSpace"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IBlockInstance~GetWorkingSpace.html"
---

# GetWorkingSpace Method (IBlockInstance)

Gets the type of working space and the working space object.

## Syntax

### Visual Basic

```vb
Sub GetWorkingSpace( _
   ByRef Type As dsObjectType_e, _
   ByRef WorkSpace As System.Object _
)
```

### C#

```csharp
void GetWorkingSpace(
   out dsObjectType_e Type,
   out System.object WorkSpace
)
```

### JScript

```
function GetWorkingSpace(
   Type : dsObjectType_e,
   WorkSpace : System.Object
);
```

### Managed Extensions for C++

```
void GetWorkingSpace(
   [PARAMFLAG::Out] dsObjectType_e Type,
   [PARAMFLAG::Out] System.Object* WorkSpace
)
```

### C++/CLI

```cpp
void GetWorkingSpace(
   [Out] dsObjectType_e Type,
   [Out] System.Object^ WorkSpace
)
```

### Parameters

- `Type`: Type of working space as defined in [dsObjectType_e](Interop.dsAutomation~Interop.dsAutomation.dsObjectType_e.html)
- `WorkSpace`: [Model](Interop.dsAutomation~Interop.dsAutomation.IModel.html) or [Sheet](Interop.dsAutomation~Interop.dsAutomation.ISheet.html)

## Examples

This code snippet shows how to get the ID and working space of a Block instance. This code snippet also shows how to determine if the working space is a model or sheet.

##### COM native C++

//Get Block instance ID
bstr_t blkInstanceID = blkIns->GetID();

//Get working space
dsObjectType_e oType;
IDispatch pWorkingSpace;
blkIns->GetWorkingSpace( &oType, &pWorkingSpace );

//If working space is a model
if( dsModelType == oType )
{

IModel modelSpace ( pWorkingSpace );
. . .

}
else
{
//If working space is a sheet
if( dsSheetType == oType )
{
ISheetPtr sheet( pWorkingSpace );

. . .

}

}

## Examples

[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (C#)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_CSharp.htm)
[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (VB.NET)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_VBNET.htm)
[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (VBA)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_VBA.htm)

## See Also

[IBlockInstance Interface](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance.html)
[IBlockInstance Members](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance_members.html)

## Availability

DraftSight V1R1
