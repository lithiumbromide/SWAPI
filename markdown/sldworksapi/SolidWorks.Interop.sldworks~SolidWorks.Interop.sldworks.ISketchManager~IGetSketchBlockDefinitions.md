---
title: "IGetSketchBlockDefinitions Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "IGetSketchBlockDefinitions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~IGetSketchBlockDefinitions.html"
---

# IGetSketchBlockDefinitions Method (ISketchManager)

Gets all of the block definitions.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSketchBlockDefinitions( _
   ByVal BlockDefCount As System.Integer _
) As SketchBlockDefinition
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim BlockDefCount As System.Integer
Dim value As SketchBlockDefinition

value = instance.IGetSketchBlockDefinitions(BlockDefCount)
```

### C#

```csharp
SketchBlockDefinition IGetSketchBlockDefinitions(
   System.int BlockDefCount
)
```

### C++/CLI

```cpp
SketchBlockDefinition^ IGetSketchBlockDefinitions(
   System.int BlockDefCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BlockDefCount`: Number of block definitions

### Return Value

- in-process, unmanaged C++: Pointer to an array of [block definitions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [ISketchManager::GetSketchBlockDefinitionCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~GetSketchBlockDefinitionCount.html) to get the value of BlockDefCount.

See [Block Definitions and Block Instances](sldworksAPIProgGuide.chm::/OVERVIEW/Block_Definitions_and_Block_Instances.htm) for details.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchManager::GetSketchBlockDefinitions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~GetSketchBlockDefinitions.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
