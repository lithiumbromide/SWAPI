---
title: "GenerateDefaultValuesForNewConfiguration Method (IEdmFile8)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile8"
member: "GenerateDefaultValuesForNewConfiguration"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile8~GenerateDefaultValuesForNewConfiguration.html"
---

# GenerateDefaultValuesForNewConfiguration Method (IEdmFile8)

Populates the file data card with default data when a new configuration is added in SOLIDWORKS.

## Syntax

### Visual Basic

```vb
Sub GenerateDefaultValuesForNewConfiguration( _
   ByVal bsConfiguration As System.String, _
   ByVal llCfgPersistID As System.Long, _
   ByVal poAux As System.Object, _
   ByRef ppoRetVariables() As System.Object _
)
```

### C#

```csharp
void GenerateDefaultValuesForNewConfiguration(
   System.string bsConfiguration,
   System.long llCfgPersistID,
   System.object poAux,
   out System.object[] ppoRetVariables
)
```

### C++/CLI

```cpp
void GenerateDefaultValuesForNewConfiguration(
   System.String^ bsConfiguration,
   System.int64 llCfgPersistID,
   System.Object^ poAux,
   [Out] System.array<Object^>^ ppoRetVariables
)
```

### Parameters

- `bsConfiguration`: Name of the new configuration
- `llCfgPersistID`: SOLIDWORKS configuration ID; 0 if ID is not available (see **Remarks**)
- `poAux`: Null; for internal use only
- `ppoRetVariables`: Array of [IEdmVariableValue5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableValue5.html)s for the file data card

## Remarks

This method is called by the SOLIDWORKS add-in when a new configuration is added to a file. Its purpose is to populate the file data card with default data for the new configuration.

llCfgPersistID is a unique SOLIDWORKS API configuration ID.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: An argument is invalid.

## See Also

[IEdmFile8 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile8.html)
[IEdmFile8 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile8_members.html)
[IEdmFile14::GenerateDefaultConfigValues Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile14~GenerateDefaultConfigValues.html)

## Availability

SOLIDWORKS PDM Professional 2010
