---
title: "TrimSideBends Property (ISweptFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweptFlangeFeatureData"
member: "TrimSideBends"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~TrimSideBends.html"
---

# TrimSideBends Property (ISweptFlangeFeatureData)

Gets or sets whether to remove extra material in neighboring bends of this swept flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property TrimSideBends As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISweptFlangeFeatureData
Dim value As System.Boolean

instance.TrimSideBends = value

value = instance.TrimSideBends
```

### C#

```csharp
System.bool TrimSideBends {get; set;}
```

### C++/CLI

```cpp
property System.bool TrimSideBends {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to trim extra material in neighboring bends, false to not

## VBA Syntax

See [SweptFlangeFeatureData::TrimSideBends](ms-its:sldworksapivb6.chm::/sldworks~SweptFlangeFeatureData~TrimSideBends.html).

## Examples

See the [ISweptFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html) examples.

## See Also

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html)
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
