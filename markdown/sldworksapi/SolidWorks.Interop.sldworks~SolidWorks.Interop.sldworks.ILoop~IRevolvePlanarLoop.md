---
title: "IRevolvePlanarLoop Method (ILoop)"
project: "SOLIDWORKS API Help"
interface: "ILoop"
member: "IRevolvePlanarLoop"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop~IRevolvePlanarLoop.html"
---

# IRevolvePlanarLoop Method (ILoop)

Obsolete. Superseded by [ILoop2::IRevolvePlanarLoop](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2~IRevolvePlanarLoop.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IRevolvePlanarLoop( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal Axisx As System.Double, _
   ByVal Axisy As System.Double, _
   ByVal Axisz As System.Double, _
   ByVal RevAngle As System.Double, _
   ByRef StopFacesOut As Face _
) As Body
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
Dim StopFacesOut As Face
Dim value As Body

value = instance.IRevolvePlanarLoop(X, Y, Z, Axisx, Axisy, Axisz, RevAngle, StopFacesOut)
```

### C#

```csharp
Body IRevolvePlanarLoop(
   System.double X,
   System.double Y,
   System.double Z,
   System.double Axisx,
   System.double Axisy,
   System.double Axisz,
   System.double RevAngle,
   ref Face StopFacesOut
)
```

### C++/CLI

```cpp
Body^ IRevolvePlanarLoop(
   System.double X,
   System.double Y,
   System.double Z,
   System.double Axisx,
   System.double Axisy,
   System.double Axisz,
   System.double RevAngle,
   Face^% StopFacesOut
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
- `StopFacesOut`:

## VBA Syntax

See [Loop::IRevolvePlanarLoop](ms-its:sldworksapivb6.chm::/sldworks~Loop~IRevolvePlanarLoop.html).

## See Also

[ILoop Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop.html)
[ILoop Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop_members.html)
