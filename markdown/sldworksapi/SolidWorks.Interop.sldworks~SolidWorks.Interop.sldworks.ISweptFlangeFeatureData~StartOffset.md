---
title: "StartOffset Property (ISweptFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweptFlangeFeatureData"
member: "StartOffset"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~StartOffset.html"
---

# StartOffset Property (ISweptFlangeFeatureData)

Gets or sets the start offset of this swept flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property StartOffset As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISweptFlangeFeatureData
Dim value As System.Double

instance.StartOffset = value

value = instance.StartOffset
```

### C#

```csharp
System.double StartOffset {get; set;}
```

### C++/CLI

```cpp
property System.double StartOffset {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Start offset

## VBA Syntax

See [SweptFlangeFeatureData::StartOffset](ms-its:sldworksapivb6.chm::/sldworks~SweptFlangeFeatureData~StartOffset.html).

## Examples

See the [ISweptFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html) examples.

## Remarks

This property is valid only if [ISweptFlangeFeatureData::Path](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~Path.html) is an open loop.

If you want the swept flange to span the entire edge of the model, set both this property and [ISweptFlangeFeatureData::EndOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~EndOffset.html) to 0.0.

## See Also

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html)
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
