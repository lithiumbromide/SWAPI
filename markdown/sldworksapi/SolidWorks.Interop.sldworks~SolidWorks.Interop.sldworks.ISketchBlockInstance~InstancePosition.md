---
title: "InstancePosition Property (ISketchBlockInstance)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockInstance"
member: "InstancePosition"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~InstancePosition.html"
---

# InstancePosition Property (ISketchBlockInstance)

Gets or sets the position for this block instance.

## Syntax

### Visual Basic (Declaration)

```vb
Property InstancePosition As MathPoint
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockInstance
Dim value As MathPoint

instance.InstancePosition = value

value = instance.InstancePosition
```

### C#

```csharp
MathPoint InstancePosition {get; set;}
```

### C++/CLI

```cpp
property MathPoint^ InstancePosition {
   MathPoint^ get();
   void set (    MathPoint^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Position](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) of this block instance

## VBA Syntax

See [SketchBlockInstance::InstancePosition](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockInstance~InstancePosition.html).

## Examples

[Get and Set Blocks Data in Any Document (VBA)](Get_and_Set_Blocks_Data_in_Any_Document_Example_VB.htm)

## See Also

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html)
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.html)
[ISketchBlockDefinition::InsertionPoint Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~InsertionPoint.html)
[ISketchBlockInstance::Angle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~Angle.html)
[ISketchBlockInstance::LockAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~LockAngle.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
