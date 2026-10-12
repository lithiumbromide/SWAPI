---
title: "DSldWorksEvents_PromptForFilenameNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_PromptForFilenameNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_PromptForFilenameNotifyEventHandler.html"
---

# DSldWorksEvents_PromptForFilenameNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when a dependent document is missing from the file being opened.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_PromptForFilenameNotifyEventHandler( _
   ByVal openOrSave As System.Integer, _
   ByVal suggestedFileName As System.String, _
   ByVal DocType As System.Integer, _
   ByVal cause As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_PromptForFilenameNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_PromptForFilenameNotifyEventHandler(
   System.int openOrSave,
   System.string suggestedFileName,
   System.int DocType,
   System.int cause
)
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_PromptForFilenameNotifyEventHandler(
   System.int openOrSave,
   System.String^ suggestedFileName,
   System.int DocType,
   System.int cause
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `openOrSave`: - 0 = save
  - 1 = open
- `suggestedFileName`: Name of the missing SOLIDWORKS document
- `DocType`: Type of the missing document as defined in [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)
- `cause`: Cause as defined in [swPrompForFilenameCause_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPrompForFilenameCause_e.html)

## VBA Syntax

See [PromptForFilenameNotify Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~PromptForFilenameNotify_EV.html).

## Remarks

Use this event with the [ISldWorks::SetPromptFilename2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetPromptFilename2.html) method, not with the [ISldWorks::SetMissingReferencePathName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetMissingReferencePathName.html) method.

An example of a good use for this event is when you are mirroring an assembly. If you want to create new files for the mirrored components, use this notification to specify the new filename. This is useful when you want to choose filenames for the newly created components during the mirroring process.

If developing a C++ application, use [swAppPromptForFileNameNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
