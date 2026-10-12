---
title: "LoadAdminSettingsFile Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "LoadAdminSettingsFile"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadAdminSettingsFile.html"
---

# LoadAdminSettingsFile Method (ISldWorks)

Loads the specified ***.sldsettings** file into [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Function LoadAdminSettingsFile( _
   ByVal FilePath As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FilePath As System.String
Dim value As System.Integer

value = instance.LoadAdminSettingsFile(FilePath)
```

### C#

```csharp
System.int LoadAdminSettingsFile(
   System.string FilePath
)
```

### C++/CLI

```cpp
System.int LoadAdminSettingsFile(
   System.String^ FilePath
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FilePath`: Full local path name of the ***.sldsettings** file to load

### Return Value

True if settings successfully applied, false if not

## VBA Syntax

See [SldWorks::LoadAdminSettingsFile](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~LoadAdminSettingsFile.html).

## Remarks

The 3DEXPERIENCE platform Admin authors the ***.sldsettings** platform file with settings appropriate for SOLIDWORKS Design connected to the 3DEXPERIENCE platform. At launch, SOLIDWORKS Design connected to the 3DEXPERIENCE platform reads a local copy. This method is used primarily by the 3DEXPERIENCE Add-in.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::RestoreSettings Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RestoreSettings.html)
[ISldWorks::SaveSettings Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SaveSettings.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
