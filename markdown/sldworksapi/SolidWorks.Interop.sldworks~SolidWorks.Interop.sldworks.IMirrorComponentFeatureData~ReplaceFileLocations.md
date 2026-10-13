---
title: "ReplaceFileLocations Property (IMirrorComponentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorComponentFeatureData"
member: "ReplaceFileLocations"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ReplaceFileLocations.html"
---

# ReplaceFileLocations Property (IMirrorComponentFeatureData)

Gets or sets the file locations of existing files that are to be replaced with new opposite-hand versions.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReplaceFileLocations As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorComponentFeatureData
Dim value As System.Object

instance.ReplaceFileLocations = value

value = instance.ReplaceFileLocations
```

### C#

```csharp
System.object ReplaceFileLocations {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ReplaceFileLocations {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of existing file paths

## VBA Syntax

See [MirrorComponentFeatureData::ReplaceFileLocations](ms-its:sldworksapivb6.chm::/sldworks~MirrorComponentFeatureData~ReplaceFileLocations.html).

## Examples

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html) example.

## Remarks

This property is valid only if:

- [IMirrorComponentFeatureData::CreateDerivedConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~CreateDerivedConfigurations.html) is false,

- and -

- [IMirrorComponentFeatureData::OppositeHandComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~OppositeHandComponents.html) is not Nothing or null. There is a one-to-one mapping between this property's array and IMirrorComponentFeatureData::OppositeHandComponents.

If this property is not set, it defaults to the current assembly's folder.

## See Also

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html)
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
