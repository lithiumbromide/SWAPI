---
title: "SetPreservedRegionSetting Method (ICWTopologyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyStudyOptions"
member: "SetPreservedRegionSetting"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyOptions~SetPreservedRegionSetting.html"
---

# SetPreservedRegionSetting Method (ICWTopologyStudyOptions)

Sets the preserved region setting.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetPreservedRegionSetting( _
   ByVal NPreservedRegionSetting As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyStudyOptions
Dim NPreservedRegionSetting As System.Integer

instance.SetPreservedRegionSetting(NPreservedRegionSetting)
```

### C#

```csharp
void SetPreservedRegionSetting(
   System.int NPreservedRegionSetting
)
```

### C++/CLI

```cpp
void SetPreservedRegionSetting(
   System.int NPreservedRegionSetting
)
```

### Parameters

- `NPreservedRegionSetting`: Preserved region setting as defined in [swsTopologyPreservedRegionOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyPreservedRegionOption_e.html)

## VBA Syntax

See [CWTopologyStudyOptions::SetPreservedRegionSetting](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyStudyOptions~SetPreservedRegionSetting.html).

## See Also

[ICWTopologyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyOptions.html)
[ICWTopologyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
