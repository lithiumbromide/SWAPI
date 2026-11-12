---
title: "DSldWorksEvents_End3DInterconnectTranslationNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_End3DInterconnectTranslationNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_End3DInterconnectTranslationNotifyEventHandler.html"
---

# DSldWorksEvents_End3DInterconnectTranslationNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Notifies the user program when the SOLIDWORKS application is finished importing or exporting a third-party native CAD file.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_End3DInterconnectTranslationNotifyEventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_End3DInterconnectTranslationNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_End3DInterconnectTranslationNotifyEventHandler(
   System.string FileName
)
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_End3DInterconnectTranslationNotifyEventHandler(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Name of imported or exported third-party native CAD file

## VBA Syntax

See [End3DInterconnectTranslationNotify Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~End3DInterconnectTranslationNotify_EV.html).

## Examples

See the [IImport3DInterconnectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.html) examples.

## Remarks

If developing a C++ application, use [swAppEnd3DInterconnectTranslationNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
