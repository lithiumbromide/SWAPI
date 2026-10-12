---
title: "DSldWorksEvents_EndTranslationNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_EndTranslationNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_EndTranslationNotifyEventHandler.html"
---

# DSldWorksEvents_EndTranslationNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Notifies the user program when the SOLIDWORKS application is finished importing a file.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_EndTranslationNotifyEventHandler( _
   ByVal FileName As System.String, _
   ByVal Options As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_EndTranslationNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_EndTranslationNotifyEventHandler(
   System.string FileName,
   System.int Options
)
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_EndTranslationNotifyEventHandler(
   System.String^ FileName,
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Name of imported file
- `Options`: Option as defined in [swTranslationNotifyOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTranslationNotifyOptions_e.html)

## VBA Syntax

See [EndTranslationNotify Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~EndTranslationNotify_EV.html).

## Remarks

This event occurs after automatic healing if it is enabled. To enable automatic healing, set swImportAutoRunImportDiagnosticsPersist and swImportAutoRunImportDiagnostics to True. See [swUserPreferenceToggle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceToggle_e.html), Import for details about these two enumerators.

If developing a C++ application, use [swAppEndTranslationNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP3, Revision Number 10.3
