---
title: "GetBreakCorners Method (IFlatPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFlatPatternFeatureData"
member: "GetBreakCorners"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~GetBreakCorners.html"
---

# GetBreakCorners Method (IFlatPatternFeatureData)

Gets whether to add break corners to the Flat-Pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBreakCorners( _
   ByRef PFeat As Feature _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFlatPatternFeatureData
Dim PFeat As Feature
Dim value As System.Boolean

value = instance.GetBreakCorners(PFeat)
```

### C#

```csharp
System.bool GetBreakCorners(
   out Feature PFeat
)
```

### C++/CLI

```cpp
System.bool GetBreakCorners(
   [Out] Feature^ PFeat
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PFeat`: Flat-Pattern [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

### Return Value

True to add break corners, false to not

## VBA Syntax

See [FlatPatternFeatureData::GetBreakCorners](ms-its:sldworksapivb6.chm::/sldworks~FlatPatternFeatureData~GetBreakCorners.html).

## See Also

[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.html)
[IFlatPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData_members.html)
[IFlatPatternFeatureData::SetBreakCorners Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~SetBreakCorners.html)
[IFlatPatternFeatureData::BreakCornerRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~BreakCornerRadius.html)
[IFlatPatternFeatureData::BreakCornerType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~BreakCornerType.html)
[IBreakCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
