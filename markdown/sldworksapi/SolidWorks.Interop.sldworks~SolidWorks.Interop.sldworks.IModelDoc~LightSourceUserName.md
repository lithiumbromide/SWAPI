---
title: "LightSourceUserName Property (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "LightSourceUserName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~LightSourceUserName.html"
---

# LightSourceUserName Property (IModelDoc)

Obsolete. Superseded by [IModelDoc2::LightSourceUserName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~LightSourceUserName.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property LightSourceUserName( _
   ByVal ID As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim ID As System.Integer
Dim value As System.String

instance.LightSourceUserName(ID) = value

value = instance.LightSourceUserName(ID)
```

### C#

```csharp
System.string LightSourceUserName(
   System.int ID
) {get; set;}
```

### C++/CLI

```cpp
property System.String^ LightSourceUserName {
   System.String^ get(System.int ID);
   void set (System.int ID, System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ID`:

## VBA Syntax

See [ModelDoc::LightSourceUserName](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~LightSourceUserName.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
