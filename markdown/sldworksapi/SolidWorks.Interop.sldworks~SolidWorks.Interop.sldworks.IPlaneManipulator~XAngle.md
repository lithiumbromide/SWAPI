---
title: "XAngle Property (IPlaneManipulator)"
project: "SOLIDWORKS API Help"
interface: "IPlaneManipulator"
member: "XAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator~XAngle.html"
---

# XAngle Property (IPlaneManipulator)

Gets or sets the x coordinate of the angle to use to rotate a plane that has a manipulator.

## Syntax

### Visual Basic (Declaration)

```vb
Property XAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IPlaneManipulator
Dim value As System.Double

instance.XAngle = value

value = instance.XAngle
```

### C#

```csharp
System.double XAngle {get; set;}
```

### C++/CLI

```cpp
property System.double XAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

x coordinate of the angle to use to rotate a plane that has a manipulator

## VBA Syntax

See [PlaneManipulator::XAngle](ms-its:sldworksapivb6.chm::/sldworks~PlaneManipulator~XAngle.html).

## Examples

[Insert and Use Plane with Manipulator (VBA)](Insert_and_Use_Plane_with_Manipulator_Example_VB.htm)
[Insert and Use Plane with Manipulator (C#)](Insert_and_Use_Plane_with_Manipulator_Example_CSharp.htm)
[Insert and Use Plane with Manipulator (VB.NET)](Insert_and_Use_Plane_with_Manipulator_Example_VBNET.htm)

## See Also

[IPlaneManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator.html)
[IPlaneManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator_members.html)
[IPlaneManipulator::YAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator~YAngle.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
