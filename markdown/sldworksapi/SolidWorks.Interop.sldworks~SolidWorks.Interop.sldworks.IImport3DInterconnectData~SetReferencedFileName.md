---
title: "SetReferencedFileName Method (IImport3DInterconnectData)"
project: "SOLIDWORKS API Help"
interface: "IImport3DInterconnectData"
member: "SetReferencedFileName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData~SetReferencedFileName.html"
---

# SetReferencedFileName Method (IImport3DInterconnectData)

Sets the full path name of the proprietary, non-native CAD file.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetReferencedFileName( _
   ByVal FileName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IImport3DInterconnectData
Dim FileName As System.String

instance.SetReferencedFileName(FileName)
```

### C#

```csharp
void SetReferencedFileName(
   System.string FileName
)
```

### C++/CLI

```cpp
void SetReferencedFileName(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Full path name of the linked non-native CAD file

## VBA Syntax

See [Import3DInterconnectData::SetReferencedFileName](ms-its:sldworksapivb6.chm::/sldworks~Import3DInterconnectData~SetReferencedFileName.html).

## See Also

[IImport3DInterconnectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.html)
[IImport3DInterconnectData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData_members.html)
[IImport3DinterconnectData::GetReferencedFileName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData~GetReferencedFileName.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
