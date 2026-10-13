---
title: "Reverse Property (IScrewMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IScrewMateFeatureData"
member: "Reverse"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData~Reverse.html"
---

# Reverse Property (IScrewMateFeatureData)

Gets or sets whether to change the direction of movement of the components relative to one another.

## Syntax

### Visual Basic (Declaration)

```vb
Property Reverse As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IScrewMateFeatureData
Dim value As System.Boolean

instance.Reverse = value

value = instance.Reverse
```

### C#

```csharp
System.bool Reverse {get; set;}
```

### C++/CLI

```cpp
property System.bool Reverse {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reverse the direction of movement of the components, false to not

## VBA Syntax

See [ScrewMateFeatureData::Reverse](ms-its:sldworksapivb6.chm::/sldworks~ScrewMateFeatureData~Reverse.html).

## Examples

See the [IScrewMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData.html) example.

## See Also

[IScrewMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData.html)
[IScrewMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
