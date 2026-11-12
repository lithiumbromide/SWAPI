---
title: "Add Method (ICustomPropertyManager)"
project: "SOLIDWORKS API Help"
interface: "ICustomPropertyManager"
member: "Add"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Add.html"
---

# Add Method (ICustomPropertyManager)

Obsolete. Superseded by [ICustomPropertyManager::Add2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomPropertyManager~Add2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function Add( _
   ByVal FieldName As System.String, _
   ByVal FieldType As System.String, _
   ByVal FieldValue As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomPropertyManager
Dim FieldName As System.String
Dim FieldType As System.String
Dim FieldValue As System.String
Dim value As System.Integer

value = instance.Add(FieldName, FieldType, FieldValue)
```

### C#

```csharp
System.int Add(
   System.string FieldName,
   System.string FieldType,
   System.string FieldValue
)
```

### C++/CLI

```cpp
System.int Add(
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

See [CustomPropertyManager::Add](ms-its:sldworksapivb6.chm::/sldworks~CustomPropertyManager~Add.html).

## See Also

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.html)
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.html)
