---
title: "SetForce Method (IMate2)"
project: "SOLIDWORKS API Help"
interface: "IMate2"
member: "SetForce"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetForce.html"
---

# SetForce Method (IMate2)

Sets the magnitude and direction of the force to apply to this mate.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetForce( _
   ByVal Magnitude As System.Double, _
   ByVal Direction As MathVector _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMate2
Dim Magnitude As System.Double
Dim Direction As MathVector
Dim value As System.Boolean

value = instance.SetForce(Magnitude, Direction)
```

### C#

```csharp
System.bool SetForce(
   System.double Magnitude,
   MathVector Direction
)
```

### C++/CLI

```cpp
System.bool SetForce(
   System.double Magnitude,
   MathVector^ Direction
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Magnitude`: Magnitude
- `Direction`: [Direction](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html)

### Return Value

True if the operation succeeds, false if not

## VBA Syntax

See [Mate2::SetForce](ms-its:sldworksapivb6.chm::/sldworks~Mate2~SetForce.html).

## See Also

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.html)
[IMate2::GetForce Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetForce.html)
[IMate2::GetTorque Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetTorque.html)
[IMate2::SetTorque Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetTorque.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
