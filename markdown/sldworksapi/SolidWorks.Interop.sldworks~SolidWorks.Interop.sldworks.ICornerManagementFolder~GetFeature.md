---
title: "GetFeature Method (ICornerManagementFolder)"
project: "SOLIDWORKS API Help"
interface: "ICornerManagementFolder"
member: "GetFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder~GetFeature.html"
---

# GetFeature Method (ICornerManagementFolder)

Gets the feature for this corner management folder.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeature() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As ICornerManagementFolder
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

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)

## VBA Syntax

See [CornerManagementFolder::GetFeature](ms-its:sldworksapivb6.chm::/sldworks~CornerManagementFolder~GetFeature.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

## See Also

[ICornerManagementFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html)
[ICornerManagementFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
