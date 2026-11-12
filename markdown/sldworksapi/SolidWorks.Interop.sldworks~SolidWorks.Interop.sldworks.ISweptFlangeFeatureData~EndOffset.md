---
title: "EndOffset Property (ISweptFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweptFlangeFeatureData"
member: "EndOffset"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~EndOffset.html"
---

# EndOffset Property (ISweptFlangeFeatureData)

Gets or sets the end offset of this swept flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property EndOffset As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISweptFlangeFeatureData
Dim value As System.Double

instance.EndOffset = value

value = instance.EndOffset
```

### C#

```csharp
System.double EndOffset {get; set;}
```

### C++/CLI

```cpp
property System.double EndOffset {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

End offset

## VBA Syntax

See [SweptFlangeFeatureData::EndOffset](ms-its:sldworksapivb6.chm::/sldworks~SweptFlangeFeatureData~EndOffset.html).

## Examples

See the [ISweptFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html) examples.

## Remarks

This property is valid only if [ISweptFlangeFeatureData::Path](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~Path.html) is an open loop.

If you want the swept flange to span the entire edge of the model, set both this property and [ISweptFlangeFeatureData::StartOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~StartOffset.html) to 0.0.

## See Also

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html)
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
