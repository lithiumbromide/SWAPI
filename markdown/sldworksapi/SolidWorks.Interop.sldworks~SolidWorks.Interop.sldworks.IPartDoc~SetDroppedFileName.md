---
title: "SetDroppedFileName Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "SetDroppedFileName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetDroppedFileName.html"
---

# SetDroppedFileName Method (IPartDoc)

Sets the filename for a recently dropped file.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetDroppedFileName( _
   ByVal FileName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
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

See [PartDoc::SetDroppedFileName](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~SetDroppedFileName.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IAssemblyDoc::SetDroppedFileName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetDroppedFileName.html)
[DPartDocEvents_FileDropPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FileDropPreNotifyEventHandler.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
