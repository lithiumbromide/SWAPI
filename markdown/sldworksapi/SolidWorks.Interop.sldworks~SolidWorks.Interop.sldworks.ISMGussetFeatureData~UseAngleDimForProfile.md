---
title: "UseAngleDimForProfile Property (ISMGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISMGussetFeatureData"
member: "UseAngleDimForProfile"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~UseAngleDimForProfile.html"
---

# UseAngleDimForProfile Property (ISMGussetFeatureData)

Gets or sets whether to dimension this gusset using an angle.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseAngleDimForProfile As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISMGussetFeatureData
Dim value As System.Boolean

instance.UseAngleDimForProfile = value

value = instance.UseAngleDimForProfile
```

### C#

```csharp
System.bool UseAngleDimForProfile {get; set;}
```

### C++/CLI

```cpp
property System.bool UseAngleDimForProfile {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use an angle to dimension this gusset, false to not

## VBA Syntax

See [SMGussetFeatureData::UseAngleDimForProfile](ms-its:sldworksapivb6.chm::/sldworks~SMGussetFeatureData~UseAngleDimForProfile.html).

## Examples

See the [ISMGussetFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html) examples.

## Remarks

This property is valid only if [ISMGussetFeatureData::ProfileDimensionScheme](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData~ProfileDimensionScheme.html) is set to 1.

After setting this property to true, set [ISMGussetFeatureData::ProfileAngleDim](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData~ProfileAngleDim.html).

See the [ISMGussetFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html) Remarks.

## See Also

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html)
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
