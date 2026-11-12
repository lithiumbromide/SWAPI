---
title: "GetInstances Method (ISketchBlockDefinition)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockDefinition"
member: "GetInstances"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetInstances.html"
---

# GetInstances Method (ISketchBlockDefinition)

Gets all of the block instances of this block definition.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetInstances() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockDefinition
Dim value As System.Object

value = instance.GetInstances()
```

### C#

```csharp
System.object GetInstances()
```

### C++/CLI

```cpp
System.Object^ GetInstances();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of all of the [block instances](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance.html)

## VBA Syntax

See [SketchBlockDefinition::GetInstances](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockDefinition~GetInstances.html).

## Examples

[Get and Set Blocks Data in Any Document (VBA)](Get_and_Set_Blocks_Data_in_Any_Document_Example_VB.htm)
[Get Block Information (VBA)](Get_Block_Information_Example_VB.htm)
[Get Blocks in Drawing (VBA)](Get_Blocks_in_Drawing_Example_VB.htm)

## See Also

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.html)
[ISketchBlockDefinition::GetInstanceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetInstanceCount.html)
[ISketchBlockDefinition::IGetInstances Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetInstances.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
