---
title: "SetBreakCorners Method (IFlatPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFlatPatternFeatureData"
member: "SetBreakCorners"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~SetBreakCorners.html"
---

# SetBreakCorners Method (IFlatPatternFeatureData)

Sets whether to add break corners to the Flat-Pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetBreakCorners( _
   ByVal BBreakCorner As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IFlatPatternFeatureData
Dim BBreakCorner As System.Boolean

instance.SetBreakCorners(BBreakCorner)
```

### C#

```csharp
void SetBreakCorners(
   System.bool BBreakCorner
)
```

### C++/CLI

```cpp
void SetBreakCorners(
   System.bool BBreakCorner
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BBreakCorner`: True to add break corners, false to not

## VBA Syntax

See [FlatPatternFeatureData::SetBreakCorners](ms-its:sldworksapivb6.chm::/sldworks~FlatPatternFeatureData~SetBreakCorners.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.html)
[IFlatPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData_members.html)
[IFlatPatternFeatureData::GetBreakCorners Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~GetBreakCorners.html)
[IFlatPatternFeatureData::BreakCornerRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~BreakCornerRadius.html)
[IFlatPatternFeatureData::BreakCornerType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~BreakCornerType.html)
[IBreakCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
