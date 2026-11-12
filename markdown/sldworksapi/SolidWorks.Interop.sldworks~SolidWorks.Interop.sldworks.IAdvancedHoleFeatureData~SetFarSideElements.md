---
title: "SetFarSideElements Method (IAdvancedHoleFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedHoleFeatureData"
member: "SetFarSideElements"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData~SetFarSideElements.html"
---

# SetFarSideElements Method (IAdvancedHoleFeatureData)

Sets the far side hole elements in this Advanced Hole.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetFarSideElements( _
   ByVal ElmArray As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedHoleFeatureData
Dim ElmArray As System.Object

instance.SetFarSideElements(ElmArray)
```

### C#

```csharp
void SetFarSideElements(
   System.object ElmArray
)
```

### C++/CLI

```cpp
void SetFarSideElements(
   System.Object^ ElmArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ElmArray`: Array of far side hole elements

## VBA Syntax

See [AdvancedHoleFeatureData::SetFarSideElements](ms-its:sldworksapivb6.chm::/sldworks~AdvancedHoleFeatureData~SetFarSideElements.html).

## Examples

See the [IAdvancedHoleFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksapiprogguide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IAdvancedHoleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData.html)
[IAdvancedHoleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData_members.html)
[IAdvancedHoleFeatureData::GetFarSideElements Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData~GetFarSideElements.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
