---
title: "DSldWorksEvents_DocumentConversionNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_DocumentConversionNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_DocumentConversionNotifyEventHandler.html"
---

# DSldWorksEvents_DocumentConversionNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program that a file has been converted from an older version of SOLIDWORKS during the open operation.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_DocumentConversionNotifyEventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_DocumentConversionNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_DocumentConversionNotifyEventHandler(
   System.string FileName
)
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_DocumentConversionNotifyEventHandler(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Name of the converted file

## VBA Syntax

See [DocumentConversionNotify Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~DocumentConversionNotify_EV.html).

## Remarks

Any number of these notifications may be sent at the end of an open operation because an open operation of an assembly or drawing may cause multiple files to open. In this scenario, all of the opened files may have been converted.

If developing a C++ application, use [swAppDocumentConversionNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.
