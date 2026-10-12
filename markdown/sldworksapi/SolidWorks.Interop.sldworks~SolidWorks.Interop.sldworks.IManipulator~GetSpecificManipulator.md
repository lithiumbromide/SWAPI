---
title: "GetSpecificManipulator Method (IManipulator)"
project: "SOLIDWORKS API Help"
interface: "IManipulator"
member: "GetSpecificManipulator"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator~GetSpecificManipulator.html"
---

# GetSpecificManipulator Method (IManipulator)

Gets the manipulator for this SOLIDWORKS part or assembly document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSpecificManipulator() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IManipulator
Dim value As System.Object

value = instance.GetSpecificManipulator()
```

### C#

```csharp
System.object GetSpecificManipulator()
```

### C++/CLI

```cpp
System.Object^ GetSpecificManipulator();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- [ITriadManipulator](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITriadManipulator.html)
- [IDragArrowManipulator](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragArrowManipulator.html)
- [IPlaneManipulator](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPlaneManipulator.html)

## VBA Syntax

See [Manipulator::GetSpecificManipulator](ms-its:sldworksapivb6.chm::/sldworks~Manipulator~GetSpecificManipulator.html).

## Examples

[Insert and Use Plane with Manipulator (VBA)](Insert_and_Use_Plane_with_Manipulator_Example_VB.htm)
[Create Triad Manipulator (VBA)](Create_Triad_Manipulator_Example_VB.htm)
[Create Triad Manipulator (VB.NET)](Create_Triad_Manipulator_Example_VBNET.htm)
[Create Triad Manipulator (C#)](Create_Triad_Manipulator_Example_CSharp.htm)

## See Also

[IManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator.html)
[IManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
