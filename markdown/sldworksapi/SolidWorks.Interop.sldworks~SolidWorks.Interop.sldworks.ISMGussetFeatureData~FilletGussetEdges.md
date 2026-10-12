---
title: "FilletGussetEdges Property (ISMGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISMGussetFeatureData"
member: "FilletGussetEdges"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~FilletGussetEdges.html"
---

# FilletGussetEdges Property (ISMGussetFeatureData)

Gets or sets whether to fillet the edges of this gusset.

## Syntax

### Visual Basic (Declaration)

```vb
Property FilletGussetEdges As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISMGussetFeatureData
Dim value As System.Boolean

instance.FilletGussetEdges = value

value = instance.FilletGussetEdges
```

### C#

```csharp
System.bool FilletGussetEdges {get; set;}
```

### C++/CLI

```cpp
property System.bool FilletGussetEdges {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to fillet the edges of this gusset, false to not

## VBA Syntax

See [SMGussetFeatureData::FilletGussetEdges](ms-its:sldworksapivb6.chm::/sldworks~SMGussetFeatureData~FilletGussetEdges.html).

## Examples

See the examples for [ISMGussetFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData.html).

## Remarks

This property is valid only if [ISMGussetFeatureData::GussetType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData~GussetType.html) is set to 1.

After setting this property, set [ISMGussetFeatureData::EdgeFilletRadius](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData~EdgeFilletRadius.html).

## See Also

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html)
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
