---
title: "PreSplitBody Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "PreSplitBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreSplitBody.html"
---

# PreSplitBody Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::PreSplitBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~PreSplitBody2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function PreSplitBody() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As System.Object

value = instance.PreSplitBody()
```

### C#

```csharp
System.object PreSplitBody()
```

### C++/CLI

```cpp
System.Object^ PreSplitBody();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) that result from splitting a body

## VBA Syntax

See [FeatureManager::PreSplitBody](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~PreSplitBody.html).

## Remarks

To create a split-body feature:

1. Select the cutting tools.
2. Call this method to get all of the bodies that will result from the split operation.
3. Create the split-body feature using [IFeatureManager::PostSplitBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~PostSplitBody.html).

To find out if the bodies in a split-body feature were consumed, use [ISplitBodyFeatureData::Consume](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplitBodyFeatureData.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
