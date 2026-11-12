---
title: "InsertDeleteBody Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertDeleteBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertDeleteBody.html"
---

# InsertDeleteBody Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::InsertDeleteBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertDeleteBody2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertDeleteBody() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As Feature

value = instance.InsertDeleteBody()
```

### C#

```csharp
Feature InsertDeleteBody()
```

### C++/CLI

```cpp
Feature^ InsertDeleteBody();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::InsertDeleteBody](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertDeleteBody.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IDeleteBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
