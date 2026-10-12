---
title: "ShowProfile Property (ISMGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISMGussetFeatureData"
member: "ShowProfile"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ShowProfile.html"
---

# ShowProfile Property (ISMGussetFeatureData)

Gets or sets whether to display the profile of the gusset in its flattened state.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowProfile As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISMGussetFeatureData
Dim value As System.Boolean

instance.ShowProfile = value

value = instance.ShowProfile
```

### C#

```csharp
System.bool ShowProfile {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowProfile {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to display the profile of the flattened gusset, false to not

## VBA Syntax

See [SMGussetFeatureData::ShowProfile](ms-its:sldworksapivb6.chm::/sldworks~SMGussetFeatureData~ShowProfile.html).

## Examples

See the [ISMGussetFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html) examples.

## Remarks

This property is valid only if [ISMGussetFeatureData::OverrideDocSettings](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~OverrideDocSettings.html) is true.

## See Also

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html)
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.html)
[ISMGussetFeatureData::ShowCenter Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ShowCenter.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
