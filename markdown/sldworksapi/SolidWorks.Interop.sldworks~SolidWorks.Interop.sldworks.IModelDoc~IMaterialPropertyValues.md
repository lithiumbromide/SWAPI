---
title: "IMaterialPropertyValues Property (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "IMaterialPropertyValues"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IMaterialPropertyValues.html"
---

# IMaterialPropertyValues Property (IModelDoc)

Obsolete. Superseded by [IModelDoc2::IMaterialPropertyValues](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IMaterialPropertyValues.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property IMaterialPropertyValues As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim value As System.Double

instance.IMaterialPropertyValues = value

value = instance.IMaterialPropertyValues
```

### C#

```csharp
System.double IMaterialPropertyValues {get; set;}
```

### C++/CLI

```cpp
property System.double IMaterialPropertyValues {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc::IMaterialPropertyValues](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~IMaterialPropertyValues.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
