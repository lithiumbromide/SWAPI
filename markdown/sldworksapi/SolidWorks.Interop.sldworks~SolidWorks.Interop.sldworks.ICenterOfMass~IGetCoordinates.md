---
title: "IGetCoordinates Method (ICenterOfMass)"
project: "SOLIDWORKS API Help"
interface: "ICenterOfMass"
member: "IGetCoordinates"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterOfMass~IGetCoordinates.html"
---

# IGetCoordinates Method (ICenterOfMass)

Gets the coordinates of this center of mass.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetCoordinates() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICenterOfMass
Dim value As System.Double

value = instance.IGetCoordinates()
```

### C#

```csharp
System.double IGetCoordinates()
```

### C++/CLI

```cpp
System.double IGetCoordinates();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles of the x, y, and z coordinates of the center of mass
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[ICenterOfMass Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterOfMass.html)
[ICenterOfMass Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterOfMass_members.html)
[ICenterOfMass::GetCoordinates Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterOfMass~GetCoordinates.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
