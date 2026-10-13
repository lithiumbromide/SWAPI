---
title: "AddCustomInfo2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "AddCustomInfo2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~AddCustomInfo2.html"
---

# AddCustomInfo2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::AddCustomInfo2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~AddCustomInfo2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddCustomInfo2( _
   ByVal FieldName As System.String, _
   ByVal FieldType As System.Integer, _
   ByVal FieldValue As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim FieldName As System.String
Dim FieldType As System.Integer
Dim FieldValue As System.String
Dim value As System.Boolean

value = instance.AddCustomInfo2(FieldName, FieldType, FieldValue)
```

### C#

```csharp
System.bool AddCustomInfo2(
   System.string FieldName,
   System.int FieldType,
   System.string FieldValue
)
```

### C++/CLI

```cpp
System.bool AddCustomInfo2(
   System.String^ FieldName,
   System.int FieldType,
   System.String^ FieldValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FieldName`:
- `FieldType`:
- `FieldValue`:

## VBA Syntax

See [ModelDoc::AddCustomInfo2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~AddCustomInfo2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
