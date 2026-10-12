---
title: "IGetPrincipleAxesOfInertia Method (IMassProperty)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty"
member: "IGetPrincipleAxesOfInertia"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~IGetPrincipleAxesOfInertia.html"
---

# IGetPrincipleAxesOfInertia Method (IMassProperty)

Gets the principal axes of inertia for this model.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetPrincipleAxesOfInertia( _
   ByVal Axis As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty
Dim Axis As System.Integer
Dim value As System.Double

value = instance.IGetPrincipleAxesOfInertia(Axis)
```

### C#

```csharp
System.double IGetPrincipleAxesOfInertia(
   System.int Axis
)
```

### C++/CLI

```cpp
System.double IGetPrincipleAxesOfInertia(
   System.int Axis
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Axis`: - 0 = X axis
  - 1 = Y axis
  - 2 = Z axis

### Return Value

- in-process, unmanaged C++: Pointer to an array of size 3 (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

This method returns:

- a vector that represents the requested axis.
- metric units unless explicitly specified otherwise.

The return value is a 0-based array of doubles:

[ lx, ly, lz ]

## See Also

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.html)
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.html)
[IMassProperty::GetMomentOfInertia Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~GetMomentOfInertia.html)
[IMassProperty::IGetMomentOfInertia Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~IGetMomentOfInertia.html)
[IMassProperty::IGetPrincipleMomentsOfInertia Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~IGetPrincipleMomentsOfInertia.html)
[IMassProperty::PrincipleAxesOfInertia Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~PrincipleAxesOfInertia.html)
[IMassProperty::PrincipleMomentsOfInertia Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~PrincipleMomentsOfInertia.html)

## Availability

SOLIDWORKS 2003 SP2, Revision Number 11.2
