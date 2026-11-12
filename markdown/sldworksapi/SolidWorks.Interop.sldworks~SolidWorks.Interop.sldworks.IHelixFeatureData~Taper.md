---
title: "Taper Property (IHelixFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHelixFeatureData"
member: "Taper"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~Taper.html"
---

# Taper Property (IHelixFeatureData)

Gets or sets whether this constant-pitch helix feature is tapered.

## Syntax

### Visual Basic (Declaration)

```vb
Property Taper As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IHelixFeatureData
Dim value As System.Boolean

instance.Taper = value

value = instance.Taper
```

### C#

```csharp
System.bool Taper {get; set;}
```

### C++/CLI

```cpp
property System.bool Taper {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if helix is tapered, false if not tapered

## VBA Syntax

See [HelixFeatureData::Taper](ms-its:sldworksapivb6.chm::/sldworks~HelixFeatureData~Taper.html).

## See Also

[IHelixFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.html)
[IHelixFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
