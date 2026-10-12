---
title: "InsertDwgOrDxfFile Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertDwgOrDxfFile"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertDwgOrDxfFile.html"
---

# InsertDwgOrDxfFile Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::InsertDwgOrDxfFile2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertDwgOrDxfFile2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertDwgOrDxfFile( _
   ByVal FileName As System.String _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim FileName As System.String
Dim value As Feature

value = instance.InsertDwgOrDxfFile(FileName)
```

### C#

```csharp
Feature InsertDwgOrDxfFile(
   System.string FileName
)
```

### C++/CLI

```cpp
Feature^ InsertDwgOrDxfFile(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Name of the DXF or DWG image file

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::InsertDwgOrDxfFile](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertDwgOrDxfFile.html).

## Remarks

This method returns:

- Nothing or null if the file contains solid bodies data.
- is not supported for use in assembly documents.

You must also select a plane or planar surface before calling this method.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
