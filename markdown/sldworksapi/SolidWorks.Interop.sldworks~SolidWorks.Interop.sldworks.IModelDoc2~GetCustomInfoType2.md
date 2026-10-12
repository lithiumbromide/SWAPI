---
title: "GetCustomInfoType2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetCustomInfoType2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetCustomInfoType2.html"
---

# GetCustomInfoType2 Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::CustomPropertyManager](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~CustomPropertyManager.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCustomInfoType2( _
   ByVal FieldName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim FieldName As System.String
Dim value As System.Integer

value = instance.GetCustomInfoType2(FieldName)
```

### C#

```csharp
System.int GetCustomInfoType2(
   System.string FieldName
)
```

### C++/CLI

```cpp
System.int GetCustomInfoType2(
   System.String^ FieldName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FieldName`:

## VBA Syntax

See [ModelDoc2::GetCustomInfoType2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetCustomInfoType2.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
