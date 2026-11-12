---
title: "CustomInfo2 Property (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "CustomInfo2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CustomInfo2.html"
---

# CustomInfo2 Property (IModelDoc)

Obsolete. Superseded by [IModelDoc2::CustomInfo2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CustomInfo2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property CustomInfo2( _
   ByVal Configuration As System.String, _
   ByVal FieldName As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Configuration As System.String
Dim FieldName As System.String
Dim value As System.String

instance.CustomInfo2(Configuration, FieldName) = value

value = instance.CustomInfo2(Configuration, FieldName)
```

### C#

```csharp
System.string CustomInfo2(
   System.string Configuration,
   System.string FieldName
) {get; set;}
```

### C++/CLI

```cpp
property System.String^ CustomInfo2 {
   System.String^ get(System.String^ Configuration, System.String^ FieldName);
   void set (System.String^ Configuration, System.String^ FieldName, System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Configuration`:
- `FieldName`:

## VBA Syntax

See [ModelDoc::CustomInfo2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~CustomInfo2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
