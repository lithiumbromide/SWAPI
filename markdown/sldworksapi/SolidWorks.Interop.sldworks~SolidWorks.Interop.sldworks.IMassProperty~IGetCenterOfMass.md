---
title: "IGetCenterOfMass Method (IMassProperty)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty"
member: "IGetCenterOfMass"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~IGetCenterOfMass.html"
---

# IGetCenterOfMass Method (IMassProperty)

Gets the center of mass for this model.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetCenterOfMass() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty
Dim value As System.Double

value = instance.IGetCenterOfMass()
```

### C#

```csharp
System.double IGetCenterOfMass()
```

### C++/CLI

```cpp
System.double IGetCenterOfMass();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of size 3 (see **Remarks**)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

This method returns metric units unless explicitly specified otherwise.

The return value is a 0-based array of doubles as follows:

[ X, Y, Z ]

## See Also

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.html)
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.html)
[IMassProperty::CenterOfMass Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~CenterOfMass.html)

## Availability

SOLIDWORKS 2003 SP2, Revision Number 11.2
