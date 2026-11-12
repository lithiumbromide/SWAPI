---
title: "CreateFormTool Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "CreateFormTool"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFormTool.html"
---

# CreateFormTool Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::CreateFormTool2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~CreateFormTool2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateFormTool() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As Feature

value = instance.CreateFormTool()
```

### C#

```csharp
Feature CreateFormTool()
```

### C++/CLI

```cpp
Feature^ CreateFormTool();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::CreateFormTool](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~CreateFormTool.html).

## Remarks

To insert a forming tool from the Design Library, call [IFeatureManager::InsertFormToolFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertFormToolFeature.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
