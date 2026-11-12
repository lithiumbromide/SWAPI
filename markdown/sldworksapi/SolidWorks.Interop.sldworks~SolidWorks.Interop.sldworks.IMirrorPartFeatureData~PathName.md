---
title: "PathName Property (IMirrorPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorPartFeatureData"
member: "PathName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~PathName.html"
---

# PathName Property (IMirrorPartFeatureData)

Gets the path and file name of the derived mirror part feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PathName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorPartFeatureData
Dim value As System.String

value = instance.PathName
```

### C#

```csharp
System.string PathName {get;}
```

### C++/CLI

```cpp
property System.String^ PathName {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Path and file name of the derived mirror part feature

## VBA Syntax

See [MirrorPartFeatureData::PathName](ms-its:sldworksapivb6.chm::/sldworks~MirrorPartFeatureData~PathName.html).

## Examples

See the [IMirrorPartFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMirrorPartFeatureData.html) examples.

## See Also

[IMirrorPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData.html)
[IMirrorPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
