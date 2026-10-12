---
title: "Merge Property (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "Merge"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~Merge.html"
---

# Merge Property (IExtrudeFeatureData2)

Gets or sets whether to merge the results of the extrude feature in a multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Property Merge As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
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

See [ExtrudeFeatureData2::Merge](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~Merge.html).

## Remarks

The merge results option tells the SOLIDWORKS Design software whether or not to merge the
new body or bodies with existing bodies in the multibody part. This property is set
to True by default.

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
