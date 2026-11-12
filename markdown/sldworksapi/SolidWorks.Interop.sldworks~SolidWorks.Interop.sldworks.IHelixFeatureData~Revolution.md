---
title: "Revolution Property (IHelixFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHelixFeatureData"
member: "Revolution"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~Revolution.html"
---

# Revolution Property (IHelixFeatureData)

Gets or sets the number of revolutions for this helix feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Revolution As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IHelixFeatureData
Dim value As System.Double

instance.Revolution = value

value = instance.Revolution
```

### C#

```csharp
System.double Revolution {get; set;}
```

### C++/CLI

```cpp
property System.double Revolution {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of revolutions (see **Remarks**)

## VBA Syntax

See [HelixFeatureData::Revolution](ms-its:sldworksapivb6.chm::/sldworks~HelixFeatureData~Revolution.html).

## Remarks

If the [helix is defined](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHelixFeatureData~DefinedBy.html) as swHelixDefinedBy_e.swHelixDefinedByHeightAndPitch, then you cannot change the number of revolutions in the helix.

You must specify a value greater than the previous region's revolution value and less than the next region's revolution value.

## See Also

[IHelixFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.html)
[IHelixFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Numbe 11.0
