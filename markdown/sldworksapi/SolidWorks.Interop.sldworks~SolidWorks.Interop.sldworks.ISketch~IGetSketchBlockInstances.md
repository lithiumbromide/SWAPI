---
title: "IGetSketchBlockInstances Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "IGetSketchBlockInstances"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSketchBlockInstances.html"
---

# IGetSketchBlockInstances Method (ISketch)

Gets the block instances in this sketch (i.e., the sketch under which the block instances are displayed in the FeatureManager design tree).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSketchBlockInstances( _
   ByVal Count As System.Integer _
) As SketchBlockInstance
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim Count As System.Integer
Dim value As SketchBlockInstance

value = instance.IGetSketchBlockInstances(Count)
```

### C#

```csharp
SketchBlockInstance IGetSketchBlockInstances(
   System.int Count
)
```

### C++/CLI

```cpp
SketchBlockInstance^ IGetSketchBlockInstances(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of block instances in this sketch

### Return Value

- in-process, unmanaged C++: Pointer to an array containing the [block instances](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance.html) in this sketch

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [ISketch::GetSketchBlockInstanceCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetSketchBlockInstanceCount.html) before calling this method to get the number of block instances in this sketch.

See [Block Definitions and Block Instances](sldworksAPIProgGuide.chm::/OVERVIEW/Block_Definitions_and_Block_Instances.htm) for details.

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::GetSketchBlockInstances Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchBlockInstances.html)
[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html)
[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
