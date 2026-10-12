---
title: "RunBatchSaveProcess Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "RunBatchSaveProcess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunBatchSaveProcess.html"
---

# RunBatchSaveProcess Method (ISldWorks)

Batch saves files to 3DEXPERIENCE.

## Syntax

### Visual Basic (Declaration)

```vb
Function RunBatchSaveProcess() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.Boolean

value = instance.RunBatchSaveProcess()
```

### C#

```csharp
System.bool RunBatchSaveProcess()
```

### C++/CLI

```cpp
System.bool RunBatchSaveProcess();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if batch save successful, false if not

## VBA Syntax

See [SldWorks::RunBatchSaveProcess](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~RunBatchSaveProcess.html).

## Remarks

This method is valid only for [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm).

Call this method:

- after loading the files to save using [ISldWorks::ShowBatchSaveTo3DExperienceDlg](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowBatchSaveTo3DExperienceDlg.html).
- before calling [ISldWorks::GetBatchUploadedFilesInfo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetBatchUploadedFilesInfo.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2022 SP03, Revision Number 30.3
