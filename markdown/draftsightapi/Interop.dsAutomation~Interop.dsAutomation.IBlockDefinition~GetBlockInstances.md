---
title: "GetBlockInstances Method (IBlockDefinition)"
project: ""
interface: "IBlockDefinition"
member: "GetBlockInstances"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~GetBlockInstances.html"
---

# GetBlockInstances Method (IBlockDefinition)

Gets the Block instances for the Block definition.

## Syntax

### Visual Basic

```vb
Function GetBlockInstances() As System.Object
```

### C#

```csharp
System.object GetBlockInstances()
```

### JScript

```
function GetBlockInstances() : System.Object;
```

### Managed Extensions for C++

```
System.Object* GetBlockInstances();
```

### C++/CLI

```cpp
System.Object^ GetBlockInstances();
```

### Return Value

Array of [Block instances](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance.html)

## Examples

This code snippet shows how to get the Block instances.

##### COM native C++

_variant_t pVariantArrayBI = blkDefs->GetBlockInstances();
if( V_VT( &pVariantArrayBI ) != VT_EMPTY )
{
IBlockInstancePtr *blkIns = NULL;
int countOfBI = 0;
[TypeConverter::convertVariantArrayToPtrArray](GettingStarted-draftsightapi.html#convertVariantArrayToPtrArray)<IBlockInstancePtr, IBlockInstance>( pVariantArrayBI, blkIns, countOfBI );
}

## Examples

[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (C#)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_CSharp.htm)
[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (VB.NET)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_VBNET.htm)
[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (VBA)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_VBA.htm)

## See Also

[IBlockDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition.html)
[IBlockDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition_members.html)

## Availability

DraftSight V1R1
