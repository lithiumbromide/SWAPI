---
title: "SetRevolutionAngle Method (IRevolveFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IRevolveFeatureData2"
member: "SetRevolutionAngle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~SetRevolutionAngle.html"
---

# SetRevolutionAngle Method (IRevolveFeatureData2)

Sets the angle of the revolve feature in Direction 1 or Direction 2.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetRevolutionAngle( _
   ByVal Forward As System.Boolean, _
   ByVal Angle As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRevolveFeatureData2
Dim Forward As System.Boolean
Dim Angle As System.Double

instance.SetRevolutionAngle(Forward, Angle)
```

### C#

```csharp
void SetRevolutionAngle(
   System.bool Forward,
   System.double Angle
)
```

### C++/CLI

```cpp
void SetRevolutionAngle(
   System.bool Forward,
   System.double Angle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`: True sets the angle in Direction 1, false sets the angle in Direction 2
- `Angle`: Angle of revolution

## VBA Syntax

See [RevolveFeatureData2::SetRevolutionAngle](ms-its:sldworksapivb6.chm::/sldworks~RevolveFeatureData2~SetRevolutionAngle.html).

## See Also

[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.html)
[IRevolveFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2_members.html)
[IRevolveFeatureData2::GetRevolutionAngle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~GetRevolutionAngle.html)
[IRevolveFeatureData2::ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~ReverseDirection.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
