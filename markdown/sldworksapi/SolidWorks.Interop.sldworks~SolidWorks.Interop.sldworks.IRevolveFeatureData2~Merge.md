---
title: "Merge Property (IRevolveFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IRevolveFeatureData2"
member: "Merge"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~Merge.html"
---

# Merge Property (IRevolveFeatureData2)

Gets or sets whether to merge the results of this revolve feature in a multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Property Merge As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRevolveFeatureData2
Dim value As System.Boolean

instance.Merge = value

value = instance.Merge
```

### C#

```csharp
System.bool Merge {get; set;}
```

### C++/CLI

```cpp
property System.bool Merge {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True enables the merge results option, false disables it

## VBA Syntax

See [RevolveFeatureData2::Merge](ms-its:sldworksapivb6.chm::/sldworks~RevolveFeatureData2~Merge.html).

## Remarks

SOLIDWORKS 2003 FCS, Revision Number 11.0

## See Also

[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.html)
[IRevolveFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
