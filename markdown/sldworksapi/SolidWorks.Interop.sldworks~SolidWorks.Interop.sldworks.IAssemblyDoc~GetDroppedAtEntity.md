---
title: "GetDroppedAtEntity Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "GetDroppedAtEntity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetDroppedAtEntity.html"
---

# GetDroppedAtEntity Method (IAssemblyDoc)

Gets a pointer to the entity where a file is dropped into this assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDroppedAtEntity() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As System.Object

value = instance.GetDroppedAtEntity()
```

### C#

```csharp
System.object GetDroppedAtEntity()
```

### C++/CLI

```cpp
System.Object^ GetDroppedAtEntity();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Object for the entity

## VBA Syntax

See [AssemblyDoc::GetDroppedAtEntity](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~GetDroppedAtEntity.html).

## Remarks

Use this method in the handler for the [FileDropNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DAssemblyDocEvents_FileDropNotifyEventHandler.html) event.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::SetDroppedFileConfigName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetDroppedFileConfigName.html)
[SetDroppedFileName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetDroppedFileName.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
