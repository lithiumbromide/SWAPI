---
title: "GetStructureSystemFolder Method (ICornerManagementFolder)"
project: "SOLIDWORKS API Help"
interface: "ICornerManagementFolder"
member: "GetStructureSystemFolder"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder~GetStructureSystemFolder.html"
---

# GetStructureSystemFolder Method (ICornerManagementFolder)

Gets the structure system folder containing this corner management folder.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetStructureSystemFolder() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICornerManagementFolder
Dim value As System.Object

value = instance.GetStructureSystemFolder()
```

### C#

```csharp
System.object GetStructureSystemFolder()
```

### C++/CLI

```cpp
System.Object^ GetStructureSystemFolder();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemFolder.html[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)

## VBA Syntax

See [CornerManagementFolder::GetStructureSystemFolder](ms-its:sldworksapivb6.chm::/sldworks~CornerManagementFolder~GetStructureSystemFolder.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

## Remarks

After calling this method to get the IFeature, use [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.html) to get an [IStructureSystemFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemFolder.html).

## See Also

[ICornerManagementFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html)
[ICornerManagementFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
