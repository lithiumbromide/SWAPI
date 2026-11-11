---
title: "GetID Method (IBlockInstance)"
project: ""
interface: "IBlockInstance"
member: "GetID"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IBlockInstance~GetID.html"
---

# GetID Method (IBlockInstance)

Gets the ID of the Block instance.

## Syntax

### Visual Basic

```vb
Function GetID() As System.Integer
```

### C#

```csharp
System.int GetID()
```

### JScript

```
function GetID() : System.int;
```

### Managed Extensions for C++

```
System.int GetID();
```

### C++/CLI

```cpp
System.int GetID();
```

### Return Value

ID of the Block instance

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
