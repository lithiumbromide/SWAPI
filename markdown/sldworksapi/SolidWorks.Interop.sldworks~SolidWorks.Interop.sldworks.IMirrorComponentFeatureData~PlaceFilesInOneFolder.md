---
title: "PlaceFilesInOneFolder Property (IMirrorComponentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorComponentFeatureData"
member: "PlaceFilesInOneFolder"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~PlaceFilesInOneFolder.html"
---

# PlaceFilesInOneFolder Property (IMirrorComponentFeatureData)

Gets or sets whether to place the opposite-hand versions in one folder.

## Syntax

### Visual Basic (Declaration)

```vb
Property PlaceFilesInOneFolder As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorComponentFeatureData
Dim value As System.Boolean

instance.PlaceFilesInOneFolder = value

value = instance.PlaceFilesInOneFolder
```

### C#

```csharp
System.bool PlaceFilesInOneFolder {get; set;}
```

### C++/CLI

```cpp
property System.bool PlaceFilesInOneFolder {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to place the opposite-hand files in one folder, false to not

## VBA Syntax

See [MirrorComponentFeatureData::PlaceFilesInOneFolder](ms-its:sldworksapivb6.chm::/sldworks~MirrorComponentFeatureData~PlaceFilesInOneFolder.html).

## Examples

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html) example.

## Remarks

This property is valid only if [IMirrorComponentFeatureData::CreateDerivedConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~CreateDerivedConfigurations.html) is false.

## See Also

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html)
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
