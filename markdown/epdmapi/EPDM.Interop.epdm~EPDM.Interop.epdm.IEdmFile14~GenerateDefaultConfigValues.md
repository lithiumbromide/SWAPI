---
title: "GenerateDefaultConfigValues Method (IEdmFile14)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile14"
member: "GenerateDefaultConfigValues"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile14~GenerateDefaultConfigValues.html"
---

# GenerateDefaultConfigValues Method (IEdmFile14)

Generates default configuration data for the specified drawing or file that lacks properties at the configuration level.

## Syntax

### Visual Basic

```vb
Sub GenerateDefaultConfigValues( _
   ByVal lOldFileID As System.Integer, _
   ByVal bsOldConfigName As System.String, _
   ByVal bsNewConfigName As System.String, _
   ByVal bsActiveConfig As System.String, _
   ByVal bOnlyForUpdateAllFlag As System.Boolean _
)
```

### C#

```csharp
void GenerateDefaultConfigValues(
   System.int lOldFileID,
   System.string bsOldConfigName,
   System.string bsNewConfigName,
   System.string bsActiveConfig,
   System.bool bOnlyForUpdateAllFlag
)
```

### C++/CLI

```cpp
void GenerateDefaultConfigValues(
   System.int lOldFileID,
   System.String^ bsOldConfigName,
   System.String^ bsNewConfigName,
   System.String^ bsActiveConfig,
   System.bool bOnlyForUpdateAllFlag
)
```

### Parameters

- `lOldFileID`: ID of drawing or file that lacks properties at the configuration level
- `bsOldConfigName`: Name of configuration whose values to copy (see **Remarks**)
- `bsNewConfigName`: Name of the configuration to which to copy values (see **Remarks**)
- `bsActiveConfig`: Name of the active configuration (see **Remarks**)
- `bOnlyForUpdateAllFlag`: True to copy values only for controls for which [IEdmCardControl6::UpdatesAllConfigurations](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl6~UpdatesAllConfigurations.html) is set to true, false to copy values for all variables associated with this file

## Examples

[Generate Configuration Values (C#)](Generate_Config_Values_Example_CSharp.htm)
[Generate Configuration Values (VB.NET)](Generate_Config_Values_Example_VBNET.htm)

## Remarks

This method:

- is valid only for files with data card variables.
- copies values from bsOldConfigName to bsNewConfigName. If it encounters a null control variable in bsOldConfigName, it takes the value from bsActiveConfig instead.

Use [IEdmFile5::GetConfigurations](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetConfigurations.html) to populate the configuration parameters.

## See Also

[IEdmFile14 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile14.html)
[IEdmFile14 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile14_members.html)
[IEdmFile8::GenerateDefaultValuesForNewConfiguration Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile8~GenerateDefaultValuesForNewConfiguration.html)

## Availability

SOLIDWORKS PDM Professional 2018 SP03
