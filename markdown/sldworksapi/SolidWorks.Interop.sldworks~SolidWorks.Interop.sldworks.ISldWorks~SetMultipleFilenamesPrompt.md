---
title: "SetMultipleFilenamesPrompt Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "SetMultipleFilenamesPrompt"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetMultipleFilenamesPrompt.html"
---

# SetMultipleFilenamesPrompt Method (ISldWorks)

Sets the new filenames to open in response to the ISldWorks [PromptForMultipleFileNamesNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_PromptForMultipleFileNamesNotifyEventHandler.html) event.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetMultipleFilenamesPrompt( _
   ByVal FileName As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FileName As System.Object

instance.SetMultipleFilenamesPrompt(FileName)
```

### C#

```csharp
void SetMultipleFilenamesPrompt(
   System.object FileName
)
```

### C++/CLI

```cpp
void SetMultipleFilenamesPrompt(
   System.Object^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Array of filenames

## VBA Syntax

See [SldWorks::SetMultipleFilenamesPrompt](ms-its:sldworksapivb6.chm::/Sldworks~Sldworks~SetMultipleFilenamesPrompt.html).

## Remarks

The filenames specified are only used if the SOLIDWORKS [PromptForMultipleFileNamesNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_PromptForMultipleFileNamesNotifyEventHandler.html) event returns S_FALSE. This implies that you cannot specify initial filenames for SOLIDWORKS to use in the standard dialog. Instead, you must provide your own file dialog and return the filenames after the user selects them.

Guidelines for using this method when the cause argument of the SOLIDWORKS PromptForMultipleFileNamesNotify event is set to [swSaveVirtualComponentExternally](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPrompForFilenameCause_e.html):

- Length of the Filename argument array must be equal to the length of the suggestedFileNames argument array passed into ISldWorks::SetMultipleFilenamesPrompt. If there is a mismatch, all virtual components will be saved internal to the assembly with the suggested file name passed by the SOLIDWORKS PromptForMultipleFileNamesNotify event .
- Supplying a full path and file name will save a virtual component external to the assembly using that path and file name.
- Supplying only a file name (i.e., no path) will save the virtual component internal to the assembly with the suggested file name passed by the SOLIDWORKS PromptForMultipleFileNamesNotify event .
- This method cannot be used to change the name of an internally saved virtual component.
- Supplying an empty string will save the virtual component external to the assembly and in the same folder as the assembly with the suggested file name passed by the SOLIDWORKS PromptForMultipleFileNamesNotify event.
- Supplying an invalid path and file name or insufficient access rights will save the virtual component internal to the assembly with the suggested file name passed by the SOLIDWORKS PromptForMultipleFileNamesNotify event.
- Insufficient access rights to the path and file name will save the virtual component internal to the assembly with the suggested file name passed by the SOLIDWORKS PromptForMultipleFileNamesNotify event.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::SetNewFilename Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetNewFilename.html)
[ISldWorks::SetPromptFilename Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetPromptFilename.html)

## Availability

SOLIDWORKS 2008 SP1, Revision Number 16.0
