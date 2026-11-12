---
title: "LightSourcePropertyValues Property (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "LightSourcePropertyValues"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~LightSourcePropertyValues.html"
---

# LightSourcePropertyValues Property (IModelDoc)

Obsolete. Superseded by [IModelDoc2::LightSourcePropertyValues](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~LightSourcePropertyValues.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property LightSourcePropertyValues( _
   ByVal ID As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim ID As System.Integer
Dim value As System.Object

instance.LightSourcePropertyValues(ID) = value

value = instance.LightSourcePropertyValues(ID)
```

### C#

```csharp
System.object LightSourcePropertyValues(
   System.int ID
) {get; set;}
```

### C++/CLI

```cpp
property System.Object^ LightSourcePropertyValues {
   System.Object^ get(System.int ID);
   void set (System.int ID, System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ID`:

## VBA Syntax

See [ModelDoc::LightSourcePropertyValues](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~LightSourcePropertyValues.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
