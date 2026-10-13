---
title: "InsertSaveOutBodies Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertSaveOutBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSaveOutBodies.html"
---

# InsertSaveOutBodies Method (IFeatureManager)

Saves the selected surface bodies or solid bodies or sub-weldments to a file.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertSaveOutBodies() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As System.Boolean

value = instance.InsertSaveOutBodies()
```

### C#

```csharp
System.bool InsertSaveOutBodies()
```

### C++/CLI

```cpp
System.bool InsertSaveOutBodies();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the selected surface bodies or solid bodies or sub-weldments are saved to a file, false if not

## VBA Syntax

See [FeatureManager::InsertSaveOutBodies](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertSaveOutBodies.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
