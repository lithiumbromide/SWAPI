---
title: "GetFeature Method (IWeldmentCutListFeature)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentCutListFeature"
member: "GetFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~GetFeature.html"
---

# GetFeature Method (IWeldmentCutListFeature)

Gets the feature for this weldment cut list table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeature() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentCutListFeature
Dim value As Feature

value = instance.GetFeature()
```

### C#

```csharp
Feature GetFeature()
```

### C++/CLI

```cpp
Feature^ GetFeature();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) for this weldment cut list table

## VBA Syntax

See [WeldmentCutListFeature::GetFeature](ms-its:sldworksapivb6.chm::/sldworks~WeldmentCutListFeature~GetFeature.html).

## See Also

[IWeldmentCutListFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature.html)
[IWeldmentCutListFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
