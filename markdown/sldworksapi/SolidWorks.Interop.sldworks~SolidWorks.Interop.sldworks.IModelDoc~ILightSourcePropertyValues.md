---
title: "ILightSourcePropertyValues Property (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "ILightSourcePropertyValues"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ILightSourcePropertyValues.html"
---

# ILightSourcePropertyValues Property (IModelDoc)

Obsolete. Superseded by [IModelDoc2::ILightSourcePropertyValues](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ILightSourcePropertyValues.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property ILightSourcePropertyValues( _
   ByVal ID As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim ID As System.Integer
Dim value As System.Double

instance.ILightSourcePropertyValues(ID) = value

value = instance.ILightSourcePropertyValues(ID)
```

### C#

```csharp
System.double ILightSourcePropertyValues(
   System.int ID
) {get; set;}
```

### C++/CLI

```cpp
property System.double ILightSourcePropertyValues {
   System.double get(System.int ID);
   void set (System.int ID, System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ID`:

## VBA Syntax

See [ModelDoc::ILightSourcePropertyValues](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~ILightSourcePropertyValues.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
