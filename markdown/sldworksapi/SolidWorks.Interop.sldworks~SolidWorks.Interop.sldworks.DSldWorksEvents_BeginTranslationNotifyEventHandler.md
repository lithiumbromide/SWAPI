---
title: "DSldWorksEvents_BeginTranslationNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_BeginTranslationNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_BeginTranslationNotifyEventHandler.html"
---

# DSldWorksEvents_BeginTranslationNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Notifies the user program when the SOLIDWORKS application starts to import a file.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_BeginTranslationNotifyEventHandler( _
   ByVal FileName As System.String, _
   ByVal Options As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_BeginTranslationNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_BeginTranslationNotifyEventHandler(
   System.string FileName,
   System.int Options
)
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_BeginTranslationNotifyEventHandler(
   System.String^ FileName,
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Name of imported file
- `Options`: Option as defined in [swTranslationNotifyOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTranslationNotifyOptions_e.html)

## VBA Syntax

See [BeginTranslationNotify Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~BeginTranslationNotify_EV.html).

## Remarks

If developing a C++ application, use [swAppBeginTranslationNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP3, Revision Number 10.3
