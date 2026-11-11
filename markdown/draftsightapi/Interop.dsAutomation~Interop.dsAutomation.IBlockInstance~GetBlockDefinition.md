---
title: "GetBlockDefinition Method (IBlockInstance)"
project: ""
interface: "IBlockInstance"
member: "GetBlockDefinition"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IBlockInstance~GetBlockDefinition.html"
---

# GetBlockDefinition Method (IBlockInstance)

Gets the Block definition for the Block instance.

## Syntax

### Visual Basic

```vb
Function GetBlockDefinition() As BlockDefinition
```

### C#

```csharp
BlockDefinition GetBlockDefinition()
```

### JScript

```
function GetBlockDefinition() : BlockDefinition;
```

### Managed Extensions for C++

```
BlockDefinition* GetBlockDefinition();
```

### C++/CLI

```cpp
BlockDefinition^ GetBlockDefinition();
```

### Return Value

[Block definition](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition.html)

## Examples

This code snippet shows how to get the Block definition for a Block instance.

##### COM native C++

//Get Block definition for Block instance
IBlockDefinition blockDef = blkIns->GetBlockDefinition();

## Examples

[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (C#)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_CSharp.htm)
[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (VB.NET)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_VBNET.htm)
[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (VBA)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_VBA.htm)

## See Also

[IBlockInstance Interface](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance.html)
[IBlockInstance Members](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance_members.html)

## Availability

DraftSight V1R1
