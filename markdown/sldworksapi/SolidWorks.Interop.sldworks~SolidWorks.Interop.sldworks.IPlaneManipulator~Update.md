---
title: "Update Method (IPlaneManipulator)"
project: "SOLIDWORKS API Help"
interface: "IPlaneManipulator"
member: "Update"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator~Update.html"
---

# Update Method (IPlaneManipulator)

Updates a plane that has a manipulator after modifying it.

## Syntax

### Visual Basic (Declaration)

```vb
Function Update() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPlaneManipulator
Dim value As System.Boolean

value = instance.Update()
```

### C#

```csharp
System.bool Update()
```

### C++/CLI

```cpp
System.bool Update();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if a plane that has a manipulator is updated after being modified, false if not

## VBA Syntax

See [PlaneManipulator::Update](ms-its:sldworksapivb6.chm::/sldworks~PlaneManipulator~Update.html).

## Examples

[Insert and Use Plane with Manipulator (VBA)](Insert_and_Use_Plane_with_Manipulator_Example_VB.htm)
[Insert and Use Plane with Manipulator (C#)](Insert_and_Use_Plane_with_Manipulator_Example_CSharp.htm)
[Insert and Use Plane with Manipulator (VB.NET)](Insert_and_Use_Plane_with_Manipulator_Example_VBNET.htm)

## See Also

[IPlaneManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator.html)
[IPlaneManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
