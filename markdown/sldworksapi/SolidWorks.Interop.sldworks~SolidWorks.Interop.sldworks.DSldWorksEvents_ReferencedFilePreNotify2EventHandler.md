---
title: "DSldWorksEvents_ReferencedFilePreNotify2EventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_ReferencedFilePreNotify2EventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_ReferencedFilePreNotify2EventHandler.html"
---

# DSldWorksEvents_ReferencedFilePreNotify2EventHandler Delegate (SolidWorks.Interop.sldworks)

Notifies the user program before SOLIDWORKS opens the specified file with the specified status.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_ReferencedFilePreNotify2EventHandler( _
   ByVal FileName As System.String, _
   ByVal FileStatus As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_ReferencedFilePreNotify2EventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_ReferencedFilePreNotify2EventHandler(
   System.string FileName,
   System.int FileStatus
)
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_ReferencedFilePreNotify2EventHandler(
   System.String^ FileName,
   System.int FileStatus
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Path and filename of file to open
- `FileStatus`: Open status as defined in [swReferencedFileStatus_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swReferencedFileStatus_e.html)

## VBA Syntax

See [ReferencedFilePreNotify2 Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~ReferencedFilePreNotify2_EV.html).

## Remarks

If developing a C++ application, use [swAppReferencedFilePreNotify2](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
