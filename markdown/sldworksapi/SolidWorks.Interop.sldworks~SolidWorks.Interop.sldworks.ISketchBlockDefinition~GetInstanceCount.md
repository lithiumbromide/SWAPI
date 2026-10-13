---
title: "GetInstanceCount Method (ISketchBlockDefinition)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockDefinition"
member: "GetInstanceCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetInstanceCount.html"
---

# GetInstanceCount Method (ISketchBlockDefinition)

Gets the number of block instances of this block definition.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetInstanceCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockDefinition
Dim value As System.Integer

value = instance.GetInstanceCount()
```

### C#

```csharp
System.int GetInstanceCount()
```

### C++/CLI

```cpp
System.int GetInstanceCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of block instances

## VBA Syntax

See [SketchBlockDefinition::GetInstanceCount](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockDefinition~GetInstanceCount.html).

## Examples

[Get and Set Blocks in Any Document (VBA)](Get_and_Set_Blocks_Data_in_Any_Document_Example_VB.htm)
[Get Blocks in Drawing (VBA)](Get_Blocks_in_Drawing_Example_VB.htm)

## Remarks

Call this method before calling [ISketchBlockDefinition::IGetInstances](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~IGetInstances.html) to get the size of the array for that method.

## See Also

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.html)
[ISketchBlockDefinition::GetInstances Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetInstances.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
