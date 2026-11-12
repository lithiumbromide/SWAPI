---
title: "SetNearSideElements Method (IAdvancedHoleFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedHoleFeatureData"
member: "SetNearSideElements"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData~SetNearSideElements.html"
---

# SetNearSideElements Method (IAdvancedHoleFeatureData)

Sets the near side hole elements in this Advanced Hole.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetNearSideElements( _
   ByVal ElmArray As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedHoleFeatureData
Dim ElmArray As System.Object

instance.SetNearSideElements(ElmArray)
```

### C#

```csharp
void SetNearSideElements(
   System.object ElmArray
)
```

### C++/CLI

```cpp
void SetNearSideElements(
   System.Object^ ElmArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ElmArray`: Array of near side hole elements

## VBA Syntax

See [AdvancedHoleFeatureData::SetNearSideElements](ms-its:sldworksapivb6.chm::/sldworks~AdvancedHoleFeatureData~SetNearSideElements.html).

## Examples

See the [IAdvancedHoleFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksapiprogguide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IAdvancedHoleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData.html)
[IAdvancedHoleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData_members.html)
[IAdvancedHoleFeatureData::GetNearSideElements Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData~GetNearSideElements.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
