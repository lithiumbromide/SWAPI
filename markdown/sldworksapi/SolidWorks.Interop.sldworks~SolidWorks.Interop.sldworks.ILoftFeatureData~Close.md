---
title: "Close Property (ILoftFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftFeatureData"
member: "Close"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~Close.html"
---

# Close Property (ILoftFeatureData)

Gets or sets whether to close this loft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Close As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftFeatureData
Dim value As System.Boolean

instance.Close = value

value = instance.Close
```

### C#

```csharp
System.bool Close {get; set;}
```

### C++/CLI

```cpp
property System.bool Close {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True for closed loft features, false for open

## VBA Syntax

See [LoftFeatureData::Close](ms-its:sldworksapivb6.chm::/sldworks~LoftFeatureData~Close.html).

## See Also

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.html)
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
