---
title: "UseReverse Property (IEndCapFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEndCapFeatureData"
member: "UseReverse"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData~UseReverse.html"
---

# UseReverse Property (IEndCapFeatureData)

Gets or sets whether to reverse the offset of this end cap feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseReverse As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEndCapFeatureData
Dim value As System.Boolean

instance.UseReverse = value

value = instance.UseReverse
```

### C#

```csharp
System.bool UseReverse {get; set;}
```

### C++/CLI

```cpp
property System.bool UseReverse {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reverse the offset, false to not

## VBA Syntax

See [EndCapFeatureData::UseReverse](ms-its:sldworksapivb6.chm::/sldworks~EndCapFeatureData~UseReverse.html).

## Examples

See the [IEndCapFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEndCapFeatureData.html) examples.

## See Also

[IEndCapFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData.html)
[IEndCapFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
