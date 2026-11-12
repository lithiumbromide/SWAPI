---
title: "NumberOfSections Property (ILoftFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftFeatureData"
member: "NumberOfSections"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~NumberOfSections.html"
---

# NumberOfSections Property (ILoftFeatureData)

Gets and sets the number of sections in this loft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property NumberOfSections As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftFeatureData
Dim value As System.Double

instance.NumberOfSections = value

value = instance.NumberOfSections
```

### C#

```csharp
System.double NumberOfSections {get; set;}
```

### C++/CLI

```cpp
property System.double NumberOfSections {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of sections

## VBA Syntax

See [LoftFeatureData::NumberOfSections](ms-its:sldworksapivb6.chm::/sldworks~LoftFeatureData~NumberOfSections.html).

## See Also

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.html)
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
