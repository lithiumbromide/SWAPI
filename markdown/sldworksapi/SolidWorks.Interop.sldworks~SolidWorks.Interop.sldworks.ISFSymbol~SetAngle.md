---
title: "SetAngle Method (ISFSymbol)"
project: "SOLIDWORKS API Help"
interface: "ISFSymbol"
member: "SetAngle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~SetAngle.html"
---

# SetAngle Method (ISFSymbol)

Sets the angle for this surface finish symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetAngle( _
   ByVal Angle As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISFSymbol
Dim Angle As System.Double
Dim value As System.Boolean

value = instance.SetAngle(Angle)
```

### C#

```csharp
System.bool SetAngle(
   System.double Angle
)
```

### C++/CLI

```cpp
System.bool SetAngle(
   System.double Angle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Angle`: Angle in radians

### Return Value

True if the angle is set, false if it is not

## VBA Syntax

See [SFSymbol::SetAngle](ms-its:sldworksapivb6.chm::/sldworks~SFSymbol~SetAngle.html).

## Remarks

This method automatically sets the orientation to swSFOrientation_UserDefined. See [ISFSymbol::Orientation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~Orientation.html) for details.

Use [ISFSymbol::GetAngle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~GetAngle.html) to get the angle of the symbol.

## See Also

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.html)
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
