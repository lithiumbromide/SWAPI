---
title: "GetCustomInfoType3 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "GetCustomInfoType3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~GetCustomInfoType3.html"
---

# GetCustomInfoType3 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::GetCustomInfoType3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetCustomInfoType3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCustomInfoType3( _
   ByVal Configuration As System.String, _
   ByVal FieldName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Configuration As System.String
Dim FieldName As System.String
Dim value As System.Integer

value = instance.GetCustomInfoType3(Configuration, FieldName)
```

### C#

```csharp
System.int GetCustomInfoType3(
   System.string Configuration,
   System.string FieldName
)
```

### C++/CLI

```cpp
System.int GetCustomInfoType3(
   System.String^ Configuration,
   System.String^ FieldName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Configuration`:
- `FieldName`:

## VBA Syntax

See [ModelDoc::GetCustomInfoType3](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~GetCustomInfoType3.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
