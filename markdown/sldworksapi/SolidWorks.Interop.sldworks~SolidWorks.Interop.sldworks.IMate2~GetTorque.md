---
title: "GetTorque Method (IMate2)"
project: "SOLIDWORKS API Help"
interface: "IMate2"
member: "GetTorque"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetTorque.html"
---

# GetTorque Method (IMate2)

Gets the angle and the axis of the torque applied to this mate.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTorque( _
   ByRef Angle As System.Double _
) As MathVector
```

### Visual Basic (Usage)

```vb
Dim instance As IMate2
Dim Angle As System.Double
Dim value As MathVector

value = instance.GetTorque(Angle)
```

### C#

```csharp
MathVector GetTorque(
   out System.double Angle
)
```

### C++/CLI

```cpp
MathVector^ GetTorque(
   [Out] System.double Angle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Angle`: Angle

### Return Value

[Axis](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html)

## VBA Syntax

See [Mate2::GetTorque](ms-its:sldworksapivb6.chm::/sldworks~Mate2~GetTorque.html).

## See Also

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.html)
[IMate2::SetTorque Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetTorque.html)
[IMate2::GetForce Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetForce.html)
[IMate2::SetForce Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetForce.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
