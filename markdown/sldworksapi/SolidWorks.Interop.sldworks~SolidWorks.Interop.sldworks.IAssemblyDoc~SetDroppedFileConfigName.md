---
title: "SetDroppedFileConfigName Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "SetDroppedFileConfigName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetDroppedFileConfigName.html"
---

# SetDroppedFileConfigName Method (IAssemblyDoc)

Sets the configuration name for the recently dropped file.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetDroppedFileConfigName( _
   ByVal ConfigName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim ConfigName As System.String
Dim value As System.Boolean

value = instance.SetDroppedFileConfigName(ConfigName)
```

### C#

```csharp
System.bool SetDroppedFileConfigName(
   System.string ConfigName
)
```

### C++/CLI

```cpp
System.bool SetDroppedFileConfigName(
   System.String^ ConfigName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConfigName`: Name of the configuration to set

### Return Value

True if the name is successfully set, false if not

## VBA Syntax

See [AssemblyDoc::SetDroppedFileConfigName](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~SetDroppedFileConfigName.html).

## Remarks

If the configuration name is set in response to the [FileDropNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DAssemblyDocEvents_FileDropNotifyEventHandler.html) event, SOLIDWORKS does not display the dialog for the selected configuration names when a file is dropped in an assembly.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::SetDroppedFileName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetDroppedFileName.html)
[IAssemblyDoc::GetDroppedAtEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetDroppedAtEntity.html)

## Availability

SOLIDWORKS 99 SP03, datecode 1999271
