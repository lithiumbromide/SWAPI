---
title: "StandardType Property (ICosmeticThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticThreadFeatureData"
member: "StandardType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~StandardType.html"
---

# StandardType Property (ICosmeticThreadFeatureData)

Gets or sets the thread standard type.

## Syntax

### Visual Basic (Declaration)

```vb
Property StandardType As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticThreadFeatureData
Dim value As System.String

instance.StandardType = value

value = instance.StandardType
```

### C#

```csharp
System.string StandardType {get; set;}
```

### C++/CLI

```cpp
property System.String^ StandardType {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Thread standard type

## VBA Syntax

See [CosmeticThreadFeatureData::StandardType](ms-its:sldworksapivb6.chm::/sldworks~CosmeticThreadFeatureData~StandardType.html).

## Examples

See the [ICosmeticThreadFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticThreadFeatureData.html) examples.

## See Also

[ICosmeticThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData.html)
[ICosmeticThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
