---
title: "IndentWidth Property (ISMGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISMGussetFeatureData"
member: "IndentWidth"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~IndentWidth.html"
---

# IndentWidth Property (ISMGussetFeatureData)

Gets or sets the indent width of this gusset.

## Syntax

### Visual Basic (Declaration)

```vb
Property IndentWidth As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISMGussetFeatureData
Dim value As System.Double

instance.IndentWidth = value

value = instance.IndentWidth
```

### C#

```csharp
System.double IndentWidth {get; set;}
```

### C++/CLI

```cpp
property System.double IndentWidth {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Indent width

## VBA Syntax

See [SMGussetFeatureData::IndentWidth](ms-its:sldworksapivb6.chm::/sldworks~SMGussetFeatureData~IndentWidth.html).

## Examples

See the examples for [ISMGussetFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData.html).

## Remarks

This property is valid only if [ISMGussetFeatureData::ProfileDimensionScheme](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData~ProfileDimensionScheme.html) is set to 0.

## See Also

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html)
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
