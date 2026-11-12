---
title: "Profiles Property (ILoftFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftFeatureData"
member: "Profiles"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~Profiles.html"
---

# Profiles Property (ILoftFeatureData)

Gets and sets the profiles for this loft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Profiles As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftFeatureData
Dim value As System.Object

instance.Profiles = value

value = instance.Profiles
```

### C#

```csharp
System.object Profiles {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Profiles {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Profiles for this loft

## VBA Syntax

See [LoftFeatureData::Profiles](ms-its:sldworksapivb6.chm::/sldworks~LoftFeatureData~Profiles.html).

## Remarks

Each profile returned is a [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object. A [ISketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html) object can be extracted from this Feature object by using [IFeature::GetSpecificFeature2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetSpecificFeature2.html).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.html)
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.html)
[ILoftFeatureData::GetProfileCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GetProfileCount.html)
[ILoftFeatureData::IGetProfiles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~IGetProfiles.html)
[ILoftFeatureData::ISetProfiles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~ISetProfiles.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
