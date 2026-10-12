---
title: "IGetCoordinates Method (IProjectionArrow)"
project: "SOLIDWORKS API Help"
interface: "IProjectionArrow"
member: "IGetCoordinates"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~IGetCoordinates.html"
---

# IGetCoordinates Method (IProjectionArrow)

Gets the location of this projection arrow's line and its label.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetCoordinates() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IProjectionArrow
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

- in-process, unmanaged C++: Pointer to an array of 24 doubles containing starting and ending x,y,z points of the projection arrow and the x,y,z point of its label (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The doubles at indexes 0, 1, and 2 are the starting point of the projection arrow; the doubles at indexes 3, 4, and 5 are the ending point of the projection arrow. The doubles at indexes 21, 22, and 23 are the label location. All other doubles in the array are duplicates of these values.

## See Also

[IProjectionArrow Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow.html)
[IProjectionArrow Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow_members.html)
[IProjectionArrow::GetCoordinates Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~GetCoordinates.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
