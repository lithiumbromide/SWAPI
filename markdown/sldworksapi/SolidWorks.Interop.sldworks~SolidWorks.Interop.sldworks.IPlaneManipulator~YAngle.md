---
title: "YAngle Property (IPlaneManipulator)"
project: "SOLIDWORKS API Help"
interface: "IPlaneManipulator"
member: "YAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator~YAngle.html"
---

# YAngle Property (IPlaneManipulator)

Gets or sets the y coordinate of the angle to use to rotate a plane that has a manipulator.

## Syntax

### Visual Basic (Declaration)

```vb
Property YAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IPlaneManipulator
Dim value As System.Double

instance.YAngle = value

value = instance.YAngle
```

### C#

```csharp
System.double YAngle {get; set;}
```

### C++/CLI

```cpp
property System.double YAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

y coordinate of the angle to use to rotate a plane that has a manipulator

## VBA Syntax

See [PlaneManipulator::YAngle](ms-its:sldworksapivb6.chm::/sldworks~PlaneManipulator~YAngle.html).

## Examples

[Insert and Use Plane with Manipulator (VBA)](Insert_and_Use_Plane_with_Manipulator_Example_VB.htm)
[Insert and Use Plane with Manipulator (C#)](Insert_and_Use_Plane_with_Manipulator_Example_CSharp.htm)
[Insert and Use Plane with Manipulator (VB.NET)](Insert_and_Use_Plane_with_Manipulator_Example_VBNET.htm)

## See Also

[IPlaneManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator.html)
[IPlaneManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator_members.html)
[IPlaneManipulator::XAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator~XAngle.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
