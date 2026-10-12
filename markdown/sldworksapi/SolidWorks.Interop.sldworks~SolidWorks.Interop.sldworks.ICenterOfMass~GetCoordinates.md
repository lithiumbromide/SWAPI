---
title: "GetCoordinates Method (ICenterOfMass)"
project: "SOLIDWORKS API Help"
interface: "ICenterOfMass"
member: "GetCoordinates"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterOfMass~GetCoordinates.html"
---

# GetCoordinates Method (ICenterOfMass)

Gets the coordinates of this center of mass.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCoordinates() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICenterOfMass
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

Array of doubles of the x, y, and z coordinates of the center of mass

## VBA Syntax

See [CenterOfMass::GetCoordinates](ms-its:sldworksapivb6.chm::/sldworks~CenterOfMass~GetCoordinates.html).

## Examples

[Get Centers of Mass in Drawing Views (VBA)](Get_Centers_of_Mass_in_Drawing_Views_Example_VB.htm)
[Get Centers of Mass in Drawing Views (VB.NET)](Get_Centers_of_Mass_in_Drawing_Views_Example_VBNET.htm)
[Get Centers of Mass in Drawing Views (C#)](Get_Centers_of_Mass_in_Drawing_Views_Example_CSharp.htm)

## See Also

[ICenterOfMass Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterOfMass.html)
[ICenterOfMass Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterOfMass_members.html)
[ICenterOfMass::IGetCoordinates Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterOfMass~IGetCoordinates.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
