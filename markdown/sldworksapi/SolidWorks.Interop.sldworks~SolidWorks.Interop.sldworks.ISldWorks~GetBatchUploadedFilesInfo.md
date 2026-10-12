---
title: "GetBatchUploadedFilesInfo Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetBatchUploadedFilesInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetBatchUploadedFilesInfo.html"
---

# GetBatchUploadedFilesInfo Method (ISldWorks)

Gets the files uploaded to 3DEXPERIENCE during a batch process.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBatchUploadedFilesInfo( _
   ByRef ProcessedFileNames As System.Object, _
   ByRef NonProcessedFileNames As System.Object, _
   ByRef FailedFileNames As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim ProcessedFileNames As System.Object
Dim NonProcessedFileNames As System.Object
Dim FailedFileNames As System.Object
Dim value As System.Boolean

value = instance.GetBatchUploadedFilesInfo(ProcessedFileNames, NonProcessedFileNames, FailedFileNames)
```

### C#

```csharp
System.bool GetBatchUploadedFilesInfo(
   out System.object ProcessedFileNames,
   out System.object NonProcessedFileNames,
   out System.object FailedFileNames
)
```

### C++/CLI

```cpp
System.bool GetBatchUploadedFilesInfo(
   [Out] System.Object^ ProcessedFileNames,
   [Out] System.Object^ NonProcessedFileNames,
   [Out] System.Object^ FailedFileNames
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ProcessedFileNames`: Array of processed file names
- `NonProcessedFileNames`: Array of unprocessed file names
- `FailedFileNames`: Array of file names that failed to upload

### Return Value

True if retrieval successful, false if not

## VBA Syntax

See [SldWorks::GetBatchUploadedFilesInfo](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetBatchUploadedFilesInfo.html).

## Remarks

This method is valid only for [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm).

Before using this method, call [ISldWorks::RunBatchSaveProcess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunBatchSaveProcess.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2022 SP03, Revision Number 30.3
