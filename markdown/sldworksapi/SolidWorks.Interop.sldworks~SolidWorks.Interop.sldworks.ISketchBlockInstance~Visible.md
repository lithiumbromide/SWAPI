---
title: "Visible Property (ISketchBlockInstance)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockInstance"
member: "Visible"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~Visible.html"
---

# Visible Property (ISketchBlockInstance)

Gets or sets the visibility of this block instance.

## Syntax

### Visual Basic (Declaration)

```vb
Property Visible As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockInstance
Dim value As System.Integer

instance.Visible = value

value = instance.Visible
```

### C#

```csharp
System.int Visible {get; set;}
```

### C++/CLI

```cpp
property System.int Visible {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Block instance's visibility as defined by [swAnnotationVisibilityState_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAnnotationVisibilityState_e.html)

## VBA Syntax

See [SketchBlockInstance::Visible](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockInstance~Visible.html).

## Examples

[Change Visibility of Sketch Block Instances (C#)](Change_Visibility_of_Sketch_Block_Instances_Example_CSharp.htm)
[Change Visibility of Sketch Block Instances (VB.NET)](Change_Visibility_of_Sketch_Block_Instances_Example_VBNET.htm)
[Change Visibility of Sketch Block Instances (VBA)](Change_Visibility_of_Sketch_Block_Instances_Example_VB.htm)

## See Also

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html)
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.html)

## Availability

SOLIDWORKS 2010 SP3, Revision Number 18.3
