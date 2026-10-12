---
title: "Size Property (ICosmeticThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticThreadFeatureData"
member: "Size"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~Size.html"
---

# Size Property (ICosmeticThreadFeatureData)

Gets or sets the thread size.

## Syntax

### Visual Basic (Declaration)

```vb
Property Size As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticThreadFeatureData
Dim value As System.String

instance.Size = value

value = instance.Size
```

### C#

```csharp
System.string Size {get; set;}
```

### C++/CLI

```cpp
property System.String^ Size {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Thread size

## VBA Syntax

See [CosmeticThreadFeatureData::Size](ms-its:sldworksapivb6.chm::/sldworks~CosmeticThreadFeatureData~Size.html).

## Examples

See the [ICosmeticThreadFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticThreadFeatureData.html) examples.

## See Also

[ICosmeticThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData.html)
[ICosmeticThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
