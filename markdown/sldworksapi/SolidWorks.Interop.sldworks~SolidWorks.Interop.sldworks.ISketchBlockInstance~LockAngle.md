---
title: "LockAngle Property (ISketchBlockInstance)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockInstance"
member: "LockAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~LockAngle.html"
---

# LockAngle Property (ISketchBlockInstance)

Gets or sets whether the angle around the insertion point which to rotate this block instance is locked.

## Syntax

### Visual Basic (Declaration)

```vb
Property LockAngle As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockInstance
Dim value As System.Boolean

instance.LockAngle = value

value = instance.LockAngle
```

### C#

```csharp
System.bool LockAngle {get; set;}
```

### C++/CLI

```cpp
property System.bool LockAngle {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to lock the angle of this block instance, false to not

## VBA Syntax

See [SketchBlockInstance::LockAngle](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockInstance~LockAngle.html).

## See Also

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html)
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.html)
[ISketchBlockInstance::Angle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~Angle.html)
[ISketchBlockInstance::InstancePosition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~InstancePosition.html)
[ISketchBlockDefinition::InsertionPoint Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~InsertionPoint.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
