---
title: "IsRolledBack Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "IsRolledBack"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsRolledBack.html"
---

# IsRolledBack Method (IFeature)

Gets whether this feature is rolled back.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsRolledBack() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.Boolean

value = instance.IsRolledBack()
```

### C#

```csharp
System.bool IsRolledBack()
```

### C++/CLI

```cpp
System.bool IsRolledBack();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the feature is rolled back, false if not

## VBA Syntax

See [Feature::IsRolledBack](ms-its:sldworksapivb6.chm::/sldworks~Feature~IsRolledBack.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeatureManager::EditRollback Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EditRollback.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
