---
title: "CustomInfo Property (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "CustomInfo"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CustomInfo.html"
---

# CustomInfo Property (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::CustomPropertyManager](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~CustomPropertyManager.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property CustomInfo( _
   ByVal FieldName As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
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

See [ModelDoc2::CustomInfo](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~CustomInfo.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
