---
title: "GetCoordinates Method (IProjectionArrow)"
project: "SOLIDWORKS API Help"
interface: "IProjectionArrow"
member: "GetCoordinates"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~GetCoordinates.html"
---

# GetCoordinates Method (IProjectionArrow)

Gets the location of this projection arrow's line and its label.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCoordinates() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IProjectionArrow
Dim value As System.Object

value = instance.GetCoordinates()
```

### C#

```csharp
System.object GetCoordinates()
```

### C++/CLI

```cpp
System.Object^ GetCoordinates();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of 24 doubles containing starting and ending x,y,z points of the projection arrow and the x,y,z point for its label (see **Remarks**)

## VBA Syntax

See [ProjectionArrow::GetCoordinates](ms-its:sldworksapivb6.chm::/sldworks~ProjectionArrow~GetCoordinates.html).

## Examples

[Get Arrow in Projected View (C#)](Get_Arrow_in_Projected_View_Example_CSharp.htm)
[Get Arrow in Projected View (VB.NET)](Get_Arrow_in_Projected_View_Example_VBNET.htm)
[Get Arrow in Projected View (VBA)](Get_Arrow_in_Projected_View_Example_VB.htm)

## Remarks

The doubles at indexes 0, 1, and 2 are the starting point of the projection arrow; the doubles at indexes 3, 4, and 5 are the ending point of the projection arrow. The doubles at indexes 21, 22, and 23 are the label location. All other doubles in the array are duplicates of these values.

## See Also

[IProjectionArrow Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow.html)
[IProjectionArrow Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow_members.html)
[IProjectionArrow::IGetCoordinates Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~IGetCoordinates.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
