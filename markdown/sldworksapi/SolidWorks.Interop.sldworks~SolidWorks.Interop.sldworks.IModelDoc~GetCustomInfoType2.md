---
title: "GetCustomInfoType2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "GetCustomInfoType2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~GetCustomInfoType2.html"
---

# GetCustomInfoType2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::GetCustomInfoType2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetCustomInfoType2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCustomInfoType2( _
   ByVal FieldName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
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

See [ModelDoc::GetCustomInfoType2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~GetCustomInfoType2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
