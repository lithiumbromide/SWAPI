---
title: "GetComponentsCount Method (ICavityFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICavityFeatureData"
member: "GetComponentsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~GetComponentsCount.html"
---

# GetComponentsCount Method (ICavityFeatureData)

Gets the number of design components in this cavity feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponentsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICavityFeatureData
Dim value As System.Integer

value = instance.GetComponentsCount()
```

### C#

```csharp
System.int GetComponentsCount()
```

### C++/CLI

```cpp
System.int GetComponentsCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [CavityFeatureData::GetComponentsCount](ms-its:sldworksapivb6.chm::/sldworks~CavityFeatureData~GetComponentsCount.html).

## Remarks

Call this method before calling [ICavityFeatureData::IGetComponents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICavityFeatureData~IGetComponents.html).

## See Also

[ICavityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData.html)
[ICavityFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData_members.html)
[ICavityFeatureData::ISetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~ISetComponents.html)
[ICavityFeatureData::Components Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~Components.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13
