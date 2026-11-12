---
title: "GetCustomInfoType Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "GetCustomInfoType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~GetCustomInfoType.html"
---

# GetCustomInfoType Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::GetCustomInfoType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetCustomInfoType.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCustomInfoType( _
   ByVal FieldName As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim FieldName As System.String
Dim value As System.String

value = instance.GetCustomInfoType(FieldName)
```

### C#

```csharp
System.string GetCustomInfoType(
   System.string FieldName
)
```

### C++/CLI

```cpp
System.String^ GetCustomInfoType(
   System.String^ FieldName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FieldName`:

## VBA Syntax

See [ModelDoc::GetCustomInfoType](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~GetCustomInfoType.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
