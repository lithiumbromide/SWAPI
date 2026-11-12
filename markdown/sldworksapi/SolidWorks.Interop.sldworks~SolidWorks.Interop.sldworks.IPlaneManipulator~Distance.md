---
title: "Distance Property (IPlaneManipulator)"
project: "SOLIDWORKS API Help"
interface: "IPlaneManipulator"
member: "Distance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator~Distance.html"
---

# Distance Property (IPlaneManipulator)

Gets or sets the distance to move a plane that has a manipulator.

## Syntax

### Visual Basic (Declaration)

```vb
Property Distance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IPlaneManipulator
Dim value As System.Double

instance.Distance = value

value = instance.Distance
```

### C#

```csharp
System.double Distance {get; set;}
```

### C++/CLI

```cpp
property System.double Distance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance to move a plane that has a manipulator

## VBA Syntax

See [PlaneManipulator::Distance](ms-its:sldworksapivb6.chm::/sldworks~PlaneManipulator~Distance.html).

## Examples

[Insert and Use Plane with Manipulator (VBA)](Insert_and_Use_Plane_with_Manipulator_Example_VB.htm)
[Insert and Use Plane with Manipulator (C#)](Insert_and_Use_Plane_with_Manipulator_Example_CSharp.htm)
[Insert and Use Plane with Manipulator (VB.NET)](Insert_and_Use_Plane_with_Manipulator_Example_VBNET.htm)

## See Also

[IPlaneManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator.html)
[IPlaneManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
