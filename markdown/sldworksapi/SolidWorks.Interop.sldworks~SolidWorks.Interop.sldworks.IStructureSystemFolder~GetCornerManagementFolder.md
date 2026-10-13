---
title: "GetCornerManagementFolder Method (IStructureSystemFolder)"
project: "SOLIDWORKS API Help"
interface: "IStructureSystemFolder"
member: "GetCornerManagementFolder"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemFolder~GetCornerManagementFolder.html"
---

# GetCornerManagementFolder Method (IStructureSystemFolder)

Gets the corner management folder in this structure system folder.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCornerManagementFolder() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IStructureSystemFolder
Dim value As System.Object

value = instance.GetCornerManagementFolder()
```

### C#

```csharp
System.object GetCornerManagementFolder()
```

### C++/CLI

```cpp
System.Object^ GetCornerManagementFolder();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)

## VBA Syntax

See [StructureSystemFolder::GetCornerManagementFolder](ms-its:sldworksapivb6.chm::/sldworks~StructureSystemFolder~GetCornerManagementFolder.html).

## Remarks

After calling this method to get the IFeature, use [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.html) to get an [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html).

## See Also

[IStructureSystemFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemFolder.html)
[IStructureSystemFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemFolder_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
