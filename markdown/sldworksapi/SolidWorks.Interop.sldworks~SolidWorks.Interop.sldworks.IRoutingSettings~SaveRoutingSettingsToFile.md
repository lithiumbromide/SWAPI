---
title: "SaveRoutingSettingsToFile Method (IRoutingSettings)"
project: "SOLIDWORKS API Help"
interface: "IRoutingSettings"
member: "SaveRoutingSettingsToFile"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~SaveRoutingSettingsToFile.html"
---

# SaveRoutingSettingsToFile Method (IRoutingSettings)

Saves routing settings to the specified file.

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveRoutingSettingsToFile( _
   ByVal RoutingSettingsFilename As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRoutingSettings
Dim RoutingSettingsFilename As System.String
Dim value As System.Boolean

value = instance.SaveRoutingSettingsToFile(RoutingSettingsFilename)
```

### C#

```csharp
System.bool SaveRoutingSettingsToFile(
   System.string RoutingSettingsFilename
)
```

### C++/CLI

```cpp
System.bool SaveRoutingSettingsToFile(
   System.String^ RoutingSettingsFilename
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RoutingSettingsFilename`: Full path name of file to which to save routing settings; file name must have an extension of **.sqy**

### Return Value

True if successful, false if not

## VBA Syntax

See [RoutingSettings::SaveRoutingSettingsToFile](ms-its:sldworksapivb6.chm::/sldworks~RoutingSettings~SaveRoutingSettingsToFile.html).

## Examples

See the [IRoutingSettings](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings.html) examples.

## See Also

[IRoutingSettings Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings.html)
[IRoutingSettings Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings_members.html)
[IRoutingSettings::LoadRoutingSettingsFromFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~LoadRoutingSettingsFromFile.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
