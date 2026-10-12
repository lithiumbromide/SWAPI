---
title: "RenameStudyFromName Method (ICWStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudyManager"
member: "RenameStudyFromName"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~RenameStudyFromName.html"
---

# RenameStudyFromName Method (ICWStudyManager)

Renames the study that has the specified name.

## Syntax

### Visual Basic (Declaration)

```vb
Function RenameStudyFromName( _
   ByVal SOldName As System.String, _
   ByVal SNewName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudyManager
Dim SOldName As System.String
Dim SNewName As System.String
Dim value As System.Integer

value = instance.RenameStudyFromName(SOldName, SNewName)
```

### C#

```csharp
System.int RenameStudyFromName(
   System.string SOldName,
   System.string SNewName
)
```

### C++/CLI

```cpp
System.int RenameStudyFromName(
   System.String^ SOldName,
   System.String^ SNewName
)
```

### Parameters

- `SOldName`: Old name of study
- `SNewName`: New name of study

### Return Value

Error as defined by [swsStudyError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsStudyError_e.html)

## VBA Syntax

See [CWStudyManager::RenameStudyFromName](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudyManager~RenameStudyFromName.html).

## Examples

[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VBA)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VB.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VB.NET)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VBNET.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (C#)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_CSharp.htm)

## See Also

[ICWStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager.html)
[ICWStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager_members.html)
[ICWStudyManager::RenameStudyFromID Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~RenameStudyFromID.html)

## Availability

SOLIDWORKS Simulation API 2014 SP0
