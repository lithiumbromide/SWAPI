---
title: "AddCustomInfo3 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "AddCustomInfo3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~AddCustomInfo3.html"
---

# AddCustomInfo3 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::AddCustomInfo3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~AddCustomInfo3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddCustomInfo3( _
   ByVal Configuration As System.String, _
   ByVal FieldName As System.String, _
   ByVal FieldType As System.Integer, _
   ByVal FieldValue As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Configuration As System.String
Dim FieldName As System.String
Dim FieldType As System.Integer
Dim FieldValue As System.String
Dim value As System.Boolean

value = instance.AddCustomInfo3(Configuration, FieldName, FieldType, FieldValue)
```

### C#

```csharp
System.bool AddCustomInfo3(
   System.string Configuration,
   System.string FieldName,
   System.int FieldType,
   System.string FieldValue
)
```

### C++/CLI

```cpp
System.bool AddCustomInfo3(
   System.String^ Configuration,
   System.String^ FieldName,
   System.int FieldType,
   System.String^ FieldValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Configuration`:
- `FieldName`:
- `FieldType`:
- `FieldValue`:

## VBA Syntax

See [ModelDoc::AddCustomInfo3](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~AddCustomInfo3.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
