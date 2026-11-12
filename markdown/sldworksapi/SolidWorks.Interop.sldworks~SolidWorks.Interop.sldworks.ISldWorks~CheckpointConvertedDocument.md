---
title: "CheckpointConvertedDocument Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "CheckpointConvertedDocument"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CheckpointConvertedDocument.html"
---

# CheckpointConvertedDocument Method (ISldWorks)

Saves the specified open document if its version is older than the version of the SOLIDWORKS Design product being used.

## Syntax

### Visual Basic (Declaration)

```vb
Function CheckpointConvertedDocument( _
   ByVal DocName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim DocName As System.String
Dim value As System.Integer

value = instance.CheckpointConvertedDocument(DocName)
```

### C#

```csharp
System.int CheckpointConvertedDocument(
   System.string DocName
)
```

### C++/CLI

```cpp
System.int CheckpointConvertedDocument(
   System.String^ DocName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DocName`: Full pathname of the file to save

### Return Value

0 for no error or a bitwise OR of the errors encountered as defined in [swFileSaveError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileSaveError_e.html)

## VBA Syntax

See [SldWorks::CheckpointConvertedDocument](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~CheckpointConvertedDocument.html).

## Remarks

This saves the document even if the document is read-only.

This method requires that the document is currently open in your SOLIDWORKS Design session. It specifically checks if the document has been upgraded to the current version of the SOLIDWORKS Design product in this session. If it has not, then this method has no effect.

Be careful when using this method because this method attempts to change the file permissions to read-write if the file is read-only, and if successful , it overwrites the file and restores the permission to read-only. Although it may appear the file is safe because it is read-only before and after the operation, it might have been overwritten by this method.

This method was designed to be used with the ISldWorks event [DocumentConversionNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_DocumentConversionNotifyEventHandler.html). It does not require that the notification be used, but it should work in response to that notification.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 99 SP1, datecode 1999229
