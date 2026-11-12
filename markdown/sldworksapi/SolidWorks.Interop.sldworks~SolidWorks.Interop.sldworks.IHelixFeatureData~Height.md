---
title: "Height Property (IHelixFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHelixFeatureData"
member: "Height"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~Height.html"
---

# Height Property (IHelixFeatureData)

Gets or sets the height of this helix feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Height As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IHelixFeatureData
Dim value As System.Double

instance.Height = value

value = instance.Height
```

### C#

```csharp
System.double Height {get; set;}
```

### C++/CLI

```cpp
property System.double Height {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Height (see **Remarks**)

## VBA Syntax

See [HelixFeatureData::Height](ms-its:sldworksapivb6.chm::/sldworks~HelixFeatureData~Height.html).

## Remarks

If the [helix is defined](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHelixFeatureData~DefinedBy.html) as swHelixDefinedBy_e.swHelixDefinedByPitchAndRevolution, then you cannot change the height of the helix.

## See Also

[IHelixFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.html)
[IHelixFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
