---
title: "Get Method (ICustomPropertyManager)"
project: "SOLIDWORKS API Help"
interface: "ICustomPropertyManager"
member: "Get"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Get.html"
---

# Get Method (ICustomPropertyManager)

Obsolete. Superseded by [ICustomPropertyManager::Get2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomPropertyManager~Get2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function Get( _
   ByVal FieldName As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomPropertyManager
Dim FieldName As System.String
Dim value As System.String

value = instance.Get(FieldName)
```

### C#

```csharp
System.string Get(
   System.string FieldName
)
```

### C++/CLI

```cpp
System.String^ Get(
   System.String^ FieldName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FieldName`:

## VBA Syntax

See [CustomPropertyManager::Get](ms-its:sldworksapivb6.chm::/sldworks~CustomPropertyManager~Get.html).

## See Also

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.html)
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.html)
