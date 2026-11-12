---
title: "AddCustomInfo Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "AddCustomInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddCustomInfo.html"
---

# AddCustomInfo Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::CustomPropertyManager](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~CustomPropertyManager.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddCustomInfo( _
   ByVal FieldName As System.String, _
   ByVal FieldType As System.String, _
   ByVal FieldValue As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim FieldName As System.String
Dim FieldType As System.String
Dim FieldValue As System.String
Dim value As System.Boolean

value = instance.AddCustomInfo(FieldName, FieldType, FieldValue)
```

### C#

```csharp
System.bool AddCustomInfo(
   System.string FieldName,
   System.string FieldType,
   System.string FieldValue
)
```

### C++/CLI

```cpp
System.bool AddCustomInfo(
   System.String^ FieldName,
   System.String^ FieldType,
   System.String^ FieldValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FieldName`:
- `FieldType`:
- `FieldValue`:

## VBA Syntax

See [ModelDoc2::AddCustomInfo](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~AddCustomInfo.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
