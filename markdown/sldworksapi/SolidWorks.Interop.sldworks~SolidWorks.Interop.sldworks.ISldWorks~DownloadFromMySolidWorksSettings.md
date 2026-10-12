---
title: "DownloadFromMySolidWorksSettings Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "DownloadFromMySolidWorksSettings"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DownloadFromMySolidWorksSettings.html"
---

# DownloadFromMySolidWorksSettings Method (ISldWorks)

Downloads the specified [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm) settings to SOLIDWORKS Design.

## Syntax

### Visual Basic (Declaration)

```vb
Function DownloadFromMySolidWorksSettings( _
   ByVal SystemOptions As System.Boolean, _
   ByVal FileLocations As System.Boolean, _
   ByVal Customizations As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim SystemOptions As System.Boolean
Dim FileLocations As System.Boolean
Dim Customizations As System.Boolean
Dim value As System.Integer

value = instance.DownloadFromMySolidWorksSettings(SystemOptions, FileLocations, Customizations)
```

### C#

```csharp
System.int DownloadFromMySolidWorksSettings(
   System.bool SystemOptions,
   System.bool FileLocations,
   System.bool Customizations
)
```

### C++/CLI

```cpp
System.int DownloadFromMySolidWorksSettings(
   System.bool SystemOptions,
   System.bool FileLocations,
   System.bool Customizations
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SystemOptions`: True to download, false to not
- `FileLocations`: True to download, false to not
- `Customizations`: True to download, false to not

### Return Value

Return code as defined by [swConnectedSyncSettingsErrors_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swConnectedSyncSettingsErrors_e.html)

## VBA Syntax

See [SldWorks::DownloadFromMySolidWorksSettings](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~DownloadFromMySolidWorksSettings.html).

## Remarks

In order to use this method, you must be logged into SOLIDWORKS Design connected to the 3DEXPERIENCE platform.

To turn on auto synchronization of settings, call:

- [ISldWorks::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.html)([swUserPreferenceToggle_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceToggle_e.html).swAutomaticSyncSettings, True)

and then call one, two, or all three of:

- ISldWorks::SetUserPreferenceToggle(swUserPreferenceToggle_e.swAutoSyncSettingsToInclude_SystemOptions, True)
- ISldWorks::SetUserPreferenceToggle(swUserPreferenceToggle_e.swAutoSyncSettingsToInclude_FileLocations, True)
- ISldWorks::SetUserPreferenceToggle(swUserPreferenceToggle_e.swAutoSyncSettingsToInclude_Customizations, True)

To get the timestamp of the last synchronization, call [ISldWorks::GetUserPreferenceStringValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceStringValue.html)([swUserPreferenceStringValue_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceStringValue_e.html).swLastSynchronizationTimeStamp).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::UploadToMySolidWorksSettings Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UploadToMySolidWorksSettings.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
