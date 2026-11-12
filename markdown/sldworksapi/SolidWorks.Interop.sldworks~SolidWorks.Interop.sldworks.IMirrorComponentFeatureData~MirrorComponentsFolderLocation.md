---
title: "MirrorComponentsFolderLocation Property (IMirrorComponentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorComponentFeatureData"
member: "MirrorComponentsFolderLocation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~MirrorComponentsFolderLocation.html"
---

# MirrorComponentsFolderLocation Property (IMirrorComponentFeatureData)

Gets or sets the existing folder where all opposite-hand versions are saved.

## Syntax

### Visual Basic (Declaration)

```vb
Property MirrorComponentsFolderLocation As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorComponentFeatureData
Dim value As System.String

instance.MirrorComponentsFolderLocation = value

value = instance.MirrorComponentsFolderLocation
```

### C#

```csharp
System.string MirrorComponentsFolderLocation {get; set;}
```

### C++/CLI

```cpp
property System.String^ MirrorComponentsFolderLocation {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Existing folder name

## VBA Syntax

See [MirrorComponentFeatureData::MirrorComponentsFolderLocation](ms-its:sldworksapivb6.chm::/sldworks~MirrorComponentFeatureData~MirrorComponentsFolderLocation.html).

## Examples

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html) example.

## Remarks

This property is valid only if [IMirrorComponentFeatureData::PlaceFilesInOneFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~PlaceFilesInOneFolder.html) is true.

## See Also

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html)
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
