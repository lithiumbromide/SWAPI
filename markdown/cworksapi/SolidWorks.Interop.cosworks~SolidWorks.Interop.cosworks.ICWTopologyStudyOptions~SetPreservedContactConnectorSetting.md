---
title: "SetPreservedContactConnectorSetting Method (ICWTopologyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyStudyOptions"
member: "SetPreservedContactConnectorSetting"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyOptions~SetPreservedContactConnectorSetting.html"
---

# SetPreservedContactConnectorSetting Method (ICWTopologyStudyOptions)

Sets the preserved contacts and connectors settings.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetPreservedContactConnectorSetting( _
   ByVal NPreservedContactConnectorSetting As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyStudyOptions
Dim NPreservedContactConnectorSetting As System.Integer

instance.SetPreservedContactConnectorSetting(NPreservedContactConnectorSetting)
```

### C#

```csharp
void SetPreservedContactConnectorSetting(
   System.int NPreservedContactConnectorSetting
)
```

### C++/CLI

```cpp
void SetPreservedContactConnectorSetting(
   System.int NPreservedContactConnectorSetting
)
```

### Parameters

- `NPreservedContactConnectorSetting`: Preserved contacts and connectors setting as defined in [swsTopologyPreservedContactConnectorOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyPreservedContactConnectorOption_e.html)

## VBA Syntax

See [CWTopologyStudyOptions::SetPreservedContactConnectorSetting](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyStudyOptions~SetPreservedContactConnectorSetting.html).

## See Also

[ICWTopologyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyOptions.html)
[ICWTopologyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
