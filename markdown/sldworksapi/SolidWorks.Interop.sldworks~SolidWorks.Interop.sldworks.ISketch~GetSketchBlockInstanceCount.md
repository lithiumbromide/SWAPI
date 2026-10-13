---
title: "GetSketchBlockInstanceCount Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetSketchBlockInstanceCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchBlockInstanceCount.html"
---

# GetSketchBlockInstanceCount Method (ISketch)

Gets the number of block instances in this sketch (i.e., the sketch under which the block instances are displayed in the FeatureManager design tree).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchBlockInstanceCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As System.Integer

value = instance.GetSketchBlockInstanceCount()
```

### C#

```csharp
System.int GetSketchBlockInstanceCount()
```

### C++/CLI

```cpp
System.int GetSketchBlockInstanceCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of block instances in this sketch

## VBA Syntax

See [Sketch::GetSketchBlockInstanceCount](ms-its:sldworksapivb6.chm::/sldworks~Sketch~GetSketchBlockInstanceCount.html).

## Remarks

Call this method before calling [ISketch::IGetSketchBlockInstances](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~IGetSketchBlockInstances.html) to get the size of the array for that method.

See [Block Definitions and Block Instances](sldworksAPIProgGuide.chm::/OVERVIEW/Block_Definitions_and_Block_Instances.htm) for details.

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::GetSketchBlockInstances Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchBlockInstances.html)
[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html)
[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
