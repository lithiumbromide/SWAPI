---
title: "RevolvePlanarLoop Method (ILoop)"
project: "SOLIDWORKS API Help"
interface: "ILoop"
member: "RevolvePlanarLoop"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop~RevolvePlanarLoop.html"
---

# RevolvePlanarLoop Method (ILoop)

Obsolete. Superseded by [ILoop2::RevolvePlanarLoop](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2~RevolvePlanarLoop.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function RevolvePlanarLoop( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal Axisx As System.Double, _
   ByVal Axisy As System.Double, _
   ByVal Axisz As System.Double, _
   ByVal RevAngle As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILoop
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim Axisx As System.Double
Dim Axisy As System.Double
Dim Axisz As System.Double
Dim RevAngle As System.Double
Dim value As System.Object

value = instance.RevolvePlanarLoop(X, Y, Z, Axisx, Axisy, Axisz, RevAngle)
```

### C#

```csharp
System.object RevolvePlanarLoop(
   System.double X,
   System.double Y,
   System.double Z,
   System.double Axisx,
   System.double Axisy,
   System.double Axisz,
   System.double RevAngle
)
```

### C++/CLI

```cpp
System.Object^ RevolvePlanarLoop(
   System.double X,
   System.double Y,
   System.double Z,
   System.double Axisx,
   System.double Axisy,
   System.double Axisz,
   System.double RevAngle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`:
- `Y`:
- `Z`:
- `Axisx`:
- `Axisy`:
- `Axisz`:
- `RevAngle`:

## VBA Syntax

See [Loop::RevolvePlanarLoop](ms-its:sldworksapivb6.chm::/sldworks~Loop~RevolvePlanarLoop.html).

## See Also

[ILoop Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop.html)
[ILoop Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop_members.html)
