---
title: "SetDroppedFileName Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "SetDroppedFileName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetDroppedFileName.html"
---

# SetDroppedFileName Method (IAssemblyDoc)

Sets the new file name for a recently dropped file.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetDroppedFileName( _
   ByVal FileName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim FileName As System.String
Dim value As System.Boolean

value = instance.SetDroppedFileName(FileName)
```

### C#

```csharp
System.bool SetDroppedFileName(
   System.string FileName
)
```

### C++/CLI

```cpp
System.bool SetDroppedFileName(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Name of the file to use for the rest of the drop process

### Return Value

True if name is set, false if not

## VBA Syntax

See [AssemblyDoc::SetDroppedFileName](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~SetDroppedFileName.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::GetDroppedAtEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetDroppedAtEntity.html)
[IAssemblyDoc::SetDroppedFileConfigName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetDroppedFileConfigName.html)
[IAssemblyDoc::SetDroppedFileFeatureName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetDroppedFileFeatureName.html)
[DAssemblyDocEvents_FileDropPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FileDropPreNotifyEventHandler.html)
[IPartDoc::SetDroppedFileName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetDroppedFileName.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
