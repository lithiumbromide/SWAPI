---
title: "Profiles Property (ILoftedBendsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftedBendsFeatureData"
member: "Profiles"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~Profiles.html"
---

# Profiles Property (ILoftedBendsFeatureData)

Gets or sets the profiles for this lofted bends feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Profiles As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftedBendsFeatureData
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

Array of profiles for this lofted bends feature

## VBA Syntax

See [LoftedBendsFeatureData::Profiles](ms-its:sldworksapivb6.chm::/sldworks~LoftedBendsFeatureData~Profiles.html).

## See Also

[ILoftedBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData.html)
[ILoftedBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData_members.html)
[ILoftedBendsFeatureData::GetProfileCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~GetProfileCount.html)
[ILoftedBendsFeatureData::IGetProfiles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~IGetProfiles.html)
[ILoftedBendsFeatureData::ISetProfiles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~ISetProfiles.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
