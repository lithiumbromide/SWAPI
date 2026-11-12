---
title: "GetFeature Method (IStructureSystemFolder)"
project: "SOLIDWORKS API Help"
interface: "IStructureSystemFolder"
member: "GetFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemFolder~GetFeature.html"
---

# GetFeature Method (IStructureSystemFolder)

Gets the feature for this structure system folder.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeature() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IStructureSystemFolder
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

See [StructureSystemFolder::GetFeature](ms-its:sldworksapivb6.chm::/sldworks~StructureSystemFolder~GetFeature.html).

## See Also

[IStructureSystemFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemFolder.html)
[IStructureSystemFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemFolder_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
