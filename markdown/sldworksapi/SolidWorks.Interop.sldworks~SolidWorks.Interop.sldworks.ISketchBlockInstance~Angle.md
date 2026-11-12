---
title: "Angle Property (ISketchBlockInstance)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockInstance"
member: "Angle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~Angle.html"
---

# Angle Property (ISketchBlockInstance)

Gets or sets the angle around the insertion point which to rotate this block instance.

## Syntax

### Visual Basic (Declaration)

```vb
Property Angle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockInstance
Dim value As System.Double

instance.Angle = value

value = instance.Angle
```

### C#

```csharp
System.double Angle {get; set;}
```

### C++/CLI

```cpp
property System.double Angle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Angle in radians

## VBA Syntax

See [SketchBlockInstance::Angle](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockInstance~Angle.html).

## Examples

[Get and Set Blocks Data in Any Document (VBA)](Get_and_Set_Blocks_Data_in_Any_Document_Example_VB.htm)
[Get Block Information (VBA)](Get_Block_Information_Example_VB.htm)

## Remarks

You must be editing the block's sketch to change the angle.

## See Also

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html)
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.html)
[ISketchBlockInstance::LockAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~LockAngle.html)
[ISketchBlockInstance::InstancePosition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~InstancePosition.html)
[ISketchBlockDefinition::InsertionPoint Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~InsertionPoint.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
