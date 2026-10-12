---
title: "GetWallThickness Method (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "GetWallThickness"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetWallThickness.html"
---

# GetWallThickness Method (IExtrudeFeatureData2)

Gets the wall thickness of the thin extrusion feature in forward or reverse direction.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetWallThickness( _
   ByVal Forward As System.Boolean _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
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

See [ExtrudeFeatureData2::GetWallThickness](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~GetWallThickness.html).

## Remarks

This method is relevant only for thin features.

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
[IExtrudeFeatureData2::IsThinFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~IsThinFeature.html)
[IExtrudeFeatureData2::SetWallThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetWallThickness.html)
[IExtrudeFeatureData2::ThinWallType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~ThinWallType.html)
[IExtrudeFeatureData2::CapEnds Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~CapEnds.html)
[IExtrudeFeatureData2::CapThickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~CapThickness.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
