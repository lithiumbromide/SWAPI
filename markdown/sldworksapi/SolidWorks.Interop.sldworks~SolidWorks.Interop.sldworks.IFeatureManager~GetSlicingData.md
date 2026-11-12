---
title: "GetSlicingData Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "GetSlicingData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetSlicingData.html"
---

# GetSlicingData Method (IFeatureManager)

Gets a new slicing data object with default parameter values.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSlicingData() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As System.Object

value = instance.GetSlicingData()
```

### C#

```csharp
System.object GetSlicingData()
```

### C++/CLI

```cpp
System.Object^ GetSlicingData();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[ISlicingData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.html)

## VBA Syntax

See [FeatureManager::GetSlicingData](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~GetSlicingData.html).

## Examples

See the [ISlicingData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.html) example.

## Remarks

Before calling this method to access default slicing parameters, you must pre-select the first reference entity/entities for slicing.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::InsertSlicing Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSlicing.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
