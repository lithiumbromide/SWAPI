---
title: "AddSpeedPak Method (IConfigurationManager)"
project: "SOLIDWORKS API Help"
interface: "IConfigurationManager"
member: "AddSpeedPak"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddSpeedPak.html"
---

# AddSpeedPak Method (IConfigurationManager)

Obsolete. Superseded by [IConfigurationManager::AddSpeedPak2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfigurationManager~AddSpeedPak2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddSpeedPak( _
   ByVal Type As System.Integer, _
   ByVal PartThreshold As System.Double, _
   ByVal FaceThreshold As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IConfigurationManager
Dim Type As System.Integer
Dim PartThreshold As System.Double
Dim FaceThreshold As System.Double
Dim value As System.Object

value = instance.AddSpeedPak(Type, PartThreshold, FaceThreshold)
```

### C#

```csharp
System.object AddSpeedPak(
   System.int Type,
   System.double PartThreshold,
   System.double FaceThreshold
)
```

### C++/CLI

```cpp
System.Object^ AddSpeedPak(
   System.int Type,
   System.double PartThreshold,
   System.double FaceThreshold
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`: - 1 = Geometry
  - 2 = Graphics
- `PartThreshold`:
- `FaceThreshold`: See **Remarks**

### Return Value

SpeedPak [configuration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration.html)

## VBA Syntax

See [ConfigurationManager::AddSpeedPak](ms-its:sldworksapivb6.chm::/sldworks~ConfigurationManager~AddSpeedPak.html).

## Remarks

The SOLIDWORKS Design user-interface control corresponding to the FaceThreshhold parameter was removed from SOLIDWORKS 2013 and later. Regardless of the value that you specify for the FaceThreshhold parameter, the value 0 is passed, which results in no faces being included for SpeedPak by a call to this method.

This method was revised as described so that existing applications that call this method will not fail.

## See Also

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.html)
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.html)
[IConfiguration::IsSpeedPak Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IsSpeedPak.html)
[IConfiguration::UpdateSpeedPak Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~UpdateSpeedPak.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
