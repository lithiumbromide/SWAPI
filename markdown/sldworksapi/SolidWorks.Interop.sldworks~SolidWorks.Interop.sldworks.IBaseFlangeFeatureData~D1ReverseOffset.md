---
title: "D1ReverseOffset Property (IBaseFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData"
member: "D1ReverseOffset"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~D1ReverseOffset.html"
---

# D1ReverseOffset Property (IBaseFlangeFeatureData)

Gets or sets whether the offset for Direction 1 is reversed for this base flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D1ReverseOffset As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBaseFlangeFeatureData
Dim value As System.Boolean

instance.D1ReverseOffset = value

value = instance.D1ReverseOffset
```

### C#

```csharp
System.bool D1ReverseOffset {get; set;}
```

### C++/CLI

```cpp
property System.bool D1ReverseOffset {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True reverses the offset, false does not

## VBA Syntax

See [BaseFlangeFeatureData::D1ReverseOffset](ms-its:sldworksapivb6.chm::/sldworks~BaseFlangeFeatureData~D1ReverseOffset.html).

## See Also

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html)
[IBaseFlangeFeatureData::D2ReverseOffset Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~D2ReverseOffset.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
