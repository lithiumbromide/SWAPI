---
title: "OverrideDocSettings Property (ISMGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISMGussetFeatureData"
member: "OverrideDocSettings"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~OverrideDocSettings.html"
---

# OverrideDocSettings Property (ISMGussetFeatureData)

Gets or sets whether to override the document flat pattern properties.

## Syntax

### Visual Basic (Declaration)

```vb
Property OverrideDocSettings As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISMGussetFeatureData
Dim value As System.Boolean

instance.OverrideDocSettings = value

value = instance.OverrideDocSettings
```

### C#

```csharp
System.bool OverrideDocSettings {get; set;}
```

### C++/CLI

```cpp
property System.bool OverrideDocSettings {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to override the document flat pattern settings, false to not

## VBA Syntax

See [SMGussetFeatureData::OverrideDocSettings](ms-its:sldworksapivb6.chm::/sldworks~SMGussetFeatureData~OverrideDocSettings.html).

## Examples

See the [ISMGussetFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html) examples.

## See Also

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html)
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.html)
[ISMGussetFeatureData::ShowCenter Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ShowCenter.html)
[ISMGussetFeatureData::ShowProfile Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ShowProfile.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
