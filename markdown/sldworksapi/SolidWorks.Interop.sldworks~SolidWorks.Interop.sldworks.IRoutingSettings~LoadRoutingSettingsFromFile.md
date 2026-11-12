---
title: "LoadRoutingSettingsFromFile Method (IRoutingSettings)"
project: "SOLIDWORKS API Help"
interface: "IRoutingSettings"
member: "LoadRoutingSettingsFromFile"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~LoadRoutingSettingsFromFile.html"
---

# LoadRoutingSettingsFromFile Method (IRoutingSettings)

Loads routing settings from the specified file.

## Syntax

### Visual Basic (Declaration)

```vb
Function LoadRoutingSettingsFromFile( _
   ByVal RoutingSettingsFilename As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRoutingSettings
Dim RoutingSettingsFilename As System.String
Dim value As System.Boolean

value = instance.LoadRoutingSettingsFromFile(RoutingSettingsFilename)
```

### C#

```csharp
System.bool LoadRoutingSettingsFromFile(
   System.string RoutingSettingsFilename
)
```

### C++/CLI

```cpp
System.bool LoadRoutingSettingsFromFile(
   System.String^ RoutingSettingsFilename
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RoutingSettingsFilename`: - Full path name of the **.sqy** file from which to load the routing settings

### Return Value

True if successful, false if not

## VBA Syntax

See [RoutingSettings::LoadRoutingSettingsFromFile](ms-its:sldworksapivb6.chm::/sldworks~RoutingSettings~LoadRoutingSettingsFromFile.html).

## See Also

[IRoutingSettings Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings.html)
[IRoutingSettings Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings_members.html)
[IRoutingSettings::LoadDefaultRoutingSettings Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~LoadDefaultRoutingSettings.html)
[IRoutingSettings::SaveRoutingSettingsToFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~SaveRoutingSettingsToFile.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
