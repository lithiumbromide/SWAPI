---
title: "GetReferencedFileName Method (IImport3DInterconnectData)"
project: "SOLIDWORKS API Help"
interface: "IImport3DInterconnectData"
member: "GetReferencedFileName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData~GetReferencedFileName.html"
---

# GetReferencedFileName Method (IImport3DInterconnectData)

Gets the full path name of the proprietary, non-native CAD file.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetReferencedFileName() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IImport3DInterconnectData
Dim value As System.String

value = instance.GetReferencedFileName()
```

### C#

```csharp
System.string GetReferencedFileName()
```

### C++/CLI

```cpp
System.String^ GetReferencedFileName();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Full path name of the linked non-native CAD file

## VBA Syntax

See [Import3DInterconnectData::GetReferencedFileName](ms-its:sldworksapivb6.chm::/sldworks~Import3DInterconnectData~GetReferencedFileName.html).

## Examples

See the [IImport3DInterconnectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.html) examples.

## See Also

[IImport3DInterconnectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.html)
[IImport3DInterconnectData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData_members.html)
[IImport3DinterconnectData::SetReferencedFileName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData~SetReferencedFileName.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
