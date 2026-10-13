---
title: "GetForce Method (IMate2)"
project: "SOLIDWORKS API Help"
interface: "IMate2"
member: "GetForce"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetForce.html"
---

# GetForce Method (IMate2)

Gets the magnitude and direction of the force applied to this mate.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetForce( _
   ByRef Magnitude As System.Double _
) As MathVector
```

### Visual Basic (Usage)

```vb
Dim instance As IMate2
Dim Magnitude As System.Double
Dim value As MathVector

value = instance.GetForce(Magnitude)
```

### C#

```csharp
MathVector GetForce(
   out System.double Magnitude
)
```

### C++/CLI

```cpp
MathVector^ GetForce(
   [Out] System.double Magnitude
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Magnitude`: Magnitude

### Return Value

[Direction](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html)

## VBA Syntax

See [Mate2::GetForce](ms-its:sldworksapivb6.chm::/sldworks~Mate2~GetForce.html).

## See Also

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.html)
[IMate2::SetForce Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetForce.html)
[IMate2::GetTorque Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetTorque.html)
[IMate2::SetTorque Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetTorque.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
