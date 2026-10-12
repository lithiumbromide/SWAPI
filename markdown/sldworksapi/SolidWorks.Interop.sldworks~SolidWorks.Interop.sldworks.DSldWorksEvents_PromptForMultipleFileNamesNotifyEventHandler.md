---
title: "DSldWorksEvents_PromptForMultipleFileNamesNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_PromptForMultipleFileNamesNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_PromptForMultipleFileNamesNotifyEventHandler.html"
---

# DSldWorksEvents_PromptForMultipleFileNamesNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when any dependent documents are missing from the file being opened.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_PromptForMultipleFileNamesNotifyEventHandler( _
   ByVal openOrSave As System.Integer, _
   ByRef suggestedFileNames As System.Object, _
   ByRef DocTypes As System.Object, _
   ByVal cause As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_PromptForMultipleFileNamesNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_PromptForMultipleFileNamesNotifyEventHandler(
   System.int openOrSave,
   ref System.object suggestedFileNames,
   ref System.object DocTypes,
   System.int cause
)
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_PromptForMultipleFileNamesNotifyEventHandler(
   System.int openOrSave,
   System.Object^% suggestedFileNames,
   System.Object^% DocTypes,
   System.int cause
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `openOrSave`: - 0 = save
  - 1 = open
- `suggestedFileNames`: Array of names of the missing SOLIDWORKS documents
- `DocTypes`: Types of the missing documents as defined in [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)
- `cause`: Cause as defined in [swPrompForFilenameCause_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPrompForFilenameCause_e.html)

## VBA Syntax

See [PromptForMultipleFileNamesNotify Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~PromptForMultipleFileNamesNotify_EV.html).

## Remarks

Use this event with the [ISldWorks::SetMultipleFilenamesPrompt](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetMultipleFilenamesPrompt.html) method.

If developing a C++ application, use [swAppPromptForMultipleFileNameNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2008 SP1, Revision Number 16.1
