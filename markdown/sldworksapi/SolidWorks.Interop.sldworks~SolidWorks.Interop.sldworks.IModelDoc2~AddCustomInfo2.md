---
title: "AddCustomInfo2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "AddCustomInfo2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddCustomInfo2.html"
---

# AddCustomInfo2 Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::CustomPropertyManager](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~CustomPropertyManager.html).

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
Dim instance As IModelDoc2
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

See [ModelDoc2::AddCustomInfo2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~AddCustomInfo2.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
