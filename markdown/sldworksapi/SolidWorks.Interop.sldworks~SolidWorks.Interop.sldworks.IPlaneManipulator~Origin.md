---
title: "Origin Property (IPlaneManipulator)"
project: "SOLIDWORKS API Help"
interface: "IPlaneManipulator"
member: "Origin"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator~Origin.html"
---

# Origin Property (IPlaneManipulator)

Gets or sets the origin of the plane.

## Syntax

### Visual Basic (Declaration)

```vb
Property Origin As MathPoint
```

### Visual Basic (Usage)

```vb
Dim instance As IPlaneManipulator
Dim value As MathPoint

instance.Origin = value

value = instance.Origin
```

### C#

```csharp
MathPoint Origin {get; set;}
```

### C++/CLI

```cpp
property MathPoint^ Origin {
   MathPoint^ get();
   void set (    MathPoint^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Origin](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html)

## VBA Syntax

See [PlaneManipulator::Origin](ms-its:sldworksapivb6.chm::/sldworks~PlaneManipulator~Origin.html).

## Remarks

If a plane with a manipulator is already displayed, then do not set a new [normal-to vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPlaneManipulator~Normal.html) or origin for that plane.

## See Also

[IPlaneManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator.html)
[IPlaneManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
