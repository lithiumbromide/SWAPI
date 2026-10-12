---
title: "GetRevolutionAngle Method (IRevolveFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IRevolveFeatureData2"
member: "GetRevolutionAngle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~GetRevolutionAngle.html"
---

# GetRevolutionAngle Method (IRevolveFeatureData2)

Gets the angle of the revolve feature in Direction 1 or Direction 2.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRevolutionAngle( _
   ByVal Forward As System.Boolean _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRevolveFeatureData2
Dim Forward As System.Boolean
Dim value As System.Double

value = instance.GetRevolutionAngle(Forward)
```

### C#

```csharp
System.double GetRevolutionAngle(
   System.bool Forward
)
```

### C++/CLI

```cpp
System.double GetRevolutionAngle(
   System.bool Forward
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`: True gets the angle in Direction 1, false gets the angle in Direction 2

### Return Value

Angle of revolution

## VBA Syntax

See [RevolveFeatureData2::GetRevolutionAngle](ms-its:sldworksapivb6.chm::/sldworks~RevolveFeatureData2~GetRevolutionAngle.html).

## See Also

[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.html)
[IRevolveFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2_members.html)
[IRevolveFeatureData2::SetRevolutionAngle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~SetRevolutionAngle.html)
[IRevolveFeatureData2::ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~ReverseDirection.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
