---
title: "SetPromptFilename2 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "SetPromptFilename2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetPromptFilename2.html"
---

# SetPromptFilename2 Method (ISldWorks)

Sets the file to open in response to a SOLIDWORKS event.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetPromptFilename2( _
   ByVal FileName As System.String, _
   ByVal ConfigName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FileName As System.String
Dim ConfigName As System.String

instance.SetPromptFilename2(FileName, ConfigName)
```

### C#

```csharp
void SetPromptFilename2(
   System.string FileName,
   System.string ConfigName
)
```

### C++/CLI

```cpp
void SetPromptFilename2(
   System.String^ FileName,
   System.String^ ConfigName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Full pathname of file to open
- `ConfigName`: Configuration name of file to open

## VBA Syntax

See [SldWorks::SetPromptFilename2](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~SetPromptFilename2.html).

## Examples

Contact SOLIDWORKS API Support to obtain **Close and Reopen a Drawing Document (VBA, VB.NET, C#)**.

## Remarks

FileName is used only:

| When the handler of this event... | Returns... |
| --- | --- |
| FileCloseNotify | non- 0 value |
| PromptForFileNameNotify | non- 0 value |
| ReferencedFilePreNotify | non- 0 value |

Because the filename specified is used only when [PromptForFileNameNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_PromptForFilenameNotifyEventHandler.html) and [ReferencedFilePreNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_ReferencedFilePreNotifyEventHandler.html) return S_FALSE, you cannot specify an initial filename for SOLIDWORKS to use in the standard dialog. Instead, you must provide your own file dialog and return the filename after the user selects it.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::LoadFile4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadFile4.html)
[ISldWorks::OpenDoc7 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc7.html)
[ISldWorks::SetMultipleFilenamesPrompt Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetMultipleFilenamesPrompt.html)
[ISldWorks::SetNewFilename Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetNewFilename.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
