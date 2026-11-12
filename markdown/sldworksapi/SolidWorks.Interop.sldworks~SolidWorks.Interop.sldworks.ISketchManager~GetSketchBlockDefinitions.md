---
title: "GetSketchBlockDefinitions Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "GetSketchBlockDefinitions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~GetSketchBlockDefinitions.html"
---

# GetSketchBlockDefinitions Method (ISketchManager)

Gets all of the block definitions.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchBlockDefinitions() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim value As System.Object

value = instance.GetSketchBlockDefinitions()
```

### C#

```csharp
System.object GetSketchBlockDefinitions()
```

### C++/CLI

```cpp
System.Object^ GetSketchBlockDefinitions();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Block definitions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition.html)

## VBA Syntax

See [SketchManager::GetSketchBlockDefinitions](ms-its:sldworksapivb6.chm::/sldworks~SketchManager~GetSketchBlockDefinitions.html).

## Examples

[Get and Set Blocks Data in Any Document (VBA)](Get_and_Set_Blocks_Data_in_Any_Document_Example_VB.htm)
[Get Block Definitions in Part or Assembly (VBA)](Get_Block_Definitions_in_Part_or_Assembly_Example_VB.htm)
[Get Block Information (VBA)](Get_Block_Information_Example_VB.htm)

## Remarks

See [Block Definitions and Block Instances](sldworksAPIProgGuide.chm::/OVERVIEW/Block_Definitions_and_Block_Instances.htm) for details.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchManager::GetSketchBlockDefinitionCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~GetSketchBlockDefinitionCount.html)
[ISketchManager::IGetSketchBlockDefinitions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~IGetSketchBlockDefinitions.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
