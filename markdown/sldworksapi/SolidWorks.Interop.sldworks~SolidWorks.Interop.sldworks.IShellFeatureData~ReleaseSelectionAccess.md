---
title: "ReleaseSelectionAccess Method (IShellFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IShellFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (IShellFeatureData)

Releases access to the selections used to define this shell feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As IShellFeatureData

instance.ReleaseSelectionAccess()
```

### C#

```csharp
void ReleaseSelectionAccess()
```

### C++/CLI

```cpp
void ReleaseSelectionAccess();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ShellFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~ShellFeatureData~ReleaseSelectionAccess.html).

## Examples

See the [IShellFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData.html) examples.

## Remarks

[IShellFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IShellFeatureData~AccessSelections.html) and [IShellFeatureData::IAccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IShellFeatureData~IAccessSelections.html) put the model in a rollback state to allow access to the selections that define the feature.

Use this method to restore the rollback state if you did not modify the feature, or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you did modify the feature.

## See Also

[IShellFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData.html)
[IShellFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
