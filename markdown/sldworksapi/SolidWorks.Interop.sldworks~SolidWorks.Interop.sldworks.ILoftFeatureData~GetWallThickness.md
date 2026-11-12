---
title: "GetWallThickness Method (ILoftFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftFeatureData"
member: "GetWallThickness"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GetWallThickness.html"
---

# GetWallThickness Method (ILoftFeatureData)

Gets the wall thickness in the specified direction for this loft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetWallThickness( _
   ByVal Forward As System.Boolean _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftFeatureData
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

- `Forward`: True for forward direction, false for reverse

### Return Value

Wall thickness

## VBA Syntax

See [LoftFeatureData::GetWallThickness](ms-its:sldworksapivb6.chm::/sldworks~LoftFeatureData~GetWallThickness.html).

## See Also

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.html)
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.html)
[ILoftFeatureData::IsThinFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~IsThinFeature.html)
[ILoftFeatureData::SetWallThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~SetWallThickness.html)
[ILoftFeatureData::ThinWallType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~ThinWallType.html)

## Availability

SolidWorkls 2001Plus FCS, Revision Number 10.0
