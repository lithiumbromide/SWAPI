---
title: "Merge Property (ILoftFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftFeatureData"
member: "Merge"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~Merge.html"
---

# Merge Property (ILoftFeatureData)

Gets or sets whether to merge the results of this loft feature in a multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Property Merge As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftFeatureData
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

True merges the results of this loft feature in a multibody part, false does not

## VBA Syntax

See [LoftFeatureData::Merge](ms-its:sldworksapivb6.chm::/sldworks~LoftFeatureData~Merge.html).

## Remarks

The merge results option tells the SOLIDWORKS Design software whether to merge the new body or bodies with existing bodies in the multibody part. This property is set to True by default.

## See Also

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.html)
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
