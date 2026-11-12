---
title: "GetType Method (ICustomPropertyManager)"
project: "SOLIDWORKS API Help"
interface: "ICustomPropertyManager"
member: "GetType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~GetType.html"
---

# GetType Method (ICustomPropertyManager)

Obsolete. Superseded by [ICustomPropertyManager::GetType2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomPropertyManager~GetType2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetType( _
   ByVal FieldName As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomPropertyManager
Dim FieldName As System.String
Dim value As System.String

value = instance.GetType(FieldName)
```

### C#

```csharp
System.string GetType(
   System.string FieldName
)
```

### C++/CLI

```cpp
System.String^ GetType(
   System.String^ FieldName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FieldName`:

## VBA Syntax

See [CustomPropertyManager::GetType](ms-its:sldworksapivb6.chm::/sldworks~CustomPropertyManager~GetType.html).

## See Also

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.html)
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.html)
