---
title: "GetWallThickness Method (IRevolveFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IRevolveFeatureData2"
member: "GetWallThickness"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~GetWallThickness.html"
---

# GetWallThickness Method (IRevolveFeatureData2)

Gets the wall thickness of the thin revolution feature in forward or reverse direction.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetWallThickness( _
   ByVal Forward As System.Boolean _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRevolveFeatureData2
Dim Forward As System.Boolean
Dim value As System.Double

value = instance.GetWallThickness(Forward)
```

### C#

```csharp
System.double GetWallThickness(
   System.bool Forward
)
```

### C++/CLI

```cpp
System.double GetWallThickness(
   System.bool Forward
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`: True for forward feature direction, false for reverse

### Return Value

Wall thickness

## VBA Syntax

See [RevolveFeatureData2::GetWallThickness](ms-its:sldworksapivb6.chm::/sldworks~RevolveFeatureData2~GetWallThickness.html).

## Remarks

This method only affects thin features.

## See Also

[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.html)
[IRevolveFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2_members.html)
[IRevolveFeatureData2::IsThinFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~IsThinFeature.html)
[IRevolveFeatureData2::SetWallThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~SetWallThickness.html)
[IRevolveFeatureData2::ThinWallType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~ThinWallType.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
