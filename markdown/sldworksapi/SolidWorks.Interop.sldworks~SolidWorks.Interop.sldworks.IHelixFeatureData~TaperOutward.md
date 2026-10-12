---
title: "TaperOutward Property (IHelixFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHelixFeatureData"
member: "TaperOutward"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~TaperOutward.html"
---

# TaperOutward Property (IHelixFeatureData)

Gets or sets the direction of the taper for this constant-pitch helix feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property TaperOutward As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IHelixFeatureData
Dim value As System.Boolean

instance.TaperOutward = value

value = instance.TaperOutward
```

### C#

```csharp
System.bool TaperOutward {get; set;}
```

### C++/CLI

```cpp
property System.bool TaperOutward {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if outward, false if inward

## VBA Syntax

See [HelixFeatureData::TaperOutward](ms-its:sldworksapivb6.chm::/sldworks~HelixFeatureData~TaperOutward.html).

## See Also

[IHelixFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.html)
[IHelixFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
