---
title: "AddSpeedPak2 Method (IConfigurationManager)"
project: "SOLIDWORKS API Help"
interface: "IConfigurationManager"
member: "AddSpeedPak2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddSpeedPak2.html"
---

# AddSpeedPak2 Method (IConfigurationManager)

Creates a SpeedPak configuration that includes all faces and the specified threshold of parts or bodies for the active assembly configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddSpeedPak2( _
   ByVal Type As System.Integer, _
   ByVal PartThreshold As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IConfigurationManager
Dim Type As System.Integer
Dim PartThreshold As System.Double
Dim value As System.Object

value = instance.AddSpeedPak2(Type, PartThreshold)
```

### C#

```csharp
System.object AddSpeedPak2(
   System.int Type,
   System.double PartThreshold
)
```

### C++/CLI

```cpp
System.Object^ AddSpeedPak2(
   System.int Type,
   System.double PartThreshold
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`: Selection type:

  - 1 = Geometry
  - 2 = Graphics
- `PartThreshold`: 1.0 >= Double value for part or body selection threshold >= 0.0; 1.0 selects nothing, and 0.0 selects all (see **Remarks**)

### Return Value

SpeedPak [configuration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration.html)

## VBA Syntax

See [ConfigurationManager::AddSpeedPak2](ms-its:sldworksapivb6.chm::/sldworks~ConfigurationManager~AddSpeedPak2.html).

## Examples

[Create a SpeedPak Configuration (VBA)](Create_SpeedPak_Example_VB.htm)
[Create a Speedpak Configuration (VB.NET)](Create_SpeedPak_Example_VBNET.htm)
[Create a Speedpak Configuration (C#)](Create_Speedpak_Example_CSharp.htm)

## Remarks

PartThreshold corresponds to the value of the **Bodies to Include** slider on the SpeedPak PropertyManager page.

This method includes all faces in the SpeedPak configuration.

## See Also

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.html)
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.html)
[IConfiguration::IsSpeedPak Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IsSpeedPak.html)
[IConfiguration::UpdateSpeedPak Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~UpdateSpeedPak.html)
[IAssemblyDoc::CreateSpeedPak Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateSpeedPak.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
