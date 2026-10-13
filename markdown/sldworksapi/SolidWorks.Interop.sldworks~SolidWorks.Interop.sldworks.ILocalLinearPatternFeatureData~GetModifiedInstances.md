---
title: "GetModifiedInstances Method (ILocalLinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalLinearPatternFeatureData"
member: "GetModifiedInstances"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~GetModifiedInstances.html"
---

# GetModifiedInstances Method (ILocalLinearPatternFeatureData)

Gets the instance numbers of all modified instances in this linear component pattern.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetModifiedInstances() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalLinearPatternFeatureData
Dim value As System.Object

value = instance.GetModifiedInstances()
```

### C#

```csharp
System.object GetModifiedInstances()
```

### C++/CLI

```cpp
System.Object^ GetModifiedInstances();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of modified pattern instance numbers

## VBA Syntax

See [LocalLinearPatternFeatureData::GetModifiedInstances](ms-its:sldworksapivb6.chm::/sldworks~LocalLinearPatternFeatureData~GetModifiedInstances.html).

## See Also

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html)
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.html)
[ILocalLinearPatternFeatureData::GetModifiedInstance Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~GetModifiedInstance.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
