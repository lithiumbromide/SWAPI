---
title: "PreSplitBody2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "PreSplitBody2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreSplitBody2.html"
---

# PreSplitBody2 Method (IFeatureManager)

Gets all of the bodies created by splitting a part.

## Syntax

### Visual Basic (Declaration)

```vb
Function PreSplitBody2() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As System.Object

value = instance.PreSplitBody2()
```

### C#

```csharp
System.object PreSplitBody2()
```

### C++/CLI

```cpp
System.Object^ PreSplitBody2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) that result from splitting a part (see **Remarks**)

## VBA Syntax

See [FeatureManager::PreSplitBody2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~PreSplitBody2.html).

## Examples

[Create Split Feature (VBA)](Create_Split-body_Feature_Example_VB.htm)
[Create Split Feature (VB.NET)](Create_Split-body_Feature_Example_VBNET.htm)
[Create Split Feature (C#)](Create_Split-body_Feature_Example_CSharp.htm)

## Remarks

The difference between this method and the now obsolete IFeatureManager::PreSplitBody is that this method supports the splitting of surfaces.

To create a Split feature:

1. Select the cutting tools to use to split the part into multiple bodies.
2. Call this method to get all of the split bodies.
3. Create the Split feature using [IFeatureManager::PostSplitBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~PostSplitBody.html).

To find out whether the bodies in a Split feature are consumed, use [ISplitBodyFeatureData::Consume](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplitBodyFeatureData~Consume.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[ISplitBodyFeatureData::GetSplitBodies Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~GetSplitBodies.html)
[ISplitBodyFeatureData::SetSplitBodies2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~SetSplitBodies2.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
