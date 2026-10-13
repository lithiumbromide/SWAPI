---
title: "GetModifiedInstances Method (ILocalCircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalCircularPatternFeatureData"
member: "GetModifiedInstances"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~GetModifiedInstances.html"
---

# GetModifiedInstances Method (ILocalCircularPatternFeatureData)

Gets the instance numbers of all modified instances in this circular component pattern.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetModifiedInstances() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalCircularPatternFeatureData
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

See [LocalCircularPatternFeatureData::GetModifiedInstances](ms-its:sldworksapivb6.chm::/sldworks~LocalCircularPatternFeatureData~GetModifiedInstances.html).

## See Also

[ILocalCircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.html)
[ILocalCircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData_members.html)
[ILocalCircularPatternFeatureData::GetModifiedInstance Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~GetModifiedInstance.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
