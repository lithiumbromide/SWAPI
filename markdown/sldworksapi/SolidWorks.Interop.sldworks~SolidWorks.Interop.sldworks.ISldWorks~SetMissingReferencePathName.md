---
title: "SetMissingReferencePathName Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "SetMissingReferencePathName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetMissingReferencePathName.html"
---

# SetMissingReferencePathName Method (ISldWorks)

Sets the missing reference file name. Use with the SOLIDWORKS event [ReferenceNotFoundNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_ReferenceNotFoundNotifyEventHandler.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetMissingReferencePathName( _
   ByVal FileName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FileName As System.String

instance.SetMissingReferencePathName(FileName)
```

### C#

```csharp
void SetMissingReferencePathName(
   System.string FileName
)
```

### C++/CLI

```cpp
void SetMissingReferencePathName(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Path and filename of the missing reference

## VBA Syntax

See [SldWorks::SetMissingReferencePathName](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~SetMissingReferencePathName.html).

## Remarks

Use with the SOLIDWORKS event [ReferenceNotFoundNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_ReferenceNotFoundNotifyEventHandler.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
