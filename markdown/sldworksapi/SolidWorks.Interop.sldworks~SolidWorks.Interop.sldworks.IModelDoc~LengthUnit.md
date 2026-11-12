---
title: "LengthUnit Property (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "LengthUnit"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~LengthUnit.html"
---

# LengthUnit Property (IModelDoc)

Obsolete. Superseded by [IModelDoc2::LengthUnit](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~LengthUnit.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property LengthUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim value As System.Integer

instance.LengthUnit = value

value = instance.LengthUnit
```

### C#

```csharp
System.int LengthUnit {get; set;}
```

### C++/CLI

```cpp
property System.int LengthUnit {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc::LengthUnit](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~LengthUnit.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
