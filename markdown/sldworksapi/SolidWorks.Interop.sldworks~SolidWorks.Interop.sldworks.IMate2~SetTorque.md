---
title: "SetTorque Method (IMate2)"
project: "SOLIDWORKS API Help"
interface: "IMate2"
member: "SetTorque"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetTorque.html"
---

# SetTorque Method (IMate2)

Sets the angle and the axis of the torque to apply to this mate.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTorque( _
   ByVal Angle As System.Double, _
   ByVal Axis As MathVector _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMate2
Dim Angle As System.Double
Dim Axis As MathVector
Dim value As System.Boolean

value = instance.SetTorque(Angle, Axis)
```

### C#

```csharp
System.bool SetTorque(
   System.double Angle,
   MathVector Axis
)
```

### C++/CLI

```cpp
System.bool SetTorque(
   System.double Angle,
   MathVector^ Axis
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Angle`: Angle
- `Axis`: [Axis](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html)

### Return Value

True if the operation succeeds, false if not

## VBA Syntax

See [Mate2::SetTorque](ms-its:sldworksapivb6.chm::/sldworks~Mate2~SetTorque.html).

## See Also

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.html)
[IMate2::GetTorque Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetTorque.html)
[IMate2::GetForce Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetForce.html)
[IMate2::SetForce Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetForce.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
