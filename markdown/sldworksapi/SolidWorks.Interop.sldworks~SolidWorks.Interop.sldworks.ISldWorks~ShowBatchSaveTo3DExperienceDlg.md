---
title: "ShowBatchSaveTo3DExperienceDlg Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "ShowBatchSaveTo3DExperienceDlg"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowBatchSaveTo3DExperienceDlg.html"
---

# ShowBatchSaveTo3DExperienceDlg Method (ISldWorks)

Opens a dialog to save files in the specified folder to 3DEXPERIENCE.

## Syntax

### Visual Basic (Declaration)

```vb
Function ShowBatchSaveTo3DExperienceDlg( _
   ByVal FolderPath As System.String, _
   ByVal Options As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FolderPath As System.String
Dim Options As System.Integer
Dim value As System.Integer

value = instance.ShowBatchSaveTo3DExperienceDlg(FolderPath, Options)
```

### C#

```csharp
System.int ShowBatchSaveTo3DExperienceDlg(
   System.string FolderPath,
   System.int Options
)
```

### C++/CLI

```cpp
System.int ShowBatchSaveTo3DExperienceDlg(
   System.String^ FolderPath,
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FolderPath`: Path of files to save
- `Options`: not used

### Return Value

0 if successful, -1 if not

## VBA Syntax

See [SldWorks::ShowBatchSaveTo3DExperienceDlg](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~ShowBatchSaveTo3DExperienceDlg.html).

## Remarks

This method is valid only for [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm).

Call [ISldWorks::RunBatchSaveProcess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunBatchSaveProcess.html) after using this method.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2022 SP03, Revision Number 30.3
