---
title: "StartOffset Property (IMiterFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMiterFlangeFeatureData"
member: "StartOffset"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~StartOffset.html"
---

# StartOffset Property (IMiterFlangeFeatureData)

Gets or sets the start offset for this miter flange.

## Syntax

### Visual Basic (Declaration)

```vb
Property StartOffset As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMiterFlangeFeatureData
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

Start offset for this miter flange

## VBA Syntax

See [MiterFlangeFeatureData::StartOffset](ms-its:sldworksapivb6.chm::/sldworks~MiterFlangeFeatureData~StartOffset.html).

## See Also

[IMiterFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData.html)
[IMiterFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData_members.html)
[IMiterFlangeFeautreData::EndOffset Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~EndOffset.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
