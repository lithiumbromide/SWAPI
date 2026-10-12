---
title: "NumberOfWeldPasses Property (ICosmeticWeldBeadFolder)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticWeldBeadFolder"
member: "NumberOfWeldPasses"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFolder~NumberOfWeldPasses.html"
---

# NumberOfWeldPasses Property (ICosmeticWeldBeadFolder)

Gets or sets the number of weld passes required to deposit the correct amount of welding material.

## Syntax

### Visual Basic (Declaration)

```vb
Property NumberOfWeldPasses As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticWeldBeadFolder
Dim value As System.Integer

instance.NumberOfWeldPasses = value

value = instance.NumberOfWeldPasses
```

### C#

```csharp
System.int NumberOfWeldPasses {get; set;}
```

### C++/CLI

```cpp
property System.int NumberOfWeldPasses {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of weld passes

## VBA Syntax

See [CosmeticWeldBeadFolder::NumberOfWeldPasses](ms-its:sldworksapivb6.chm::/sldworks~CosmeticWeldBeadFolder~NumberOfWeldPasses.html).

## Examples

See [ICosmeticWeldBeadFolder](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFolder.html) examples.

## See Also

[ICosmeticWeldBeadFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFolder.html)
[ICosmeticWeldBeadFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFolder_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
