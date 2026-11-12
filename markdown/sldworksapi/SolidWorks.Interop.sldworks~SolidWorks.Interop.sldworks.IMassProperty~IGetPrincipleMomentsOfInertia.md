---
title: "IGetPrincipleMomentsOfInertia Method (IMassProperty)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty"
member: "IGetPrincipleMomentsOfInertia"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~IGetPrincipleMomentsOfInertia.html"
---

# IGetPrincipleMomentsOfInertia Method (IMassProperty)

Gets the principal moments of inertia for this model.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetPrincipleMomentsOfInertia() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty
Dim value As System.Double

value = instance.IGetPrincipleMomentsOfInertia()
```

### C#

```csharp
System.double IGetPrincipleMomentsOfInertia()
```

### C++/CLI

```cpp
System.double IGetPrincipleMomentsOfInertia();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of size 3 (see **Remarks**)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

This method returns metric units unless explicitly specified otherwise.

The return value is a 0-based array of doubles:

[ Px, Py, Pz ]

## See Also

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.html)
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.html)
[IMassProperty::GetMomentOfInertia Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~GetMomentOfInertia.html)
[IMassProperty::IGetMomentOfInertia Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~IGetMomentOfInertia.html)
[IMassProperty::IGetPrincipleAxesOfInertia Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~IGetPrincipleAxesOfInertia.html)
[IMassProperty::PrincipleAxesOfInertia Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~PrincipleAxesOfInertia.html)
[IMassProperty::PrincipleMomentsOfInertia Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~PrincipleMomentsOfInertia.html)

## Availability

SOLIDWORKS 2003 SP2, Revision Number 11.2
