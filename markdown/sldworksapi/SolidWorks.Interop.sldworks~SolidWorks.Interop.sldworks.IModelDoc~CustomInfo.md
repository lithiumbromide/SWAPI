---
title: "CustomInfo Property (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "CustomInfo"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CustomInfo.html"
---

# CustomInfo Property (IModelDoc)

Obsolete. Superseded by [IModelDoc2::CustomInfo](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CustomInfo.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property CustomInfo( _
   ByVal FieldName As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim FieldName As System.String
Dim value As System.String

instance.CustomInfo(FieldName) = value

value = instance.CustomInfo(FieldName)
```

### C#

```csharp
System.string CustomInfo(
   System.string FieldName
) {get; set;}
```

### C++/CLI

```cpp
property System.String^ CustomInfo {
   System.String^ get(System.String^ FieldName);
   void set (System.String^ FieldName, System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FieldName`:

## VBA Syntax

See [ModelDoc::CustomInfo](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~CustomInfo.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
