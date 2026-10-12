---
title: "EndOffset Property (IMiterFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMiterFlangeFeatureData"
member: "EndOffset"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~EndOffset.html"
---

# EndOffset Property (IMiterFlangeFeatureData)

Gets or sets the end offset for this miter flange.

## Syntax

### Visual Basic (Declaration)

```vb
Property EndOffset As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMiterFlangeFeatureData
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

## VBA Syntax

See [MiterFlangeFeatureData::EndOffset](ms-its:sldworksapivb6.chm::/sldworks~MiterFlangeFeatureData~EndOffset.html).

## See Also

[IMiterFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData.html)
[IMiterFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData_members.html)
[IMiterFlangeFeatureData::StartOffset Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~StartOffset.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
