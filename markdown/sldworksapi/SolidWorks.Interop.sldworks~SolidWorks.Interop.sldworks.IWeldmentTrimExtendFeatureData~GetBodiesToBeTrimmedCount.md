---
title: "GetBodiesToBeTrimmedCount Method (IWeldmentTrimExtendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentTrimExtendFeatureData"
member: "GetBodiesToBeTrimmedCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~GetBodiesToBeTrimmedCount.html"
---

# GetBodiesToBeTrimmedCount Method (IWeldmentTrimExtendFeatureData)

Gets the number of bodies to trim.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBodiesToBeTrimmedCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentTrimExtendFeatureData
Dim value As System.Integer

value = instance.GetBodiesToBeTrimmedCount()
```

### C#

```csharp
System.int GetBodiesToBeTrimmedCount()
```

### C++/CLI

```cpp
System.int GetBodiesToBeTrimmedCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of bodies to trim

## VBA Syntax

See [WeldmentTrimExtendFeatureData::GetBodiesToBeTrimmedCount](ms-its:sldworksapivb6.chm::/sldworks~WeldmentTrimExtendFeatureData~GetBodiesToBeTrimmedCount.html).

## Remarks

Only end-trim corner types (swEndConditionTrim) can have multiple bodies to trim. Use [IWeldmentTrimExtendFeatureData::CornerType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentTrimExtendFeatureData~CornerType.html) to determine the type of corner.

Call this method before calling [IWeldmentTrimExtendFeatureData::IGetBodiesToBeTrimmed](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentTrimExtendFeatureData~IGetBodiesToBeTrimmed.html) to get the size of the array for that method.

## See Also

[IWeldmentTrimExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData.html)
[IWeldmentTrimExtendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData_members.html)
[IWeldmentTrimExtendFeatureData::ISetTrimmingBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~ISetTrimmingBoundary.html)
[IWeldmentTrimExtendFeatureData::BodiesToBeTrimmed Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~BodiesToBeTrimmed.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
