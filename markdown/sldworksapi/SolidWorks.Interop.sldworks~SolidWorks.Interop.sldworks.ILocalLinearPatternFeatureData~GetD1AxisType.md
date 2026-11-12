---
title: "GetD1AxisType Method (ILocalLinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalLinearPatternFeatureData"
member: "GetD1AxisType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~GetD1AxisType.html"
---

# GetD1AxisType Method (ILocalLinearPatternFeatureData)

Gets the type of axis used for Direction 1 in this linear component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetD1AxisType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalLinearPatternFeatureData
Dim value As System.Integer

value = instance.GetD1AxisType()
```

### C#

```csharp
System.int GetD1AxisType()
```

### C++/CLI

```cpp
System.int GetD1AxisType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Type of axis as defined in [swPatternReferenceTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPatternReferenceTypes_e.html)

## VBA Syntax

See [LocalLinearPatternFeatureData::GetD1AxisType](ms-its:sldworksapivb6.chm::/sldworks~LocalLinearPatternFeatureData~GetD1AxisType.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html)
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.html)
[ILocalLinearPatternFeatureData::GetD2AxisType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~GetD2AxisType.html)
[ILocalLinearPatternFeatureData::D1Axis Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1Axis.html)
[ILocalLinearPatternFeatureData::D1ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1ReverseDirection.html)
[ILocalLinearPatternFeatureData::D1Spacing Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1Spacing.html)
[ILocalLinearPatternFeatureData::D1TotalInstances Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1TotalInstances.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
