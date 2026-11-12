---
title: "SetPromptFilename Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "SetPromptFilename"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetPromptFilename.html"
---

# SetPromptFilename Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::SetPromptFilename2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetPromptFilename2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetPromptFilename( _
   ByVal FileName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FileName As System.String

instance.SetPromptFilename(FileName)
```

### C#

```csharp
void SetPromptFilename(
   System.string FileName
)
```

### C++/CLI

```cpp
void SetPromptFilename(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Filename

## VBA Syntax

See [SldWorks::SetPromptFilename](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~SetPromptFilename.html).

## Remarks

The filename specified is only used if the SOLIDWORKS events [PromptForFileNameNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_PromptForFilenameNotifyEventHandler.html) or [ReferencedFilePreNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_ReferencedFilePreNotifyEventHandler.html) returns S_FALSE. This implies that you cannot specify an initial filename for SOLIDWORKS to use in the standard dialog. Instead, you must provide your own file dialog and return the filename after the user selects it.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::LoadFile4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadFile4.html)
[ISldWorks::OpenDoc6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.html)
[ISldWorks::SetMultipleFilenamesPrompt Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetMultipleFilenamesPrompt.html)
[ISldWorks::SetNewFilename Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetNewFilename.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
