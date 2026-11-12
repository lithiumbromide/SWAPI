---
title: "GetSketchBlockInstances Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetSketchBlockInstances"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchBlockInstances.html"
---

# GetSketchBlockInstances Method (ISketch)

Gets the block instances in this sketch (i.e., the sketch under which the block instances are displayed in the FeatureManager design tree).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchBlockInstances() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As System.Object

value = instance.GetSketchBlockInstances()
```

### C#

```csharp
System.object GetSketchBlockInstances()
```

### C++/CLI

```cpp
System.Object^ GetSketchBlockInstances();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array containing the [block instances](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance.html) in this sketch

## VBA Syntax

See [Sketch::GetSketchBlockInstances](ms-its:sldworksapivb6.chm::/sldworks~Sketch~GetSketchBlockInstances.html).

## Remarks

See [Block Definitions and Block Instances](sldworksAPIProgGuide.chm::/OVERVIEW/Block_Definitions_and_Block_Instances.htm) for details.

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::GetSketchBlockInstanceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchBlockInstanceCount.html)
[ISketch::IGetSketchBlockInstances Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSketchBlockInstances.html)
[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html)
[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
