---
title: "D2ReverseOffset Property (IBaseFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData"
member: "D2ReverseOffset"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~D2ReverseOffset.html"
---

# D2ReverseOffset Property (IBaseFlangeFeatureData)

Gets or sets whether the offset for Direction 2 is reversed for this base flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D2ReverseOffset As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBaseFlangeFeatureData
Dim value As System.Boolean

instance.D2ReverseOffset = value

value = instance.D2ReverseOffset
```

### C#

```csharp
System.bool D2ReverseOffset {get; set;}
```

### C++/CLI

```cpp
property System.bool D2ReverseOffset {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True reverses the offset false does not

## VBA Syntax

See [BaseFlangeFeatureData::D2ReverseOffset](ms-its:sldworksapivb6.chm::/sldworks~BaseFlangeFeatureData~D2ReverseOffset.html).

## See Also

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html)
[IBaseFlangeFeatureData::D1ReverseOffset Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~D1ReverseOffset.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
