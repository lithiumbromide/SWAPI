---
title: "GetSketchBlockDefinitionCount Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "GetSketchBlockDefinitionCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~GetSketchBlockDefinitionCount.html"
---

# GetSketchBlockDefinitionCount Method (ISketchManager)

Gets the number of block definitions in the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchBlockDefinitionCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim value As System.Integer

value = instance.GetSketchBlockDefinitionCount()
```

### C#

```csharp
System.int GetSketchBlockDefinitionCount()
```

### C++/CLI

```cpp
System.int GetSketchBlockDefinitionCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of block definitions in the model

## VBA Syntax

See [SketchManager::GetSketchBlockDefinitionCount](ms-its:sldworksapivb6.chm::/sldworks~SketchManager~GetSketchBlockDefinitionCount.html).

## Remarks

Call this method before calling [ISketchManager::IGetSketchBlockDefinitions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~IGetSketchBlockDefinitions.html) to get the size of the array for that method.

See [Block Definitions and Block Instances](sldworksAPIProgGuide.chm::/OVERVIEW/Block_Definitions_and_Block_Instances.htm) for details.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchManager::GetSketchBlockDefinitions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~GetSketchBlockDefinitions.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
