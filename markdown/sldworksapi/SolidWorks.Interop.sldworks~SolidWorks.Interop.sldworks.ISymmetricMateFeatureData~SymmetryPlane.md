---
title: "SymmetryPlane Property (ISymmetricMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISymmetricMateFeatureData"
member: "SymmetryPlane"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData~SymmetryPlane.html"
---

# SymmetryPlane Property (ISymmetricMateFeatureData)

Gets or sets the symmetry plane of this symmetry mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property SymmetryPlane As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISymmetricMateFeatureData
Dim value As System.Object

instance.SymmetryPlane = value

value = instance.SymmetryPlane
```

### C#

```csharp
System.object SymmetryPlane {get; set;}
```

### C++/CLI

```cpp
property System.Object^ SymmetryPlane {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Front, Top, or Right plane or [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html)

## VBA Syntax

See [SymmetricMateFeatureData::SymmetryPlane](ms-its:sldworksapivb6.chm::/sldworks~SymmetricMateFeatureData~SymmetryPlane.html).

## Examples

See the [ISymmetricMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData.html) examples.

## See Also

[ISymmetricMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData.html)
[ISymmetricMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
