---
title: "Normal Property (IPlaneManipulator)"
project: "SOLIDWORKS API Help"
interface: "IPlaneManipulator"
member: "Normal"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator~Normal.html"
---

# Normal Property (IPlaneManipulator)

Gets or sets the normal-to vector for a plane that has a manipulator.

## Syntax

### Visual Basic (Declaration)

```vb
Property Normal As MathVector
```

### Visual Basic (Usage)

```vb
Dim instance As IPlaneManipulator
Dim value As MathVector

instance.Normal = value

value = instance.Normal
```

### C#

```csharp
MathVector Normal {get; set;}
```

### C++/CLI

```cpp
property MathVector^ Normal {
   MathVector^ get();
   void set (    MathVector^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Normal-to vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html)

## VBA Syntax

See [PlaneManipulator::Normal](ms-its:sldworksapivb6.chm::/sldworks~PlaneManipulator~Normal.html).

## Remarks

If a plane with a manipulator is already displayed, then do not set a new normal-to vector or [origin](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPlaneManipulator~Origin.html) for that plane.

## See Also

[IPlaneManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator.html)
[IPlaneManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
