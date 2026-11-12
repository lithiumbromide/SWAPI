---
title: "ShowCenter Property (ISMGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISMGussetFeatureData"
member: "ShowCenter"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ShowCenter.html"
---

# ShowCenter Property (ISMGussetFeatureData)

Gets or sets whether to display the center marks of the gusset in its flattened state.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowCenter As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISMGussetFeatureData
Dim value As System.Boolean

instance.ShowCenter = value

value = instance.ShowCenter
```

### C#

```csharp
System.bool ShowCenter {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowCenter {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to display the center marks of the flattened gusset, false to not

## VBA Syntax

See [SMGussetFeatureData::ShowCenter](ms-its:sldworksapivb6.chm::/sldworks~SMGussetFeatureData~ShowCenter.html).

## Examples

See the [ISMGussetFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html) examples.

## Remarks

This property is valid only if [ISMGussetFeatureData::OverrideDocSettings](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~OverrideDocSettings.html) is true.

## See Also

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html)
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.html)
[ISMGussetFeatureData::ShowProfile Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ShowProfile.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
